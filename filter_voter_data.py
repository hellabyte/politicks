import pandas as pd
import sys,os

def main(xls_to_filter):
  """
    Takes an xls, filters it, and saves new result to csv with 
    '_filtered' appended to original prefix.
  """
  # Load the xls into the dataframe object and rename the columns 
  # NOTE: PAN is the PermanentAbsenteeName status, either 'Y' or 'N'
  #       for yes or no.
  df = pd.read_excel(xls_to_filter,names=['VANID','LastName','FirstName','Address','City','State','Zip5','PAN'])
  # Only keep addresses for Permanent Absentee Voters
  df = df[df.PAN == 'Y']
  # Remove address duplicates
  df = df.drop_duplicates(['Address','City','State','Zip5'])
  # Remove addresses that appear to not be homes by negating matches to
  #   Apartments
  #   Suites
  #   Units
  #   Post Office Boxes
  df = df[~df.Address.str.contains(' [aA][pP][tT].? | [aA][pP][aA][rR][tT][mM][eE][nN][tT] | [sS][tT][eE].? | [sS][uU][iI][tT][eE] |#| unit | [pP].?[oO].? ')]

  xls_path     = '/'.join(xls_to_filter.split('/')[:-1])
  xls_prefix   = xls_to_filter.split('/')[-1].split('.')[0]
  csv_filtered = f'{xls_path:s}{xls_prefix:s}_filtered.csv'
  df.to_csv(csv_filtered,index=False)
  return None

if __name__ == '__main__':
  xls_to_filter = sys.argv[1]
  main(xls_to_filter)

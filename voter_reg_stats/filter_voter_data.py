import pandas as pd
import sys,os

def main(csv_to_filter):
  """
    Takes a csv, filters it, and saves new result to csv with 
    '_filtered' appended to original prefix.
  """
  # Load the csv into the dataframe object and rename the columns 
  # NOTE: PAN is the PermanentAbsenteeName status, either 'Y' or 'N'
  #       for yes or no.
  df = pd.read_csv(csv_to_filter,names=['VANID','LastName','FirstName','Address','City','State','Zip5','PAN'])
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

  csv_path     = '/'.join(csv_to_filter.split('/')[:-1])
  csv_prefix   = csv_to_filter.split('/')[-1].split('.csv')[0]
  csv_filtered = f'{csv_path:s}{csv_prefix:s}_filtered.csv'
  df.to_csv(csv_filtered,index=False)
  return None

if __name__ == '__main__':
  csv_to_filter = sys.argv[1]
  main(csv_to_filter)

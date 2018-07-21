#!/usr/bin/env python
import pandas as pd
import sys,os
import glob,natsort

if __name__ == '__main__':
  glob_base = sys.argv[1]
  glob_list = natsort.natsorted(glob.glob(glob_base))
  dfs = pd.concat([ pd.read_excel(filtered_xls) for filtered_xls in glob_list ])
  dfs.to_excel('mailer_combo.xls',index=False)  

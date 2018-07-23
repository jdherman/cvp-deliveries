import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

years = ['01','02','03','04','05','06', 
         '07', '08', '09', '10']

# THIS DOES NOT WORK
# not recognizing delimiters
for year in years:
  for table in range(21,30):
    fname = 'prns/tab%d%s.prn' % (table, year)
    df = pd.read_table(fname, header=5,
                       skip_blank_lines=True,
                       skipinitialspace=True,)
    print(df)
    # df.to_csv('tab%d%s.csv' % (table,year))
    error
      # yr2 = '19'
      # df.to_csv('csvs/table_%d_%s%s.csv' % (table, yr2, year))

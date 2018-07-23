import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

years = ['93','94','95','96','97','98','99',
         '00','01','02','03','04','05','06', 
         '07', '08', '09', '10']

# THIS DOES NOT WORK

for year in years:
  for table in range(21,30):
    fname = 'txts/tab%d%s.prn' % (table, year)
    df = pd.read_table(fname)
    print(df)
    error
      # yr2 = '19'
      # df.to_csv('csvs/table_%d_%s%s.csv' % (table, yr2, year))

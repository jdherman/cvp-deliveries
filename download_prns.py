import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from subprocess import call

years = ['01','02','03','04','05','06', 
         '07', '08', '09', '10']

for year in years:
  for table in range(21,30):
    fname = 'tab%d%s' % (table, year)
    link = 'https://usbr.gov/mp/cvo/vungvari/%s.prn' % fname
    call(['wget', link])
    print(fname)
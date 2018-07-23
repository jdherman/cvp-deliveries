import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from subprocess import call

years = ['93','94','95','96','97','98','99','00']
ct = 0

for year in years:
  r = range(30,39) if ct < 5 else range(21,30)

  for table in r:
    fname = 'tab%d%s' % (table, year)
    link = 'https://usbr.gov/mp/cvo/vungvari/%s.txt' % fname
    call(['wget', link])
    print(fname)

  ct += 1
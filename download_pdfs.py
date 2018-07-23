import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from subprocess import call

for year in range(2011,2019):
  for table in range(21,30):
    fname = 'table_%d_%d' % (table, year)
    link = 'https://usbr.gov/mp/cvo/vungvari/%s.pdf' % fname
    call(['wget', link])
    print(fname)
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from tabula import read_pdf

# after this: pip install tabula-py
# and install homebrew java (NOT default java)

for year in range(2011,2019):
  for table in range(21,30):
    try:
      fname = 'pdfs/table_%d_%d.pdf' % (table, year)
      df = read_pdf(fname)
      df.to_csv('csvs/table_%d_%d.csv' % (table, year))
    except:
      pass

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import glob

suf = '_clean.txt'
all_files = glob.glob('*.txt')
for filename in all_files:
	newfilename = filename.split('.')[0] + suf
	data = pd.read_csv(filename,sep = ' *\| *');
	data = data.drop(['Redshift Flag','No.','Separation','References','Notes','Photometry Points','Positions','Redshift Points','Diameter Points','Associations'],axis = 'columns')
	data = data.dropna()
	data = data[data.Type == 'G'].reset_index()
	data = data.drop(['Type','index'],axis = 'columns');
	data.to_csv(newfilename,index = False)

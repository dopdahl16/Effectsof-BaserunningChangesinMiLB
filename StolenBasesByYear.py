import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

MiLBSBData = pd.read_csv('MiLMSBData.csv')

sns.lmplot(x='Year', y='SBs', data=MiLBSBData, hue='League')
plt.show()

MiLBSBData.groupby(['Year','League'])['SBs'].mean()
MiLBSBData.groupby(['Year'])['SBs'].mean()
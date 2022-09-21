import researchpy as rp
import pandas as pd

df = pd.read_csv('/Users/marialozano/Documents/GitHub/descriptives-realpython/data.csv')
df
rp.codebook(df)

##example of giving a descriptive for a single or group of continuous variables 
rp.summary_cont(df[['Age','HR','sBP']])
rp.summary_cat(df[['Group','Smoke']]) ##we get the value count but also the percentage as it relates to the proportion of values that fit to that subgroup


df['Group'].value_counts() ##would give us the same return as ^ function but without our researchpy package


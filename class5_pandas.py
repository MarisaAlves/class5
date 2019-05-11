import pandas as pd

#creating dataframe from files

insurance_df = pd.read_csv(filepath_or_buffer = '~/Downloads/insurance.csv', sep =',', header=0)
#print(insurance_df.to_string())

print(insurance_df[['age']])







print(insurance_df.columns)
print(insurance_df.index)
print(insurance_df.dtypes)
print(insurance_df.shape)
print(insurance_df.info())
print(insurance_df.describe())








#to add columns names, or replace existing ones: insurance_df.columns = ['a','b','c','d','e']

#printing the first 5 lines of age, children, charges
print(insurance_df.loc[0:4, ('age', 'children', 'charges')])
#or
print(insurance_df[['age','children', 'charges']].head(5))

#print mean of charges
print("Mean of charges=", insurance_df['charges'].mean())

print()

#print row where the charges value is 10797.3362
print(insurance_df.loc[insurance_df['charges']==10797.3362])
#or
print(insurance_df[insurance_df['charges']==10797.3362])



#printing age of person who paid maximum charge
print(insurance_df[insurance_df['charges']==insurance_df['charges'].max()])

print(insurance_df['region'].value_counts())
print(insurance_df['children'].value_counts())


#correlation method. To print a correlation matrix. Should usually normalize to have the values all on the same scale
print(insurance_df.corr())
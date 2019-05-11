import pandas as pd
import os
import matplotlib.pyplot as plt
# Creating Dataframe from Files
insurance_df = pd.read_csv(filepath_or_buffer='~/Downloads/insurance.csv',
                      sep=',',
                      header=0)

#Create a directory to keep all of the plots
os.makedirs('plots', exist_ok=True)

# Plotting line chart
plt.plot(insurance_df['charges'], color='red')
plt.title('charges by Index')
plt.xlabel('Index')
plt.ylabel('charges')
plt.savefig(f'plots/charges_by_index_plot.png', format='png')
plt.clf()

# Plotting histogram
plt.hist(insurance_df['bmi'], bins=3, color='g')
plt.title('bmi')
plt.xlabel('bmi')
plt.ylabel('Count')
plt.savefig(f'plots/bmi_hist.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(insurance_df['charges'], insurance_df['age'], color='b')
plt.title('charges to age')
plt.xlabel('charges')
plt.ylabel('age')
plt.savefig(f'plots/charges_to_age.png', format='png')

plt.scatter(insurance_df['charges'], insurance_df['bmi'], color='r')
plt.title('charges to bmi')
plt.xlabel('charges')
plt.ylabel('bmi')
plt.savefig(f'plots/charges_to_bmi.png', format='png')
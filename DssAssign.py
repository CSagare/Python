# Check the basic information about the dataframe
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a pandas dataframe
# df = pd.read_csv('customer_delinquency_data.csv')
df = pd.read_csv('Delinquent_customer.csv')


df.info()

# Create a box plot of the age column
sns.boxplot(x='TARGET_LABEL', y='AGE', data=df)
plt.title('Distribution of Age by Delinquency Status')
plt.xlabel('Delinquent (1) / Non-delinquent (0)')
plt.ylabel('Age')
plt.show()

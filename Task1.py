import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic Dataset
df = sns.load_dataset("titanic")

# Print first 5 rows
print(df.head())

# Gender Distribution Bar Chart
plt.figure(figsize=(6,4))
sns.countplot(x="sex", data=df)
plt.title("Gender Distribution in Titanic Dataset")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()
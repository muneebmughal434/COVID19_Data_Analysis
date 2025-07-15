import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
df = pd.read_csv(url)
df = df[df['location'] == 'United States']

sns.lineplot(data=df, x='date', y='new_cases')
plt.title('COVID-19 Daily New Cases in the US')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
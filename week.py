import pandas as pd
import matplotlib.pyplot as plt

def business_problem(_topic):
    raw_df = pd.read_csv('vg_sales.csv')
    publisher_df = raw_df.groupby([_topic])[['Global_Sales', 'JP_Sales']].sum().reset_index()
    publisher_df = publisher_df.sort_values('Global_Sales', ascending=False)
    return publisher_df

year_analysis = business_problem('Year')

year_analysis = year_analysis.sort_values(['Year'])
fig, ax = plt.subplots()
ax.plot(year_analysis['Year'].values, year_analysis['Global_Sales'].values)
plt.show()
plt.savefig('test.png')

#this is a test
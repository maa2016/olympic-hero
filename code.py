# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)
#print(data)
data.rename(columns = {'Total':'Total_Medals'}, inplace = 'True')
data.head(10)


#Code starts here



# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'],'Summer',np.where(data['Total_Summer'] == data['Total_Winter'],'Both','Winter'))
better_event = data['Better_Event'].value_counts().index.tolist()[0]


# --------------
#Code starts here
top_countries = data.loc[:,['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
#top_countries.drop(top_countries.index[-1], inplace=True)
top_countries = top_countries.iloc[0:-1]

def top_ten(df,column):
    return df.nlargest(10,str(column))['Country_Name']

top_10_summer = list(top_ten(top_countries,'Total_Summer'))
top_10_winter = list(top_ten(top_countries,'Total_Winter'))
top_10 = list(top_ten(top_countries,'Total_Medals'))

common = []
for x in top_10_summer:
    if x in top_10_winter and x in top_10:
        print(x)
        common.append(x)


# --------------
#Code starts here
def return_subset_dataframe(data,from_list):
    return data[data['Country_Name'].isin(from_list)]

summer_df = return_subset_dataframe(data,top_10_summer)

winter_df = return_subset_dataframe(data,top_10_winter)

top_df = return_subset_dataframe(data,top_10)

plt.bar(np.arange(len(summer_df['Country_Name'])), summer_df['Total_Summer'], align='center', alpha=0.8)
plt.xticks(np.arange(len(summer_df['Country_Name'])), summer_df['Country_Name'], rotation=45)
plt.xlabel('Country')
plt.ylabel('Summer Medals')

plt.bar(np.arange(len(winter_df['Country_Name'])), winter_df['Total_Winter'], align = 'center', alpha=0.8)
plt.xticks(np.arange(len(winter_df['Country_Name'])), winter_df['Country_Name'], rotation=45)
plt.xlabel('Country')
plt.ylabel('Winter Medals')

plt.bar(np.arange(len(top_df['Country_Name'])), top_df['Total_Medals'], align='center', alpha=0.8)
plt.xticks(np.arange(len(top_df['Country_Name'])), top_df['Country_Name'], rotation=45)
plt.xlabel('Country')
plt.ylabel('Total Medals')

plt.show()


# --------------

summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df[summer_df['Golden_Ratio']==summer_df['Golden_Ratio'].max()].iloc[0,0]

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df[winter_df['Golden_Ratio']==winter_df['Golden_Ratio'].max()].iloc[0,0]

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df[top_df['Golden_Ratio']==top_df['Golden_Ratio'].max()].iloc[0,0]


# --------------
#Code starts here
data_1 = data.drop(data.index[-1])
data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1
most_points = data_1['Total_Points'].max()
best_country = data_1[data_1['Total_Points']==data_1['Total_Points'].max()].iloc[0,0]


# --------------
#Code starts here
best = data[data['Country_Name']==best_country]
best = best[['Gold_Total', 'Silver_Total', 'Bronze_Total']]
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)



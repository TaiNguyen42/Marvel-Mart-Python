#!/usr/bin/env python
# coding: utf-8

# # Python Project - Marvel Mart Project
# # Tai Nguyen
# # 03/15/2023

# # Part 1: Cleaning the data
# 

# In[49]:


import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import seaborn as sns
sns.set(style='ticks', palette='Set2')
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Checking for Missing data / Finding Missing Data

# In[50]:


mm = pd.read_csv('Data/MM_SalesRawData.csv')
print(mm.shape)
print(mm.count())
#This step help me to know what data is missing, then we need to fix all of this


# In[51]:


#Check for MISSING DATA in each individual column
sumNA = mm.isna().sum()
print(sumNA)


# In[52]:


#Copy of our DataFrame for clean Data
mmClean = mm.copy()


# In[53]:


display(mm.head())
print(mm.dtypes)
#This help to display type of each column in csv file
print('\n')

print(type(mm['Region']))
print(type(mm['Country']))
print(type(mm['Item Type']))
print(type(mm['Sales Channel']))


# ## We need to focus on cleaning Data for columns: Country, Item Type, Order Priority, Order ID

# ### Testing the Erronous data in "Country" Column and Fix it

# In[7]:


print(mmClean.shape)
print(mmClean.count())

# From this, we know that in 'Country' column is not missing any data. So, the problems is we need to get rid of the 'Number as a String'
# Also, this is the output before cleaning the data


# In[8]:


count = 0
print('\nTesting erronous data in Country')
for index, row in mmClean.iterrows():
    try:
        # try to convert the type of data from string to float. Obviously, the type of data in this column suppose cannot convert to float. 
        # However, I know that there are some 'Number as string' as dirty data that can be converted to float. if they can convert, we can get it out and replace them to 'NULL'
        row.loc['Country'] = float(row.loc['Country'])
        print(mmClean.loc[int(index), 'Country'])
        mmClean.loc[int(index), 'Country'] = 'NULL'
        # This is the code to change the dirty data to 'NULL'
        print('After cleaned')
        print(mmClean.loc[int(index), 'Country'])
        count+=1
    except:
        if mmClean.loc[int(index), 'Country'] == 'NULL':
            count+=1
        pass
print(f'Number of erronous Country {count}')

#This output is belonged to the FIRST time I run the code above.


# In[9]:


count = 0
print('\nTesting erronous data in Country')
for index, row in mmClean.iterrows():
    try:
        row.loc['Country'] = float(row.loc['Country'])
        print(mmClean.loc[int(index), 'Country'])
        mmClean.loc[int(index), 'Country'] = 'NULL'
        print('After cleaned')
        print(mmClean.loc[int(index), 'Country'])
        count+=1
    except:
        if mmClean.loc[int(index), 'Country'] == 'NULL':
            count+=1
        pass
print(f'Number of erronous Country {count}')

# This output is belonged to the SECOND time I run the code 
## Notice: This code is the SAME of the one ABOVE


# In[10]:


mmClean = mmClean[mmClean['Country'] != 'NULL']
# this code filters the mmClean dataframe to remove any rows where the 'Country' column has a value of 'NULL'. 
## The resulting dataframe contains only the rows where the 'Country' column has a valid value.


# In[11]:


count = 0
print('\nTesting erronous data in Country')
for index, row in mmClean.iterrows():
    try:
        row.loc['Country'] = float(row.loc['Country'])
        print(mmClean.loc[int(index), 'Country'])
        mmClean.loc[int(index), 'Country'] = 'NULL'
        print('After cleaned')
        print(mmClean.loc[int(index), 'Country'])
        count+=1
    except:
        if mmClean.loc[int(index), 'Country'] == 'NULL':
            count+=1
        pass
print(f'Number of erronous Country {count}')
print(mmClean.shape)
print(mmClean.count())

#This is the output of the amount of data that is not 'NULL' after we clean the data
## This output is belonged to the THIRD time I run the code above 
### Notice: This code is the SAME of the one ABOVE
#### However: The output was affected by the code above -----> {mmClean = mmClean[mmClean['Country'] != 'NULL']} ---> It makes the 'NULL' data disappear.


# ### Testing the Erroneous data in "Item Type" Column and Fix it
# 

# In[12]:


# In the previous code, we know that there are some missing data in the 'Item Type' column. Now all we need to do is replacing the missing items to 'NULL'
## I just realized that there are some invalid items: nan
### Number of missing data: 6


# In[13]:


print(mmClean.shape)
print(mmClean.count())

# From this, we noticed that 'Item Type' column is missing 6 data. All we need to do is replacing these data to 'NULL'


# In[14]:


count = 0
print('\nTesting erronous data in Item Type')
for index, row in mmClean.iterrows():
    # this code is checking for missing data in the 'Item Type' column of the 'mmClean' dataframe, and replacing any missing values with the string 'NULL'.
    if pd.isna(row.loc['Item Type']):
        print(f"Missing data in Item Type at index {index}")
        mmClean.loc[int(index), 'Item Type'] = 'NULL'
    try:
        row.loc['Item Type'] = float(row.loc['Item Type'])
        # When you attempt to convert 'nan' to a float using the float() function, a ValueError exception is raised, because 'nan' is not a valid numeric value that can be represented as a float.
        print(mmClean.loc[int(index), 'Item Type'])
        mmClean.loc[int(index), 'Item Type'] = 'NULL'
        print('After cleaned')
        print(mmClean.loc[int(index), 'Item Type'])
        count+=1
    except:
        if mmClean.loc[int(index), 'Item Type'] == 'NULL':
            count+=1
        
        pass
print(f'Number of invalid Item Type that changed to NULL: {count}')

# This is the very first code that can show the result belowed. After I run this again "in the next code" these result will be changed.
## 'nan' stands for 'Not A Number' and is one of the common ways to represent the missing value in the data. 
### It is a special floating-point value and cannot be converted to any other type than float. NaN value is one of the major problems in Data Analysis.


# In[15]:


count = 0
print('\nTesting erronous data in Item Type')
for index, row in mmClean.iterrows():
    # this code is checking for missing data in the 'Item Type' column of the 'mmClean' dataframe, and replacing any missing values with the string 'NULL'.
    if pd.isna(row.loc['Item Type']):
        print(f"Missing data in Item Type at index {index}")
        mmClean.loc[int(index), 'Item Type'] = 'NULL'
    try:
        row.loc['Item Type'] = float(row.loc['Item Type'])
        # try to convert the data from string to float, if cannot then it is bad
        print(mmClean.loc[int(index), 'Item Type'])
        mmClean.loc[int(index), 'Item Type'] = 'NULL'
        print('After cleaned')
        print(mmClean.loc[int(index), 'Item Type'])
        count+=1
    except:
        if mmClean.loc[int(index), 'Item Type'] == 'NULL':
            count+=1
        
        pass
print(f'Number of invalid Item Type that changed to NULL: {count}')

# This output is belonged to the SECOND time I run the code 
## Notice: this code is the same the one above


# In[16]:


mmClean = mmClean[mmClean['Item Type'] != 'NULL']
# this code filters the mmClean dataframe to remove any rows where the 'Item Type' column has a value of 'NULL'. 
## The resulting dataframe contains only the rows where the 'Item Type' column has a valid value.


# In[17]:


count = 0
print('\nTesting erronous data in Item Type')
for index, row in mmClean.iterrows():
    if pd.isna(row.loc['Item Type']):
        print(f"Missing data in Item Type at index {index}")
        mmClean.loc[int(index), 'Item Type'] = 'NULL'
    try:
        row.loc['Item Type'] = float(row.loc['Item Type'])
        # try to convert the data from string to float, if cannot
        print(mmClean.loc[int(index), 'Item Type'])
        mmClean.loc[int(index), 'Item Type'] = 'NULL'
        print('After cleaned')
        print(mmClean.loc[int(index), 'Item Type'])
        count+=1
    except:
        if mmClean.loc[int(index), 'Item Type'] == 'NULL':
            count+=1
        pass
print(f'Number of invalid Item Type that changed to NULL: {count}')
print(mmClean.shape)
print(mmClean.count())


#This is the output of the amount of data that is not 'NULL' after we clean the data
# This output is belonged to the THIRD time I run the code above 
## Notice: This code is the SAME of the one ABOVE
### However: The output was affected by the code  -----> {mmClean = mmClean[mmClean['Item Type'] != 'NULL']}


# In[18]:


print(mmClean['Item Type'].head(15))
#the index[11] was contained 'NULL' value, then when I ran the code  {mmClean = mmClean[mmClean['Item Type'] != 'NULL']},   its gone - the whole row


# ### Testing the Erronous data in "Order Priority" Column and Fix it
# 

# In[19]:


# For this "Order Priority" column, it either MISSING DATA or VALID Priority code: 'C' , 'H' , 'M' , 'L' or if out of these 4 codes, we need to replace it to 'NULL'


# In[20]:


print(mmClean.shape)
print(mmClean.count())

# From this, we know that in 'Order Priority' is missing 15 Data (49994 - 49979), so there should have 15 'NULL' value
# Also, this is the output before cleaning the data


# In[21]:


print('\nTesting the erronous data in Order Priority')
count = 0
for index, row in mmClean.iterrows():
    if pd.isna(row.loc['Order Priority']):
        # this code is checking for missing data in the 'Item Type' column of the 'mmClean' dataframe, and replacing any missing values with the string 'NULL'.

        print(f"Missing data in Order Priority at index {index}")
    try:
        # try to convert each Order Priority to a float, if it succeeds, its bad        
        row.loc['Order Priority'] = float(row.loc['Order Priority'])
        print(mmClean.loc[int(index), 'Order Priority'])
        mmClean.loc[int(index), 'Order Priority'] = "NULL"
        print('After cleaned')
        print(mmClean.loc[int(index), 'Order Priority'])   # print to verify changes
        count+=1
    except:
        if row.loc['Order Priority'] != 'C' and row.loc['Order Priority'] != 'H' and row.loc['Order Priority'] != 'M' and row.loc['Order Priority'] != 'L':
            mmClean.loc[int(index), 'Order Priority'] = "NULL"
            print(mmClean.loc[int(index), 'Order Priority'])   # print to verify changes
            count+=1

print(f"Number of erronous Order Priority {count}")
#This output is belonged to the FIRST time I run the code above


# In[22]:


print('\nTesting the erronous data in Order Priority')
count = 0
for index, row in mmClean.iterrows():
    if pd.isna(row.loc['Order Priority']):
        # this code is checking for missing data in the 'Item Type' column of the 'mmClean' dataframe, and replacing any missing values with the string 'NULL'.

        print(f"Missing data in Order Priority at index {index}")
    try:
        # try to convert each Order Priority to a float, if it succeeds, its bad        
        row.loc['Order Priority'] = float(row.loc['Order Priority'])
        print(mmClean.loc[int(index), 'Order Priority'])
        mmClean.loc[int(index), 'Order Priority'] = "NULL"
        print('After cleaned')
        print(mmClean.loc[int(index), 'Order Priority'])   # print to verify changes
        count+=1
    except:
        if row.loc['Order Priority'] != 'C' and row.loc['Order Priority'] != 'H' and row.loc['Order Priority'] != 'M' and row.loc['Order Priority'] != 'L':
            mmClean.loc[int(index), 'Order Priority'] = "NULL"
            print(mmClean.loc[int(index), 'Order Priority'])   # print to verify changes
            count+=1

print(f"Number of erronous Order Priority {count}")

# This output is belonged to the SECOND time I run the code  
## Notice: This code is the SAME of the one ABOVE


# In[23]:


mmClean = mmClean[mmClean['Order Priority'] != 'NULL']
# this code filters the mmClean dataframe to remove any rows where the 'Order Priority' column has a value of 'NULL'. The resulting dataframe contains only the rows where the 'Order Priority' column has a valid value.


# In[24]:


print('\nTesting the erronous data in Order Priority')
count = 0
for index, row in mmClean.iterrows():
    if pd.isna(row.loc['Order Priority']):
        # this code is checking for missing data in the 'Item Type' column of the 'mmClean' dataframe, and replacing any missing values with the string 'NULL'.

        print(f"Missing data in Order Priority at index {index}")
    try:
        # try to convert each Order Priority to a float, if it succeeds, its bad        
        row.loc['Order Priority'] = float(row.loc['Order Priority'])
        print(mmClean.loc[int(index), 'Order Priority'])
        mmClean.loc[int(index), 'Order Priority'] = "NULL"
        print('After cleaned')
        print(mmClean.loc[int(index), 'Order Priority'])   # print to verify changes
        count+=1
    except:
        if row.loc['Order Priority'] != 'C' and row.loc['Order Priority'] != 'H' and row.loc['Order Priority'] != 'M' and row.loc['Order Priority'] != 'L':
            mmClean.loc[int(index), 'Order Priority'] = "NULL"
            print(mmClean.loc[int(index), 'Order Priority'])   # print to verify changes
            count+=1

print(f"Number of erronous Order Priority {count}")

# This output is belonged to the THIRD time I run the code below 
## Notice: This code is the SAME of the one ABOVE
### However: The output was affected by the code BELOW -----> {mmClean = mmClean[mmClean['Order Priority'] != 'NULL']}


# ### Testing the Erronous data in "Order ID" Column and Fix it

# In[25]:


# For this "Order ID" column, it either MISSING DATA or NOT a NUMBER ---> So we need to Replace the Missing data to 'NULL' and also fix the 'Non-numeric character' to 'NULL' as well


# In[26]:


print(mmClean.shape)
print(mmClean.count())

# From this code, we know that the "Order ID" column is not missing any Data. Therefore, the only problem that we need to clean the data for this column is replacing the 'Non-numeric character' to 'NULL'
## Also, this is the output before cleaning the data


# In[27]:


print('\nTesting the erronous data in Order ID')
count = 0
for index, row in mmClean.iterrows():
    try:
        # Try to convert each value in the column to an int. If it fails, it means the value contains non-numeric characters
        int(row['Order ID'])
    except ValueError:
        # If the conversion fails, replace the value with 0
        mmClean.loc[index, 'Order ID'] = 0
        count += 1

print(f"Number of erroneous values found and replaced with 0: {count}")

# In this code, we can see that the 'Non-numeric characters' have been found and replaced to 0 
## This output is belonged to the FIRST time I run the code above


# In[29]:


print('\nTesting the erronous data in Order ID')
count = 0
for index, row in mmClean.iterrows():
    try:
        # Try to convert each value in the column to an int. If it fails, it means the value contains non-numeric characters
        int(row['Order ID'])
    except ValueError:
        # If the conversion fails, replace the value with 0
        mmClean.loc[index, 'Order ID'] = 0
        count += 1

print(f"Number of erroneous values found and replaced with 0: {count}")

# In this code, we can see that the 'Non-numeric characters' have been found and replaced to 0, but the reason that the output showed "Number of erroneous values found and replaced with 0: 0" is because this is the second time that the code ran, and '0' is the number (int)
## This output is belonged to the SECOND time I run the code above


# In[30]:


mmClean = mmClean[mmClean['Order ID'] != 0]
# this code filters the mmClean dataframe to remove any rows where the 'Order ID' column has a value of 0. The resulting dataframe contains only the rows where the 'Order ID' column has a valid value.

print(mmClean.shape)
print(mmClean.count())
# As we can see, I just removed all the 'Order ID' column has a value of 0. The output is the clean data and ready to use


# ## Testing the Data to see if it is clean/ready

# In[31]:


print(mmClean['Country'][mmClean['Country'] == 'NULL'].count())
print(mmClean['Item Type'][mmClean['Item Type'] == 'NULL'].count())
print(mmClean['Order Priority'][mmClean['Order Priority'] == 'NULL'].count())
print(mmClean['Order ID'][mmClean['Order ID'] == 0].count())

# This code test that whether the Country, Item Type, Order Priority, and Order ID still have 'NULL' or '0' inside. 
## If the output is 0, we completely clean the data and ready to move to next step


# ## Rewrite the Clean Data to a new CSV file

# In[48]:


mmClean.to_csv('Data/MM_Sales_clean.csv')
# rewrite to a new CSV file called MM_Sales_clean.csv


# # Part 2: Exploratory Data Analysis with Reports & Visualizations

# ## 1A

# ### Get the top 10 countries we sell the most:

# In[35]:


# We want to know which country we sell the most so we can pick a new location to build a shipping cener 
## Rank the top 10 countries we sell to the most to least along with the number of sales we've had with that country 
### Note: You are getting a "Count of the number of sale transaction" --> Not a Sum of total Sales.


# In[1]:


# NUMBER OF SALES TRANSACTION = COUNT OF THE NUMBER OF SALE TRANSACTION = COUNT THE ORDER ID 
# When I say most sales, talking about the most sales transaction, not the most sales amount. A sales transaction is represented by a row


# In[4]:


# Load the data into a pandas DataFrame
mmCleandata = pd.read_csv('Data/MM_Sales_clean.csv')

# Group the data by country and count the number of sales (Order ID) for each country. 
## A sales transaction is represented by a row. We count how many rows of Order ID of each Country. 
sales_by_country = mmCleandata.groupby('Country')['Order ID'].count().reset_index()

# Sort the data by the number of sales in descending order and select the top 10
## The code: sort_values in this case help us sort the result DataFrame by 'Order ID' column in descending order. 
### And then head(10) help us to get the top 10 country
top_countries = sales_by_country.sort_values('Order ID', ascending=False).head(10)

# Print the top 10 countries and their number of sales
## In this case, the Order ID represent for the Number of Sales Transaction for each Country.
print(top_countries[['Country', 'Order ID']])


# ### Use Matplotlib to create a chart to show these top 10 values by Country:

# In[5]:


# This line of code sets the figure size for a Matplotlib plot. 
## The figsize argument is set to (30, 10), which means that the figure will have a width of 30 inches and a height of 10 inches.
plt.figure(figsize=(30,10)) 

# set the Title of the bar chart as: 'Top 10 countries by sales'
plt.title('Top 10 Countries by Sales')

# this code is use for create a bar chart with the data from 'top_countries' from the code above
plt.bar(top_countries['Country'], top_countries['Order ID'])

# This assigned the x-axis label as 'Country'
plt.xlabel('Country')

# This assigned the y-axis label as 'Number of Sales'
plt.ylabel('Number of Sales')

# Show/print the bar chart
plt.show()


# ## 1B Answer the question by writing the results to a text file called MM_Rankings.txt

# In[6]:


# We have shipping centers in Trinidad and Tobago, Guinea, and Maldives right now. Which country should we build a shipping center in based on most sales and lack of shipping center?


# In[7]:


print(top_countries)


# In[31]:


# create a string
ct = ['Countries Most Sale Transaction:\n']

# Process the data to create a list of output lines
textfiles = []
for index, row in top_countries.iterrows():
    Country = row['Country']
    Order_ID = row['Order ID']
    textfile = f'{Country}: {Order_ID}\n'
    textfiles.append(textfile)
    
    # concatenate the lists with the additional line
    mmr = ct + textfiles
    
    # '.iloc' is the code that help to get the data from the Data Frame by integer location
    ## It allows you to select data based on its numerical position in the DataFrame or Series, rather than by label.
    ### in this code, {top_countries.iloc[2]["Country"]} means that get the data from DataFrame: top_countries, with the index in the 2nd row in the 'Country' column
    #### also, {top_countries.iloc[2]["Order ID"]} means that get the data from DataFrame: top_countries, with the index in the 2nd row in the 'Order ID' column
    mmr.append(f'The country we should build our shipping center is {top_countries.iloc[2]["Country"]} because it has {top_countries.iloc[2]["Order ID"]} sales and is in the top 3 of the most sale countries\n')
    
# Write the output lines to a text file
with open('Data/MM_Ranking.txt', 'w+') as text:
    text.writelines(mmr)


# ## 2A: Determine the count for how many online and offline orders we take

# In[32]:


# Load the data into a pandas DataFrame
mmCleandata = pd.read_csv('Data/MM_Sales_clean.csv')

# Group the data by Sales Channel and count the number of sales (Order ID) for each Sales Channel (Online and Offline). 
## A sales transaction is represented by a row. Basically, in this code, we groupby the online and offline order type in 'Sale Channel' column
### Then, each order type (online and offline) has multiple different order ID. So, after we groupby the online and offline order type, then we count sales transactions belonged to that order type 
oline_offline_order = mmCleandata.groupby('Sales Channel')['Order ID'].count().reset_index()

# The code: 'sort_values' in this case help us sort the result DataFrame by 'Order ID' column in descending order.
top_sales = oline_offline_order.sort_values('Order ID', ascending=False)

print(top_sales)


# ## 2B: Determine the count of the different Order Priority types

# In[33]:


# Load the data into a pandas DataFrame
mmCleandata = pd.read_csv('Data/MM_Sales_clean.csv')

# Group the data by Order Priority type and count the number of sales/transactions (Order ID) for each Order Priority (C,H,L,M). 
## A sales transaction is represented by a row. Basically, in this code, we groupby the Order Priority type in 'Order Priority' column
### Then, each Order Priority type (C,H,L,M) has multiple different order ID. So, after we groupby the Order Priority type, then we count sales transactions belonged to that type 
order_priority_type = mmCleandata.groupby('Order Priority')['Order ID'].count().reset_index()

# The code: sort_values in this case help us sort the result DataFrame by 'Order ID' column in descending order.
top_order_priority = order_priority_type.sort_values('Order ID', ascending=False)

print(top_order_priority)


# ## 2C: Create a pie chart for 2A and 2B

# ### 2A: Pie Chart

# In[11]:


print(top_sales)


# In[34]:


# plt.figure(figsize=(5,5)) creates a new figure with a specified size of (5,5) inches. 
## The figsize parameter is a tuple that specifies the width and height of the figure in inches. In this case, the figure will be 5 inches wide and 5 inches tall.
plt.figure(figsize=(5,5))

# create a pie chart from 'oline_offline_order' DataFrame
plt.pie(top_sales['Order ID'], 
        labels = top_sales['Sales Channel'], 
        autopct='%1.1f%%', startangle = 90)
# 'autopct' is a parameter in the 'plt.pie()' function in Matplotlib that is used to format the text inside each wedge of the pie chart to display 
## the percentage or numerical value of each category in the chart. In the code autopct='%1.1f%%', the %1.1f format string specifies that the 
### text inside each wedge should be displayed as a floating-point number with one decimal place, while the %% specifies that a percentage sign should be added at the end of each value.
#The startangle parameter is defined with an angle in degrees, default angle is 0, and in this case, we want it to be 90 degree

#The plt.axis('equal') function is typically used after creating a pie chart using the plt.pie() function to ensure that the chart is circular and has an equal aspect ratio. 
plt.axis('equal')

# plt.legend() is a Matplotlib function that adds a legend to a chart, identifying the elements of the chart and their corresponding labels.
## In this code, loc = 1 specifies the location of the legend in the plot. The value 1 corresponds to the upper-left corner of the plot
### title is the tile of this pie chart
plt.legend(loc = 2, title = 'Sales by channel')

# plt.show() is a Matplotlib function to show the plot that has been created.
plt.show()


# ### 2B: Pie Chart

# In[13]:


print(top_order_priority)


# In[14]:


# plt.figure(figsize=(8,8)) creates a new figure with a specified size of (8,8) inches. 
## The figsize parameter is a tuple that specifies the width and height of the figure in inches. In this case, the figure will be 8 inches wide and 8 inches tall.
plt.figure(figsize=(7,7))

# create a pie chart from 'order_priority_type' DataFrame
plt.pie(top_order_priority['Order ID'], 
        labels = top_order_priority['Order Priority'], 
        autopct='%1.1f%%', startangle = 90)
# 'autopct' is a parameter in the 'plt.pie()' function in Matplotlib that is used to format the text inside each wedge of the pie chart to display 
## the percentage or numerical value of each category in the chart. In the code autopct='%1.1f%%', the %1.1f format string specifies that the 
### text inside each wedge should be displayed as a floating-point number with one decimal place, while the %% specifies that a percentage sign should be added at the end of each value.
#The startangle parameter is defined with an angle in degrees, default angle is 0, and in this case, we want it to be 90 degree

#The plt.axis('equal') function is typically used after creating a pie chart using the plt.pie() function to ensure that the chart is circular and has an equal aspect ratio. 
plt.axis('equal')

# plt.legend() is a Matplotlib function that adds a legend to a chart, identifying the elements of the chart and their corresponding labels.
## In this code, loc = 1 specifies the location of the legend in the plot. The value 1 corresponds to the upper-left corner of the plot
### title is the tile of this pie chart
plt.legend(loc = 2, title = 'Sales by Order Priority Type')

# plt.show() is a Matplotlib function to show the plot that has been created.
plt.show()


# ## 2D: Add the results of the sales channel types and the order priorities to the file MM_Rankings.txt.

# ### Sale Channels:

# In[15]:


print(top_sales)


# In[35]:


# create a string
sc = ['\nSales Channel:\n']

# Process the data to create a list of output lines
textfiles2 = []
for index, row in top_sales.iterrows():
    Sales_Channel = row['Sales Channel']
    Order_ID = row['Order ID']
    textfile2 = f'{Sales_Channel}: {Order_ID}\n'
    textfiles2.append(textfile2)
    
    # concatenate the lists with the additional line
    mmr2 = sc + textfiles2
    
    # '.iloc' is the code that help to get the data from the Data Frame by integer location
    ## It allows you to select data based on its numerical position in the DataFrame or Series, rather than by label.
    ### in this code, {top_sales.iloc[0]["Sales Channel"]} means that get the data from DataFrame: top_sales, with the index in the 1st row in the 'Sales Channel' column
    mmr2.append(f'We do more {top_sales.iloc[0]["Sales Channel"]} sales\n')
    
# Write the output lines to a text file
with open('Data/MM_Ranking.txt', 'a') as text:
    text.writelines(mmr2)    


# ### Order Priorities:

# In[17]:


print(top_order_priority)


# In[36]:


# create a string
od = ['\nOrder Priority:\n']

# Process the data to create a list of output lines
textfiles3 = []
for index, row in top_order_priority.iterrows():
    Order_Priority = row['Order Priority']
    Order_ID = row['Order ID']
    textfile3 = f'{Order_Priority}: {Order_ID}\n'
    textfiles3.append(textfile3)
    
    # concatenate the lists with the additional line
    mmr3 = od + textfiles3
    
    # '.iloc' is the code that help to get the data from the Data Frame by integer location
    ## It allows you to select data based on its numerical position in the DataFrame or Series, rather than by label.
    ### in this code, {top_order_priority.iloc[0]["Order Priority"]} means that get the data from DataFrame: top_order_priority, with the index in the 1st row in the 'Order Priority' column
    mmr3.append(f'We do more {top_order_priority.iloc[0]["Order Priority"]} order priorities\n')

# Write the output lines to a text file
with open('Data/MM_Ranking.txt', 'a') as text:
    text.writelines(mmr3)


# ## 3A: Create a Boxplot using Seaborn showing the Total Profits DISTRIBUTION by Item Type:
# 

# In[19]:


# Create the boxplot using Seaborn
plt.figure(figsize = (20,10))
ax = sns.boxplot(x='Item Type', y='Total Profit', data = mmCleandata)

# Set the title and axis labels
ax.set_title('Total Profits Distribution by Item Type')
ax.set_xlabel('Item Type')
ax.set_ylabel('Total Profit')

# Show the plot
plt.show()


# ## 3B: Use Python to determine the sum of Total Profit by Item Type.

# In[37]:


# Load the data into a pandas DataFrame
mmCleandata = pd.read_csv('Data/MM_Sales_clean.csv')

# Group the data by Item Type and sum the Total Profit for each Item. 
item_type = mmCleandata.groupby('Item Type')['Total Profit'].sum().round(2).reset_index()


# Sort the data by the number of sales in descending order 
## The code: sort_values in this case help us sort the result DataFrame by Sum of 'Total Profit' column in descending order. 
item_type_list = item_type.sort_values('Total Profit', ascending=False)

print(item_type_list[['Item Type', 'Total Profit']])

# about the output:
## 3.638408e+09 = 3.638408 times 10 to the power of 9 = 3.638408 Billion
## 5.352505e+08 = 5.352505 times 10 to the power of 8 = 535,250,500 Million 
## 5.101057e+07 = 5.101057 times 10 to the power of 7 = 51,010,570 Million


# ## 3C: Now create a chart type of your choice (Seaborn or Matplotlib) showing the sums of the different Item Types.

# In[21]:


# This line of code sets the figure size for a Matplotlib plot. 
## The figsize argument is set to (30, 10), which means that the figure will have a width of 30 inches and a height of 10 inches.
plt.figure(figsize=(20,10)) 

# set the Title of the bar chart as: 'Total Profit for each Item Type'
plt.title('Total Profit for each Item Type')

# this code is use for create a bar chart with the data from 'item_type_list' from the code above
plt.bar(item_type_list['Item Type'], item_type_list['Total Profit'])

# This assigned the x-axis label as 'Item Types'
plt.xlabel('Item Types')

# This assigned the y-axis label as 'Total Profit each Item'
plt.ylabel('Total Profit each Item')

# Show/print the bar chart
plt.show()


# ## 3D: Rank the top 3 item types we did the most sales (brought in most profit) in to the least sales. (Use 'Total Profit' to determine this).  Please list the item types and the amount of profit made from sales.

# In[38]:


# Load the data into a pandas DataFrame
mmCleandata = pd.read_csv('Data/MM_Sales_clean.csv')

# Group the data by Item Type and sum the Total Profit for each Item. 
item_type = mmCleandata.groupby('Item Type')['Total Profit'].sum().round(2).reset_index()


# Sort the data by the number of sales in descending order 
## The code: sort_values in this case help us sort the result DataFrame by Sum of 'Total Profit' column in descending order (from the most sales to the least sales)
### And then head(3) help us to get the top 3 Item Type 
item_type_list = item_type.sort_values('Total Profit', ascending=False).head(3)

print(item_type_list[['Item Type', 'Total Profit']])


# ## 3E: Add the results of the top 3 item types to the file MM_Rankings.txt

# In[39]:


# create a string
hsi = ['\nHighest Selling Items:\n']

# Process the data to create a list of output lines
textfiles4 = []
for index, row in item_type_list.iterrows():
    Item_Type = row['Item Type']
    Total_Profit = row['Total Profit']
    textfile4 = f'{Item_Type}: {Total_Profit}\n'
    textfiles4.append(textfile4)
    
    # concatenate the lists with the additional line
    mmr4 = hsi + textfiles4
    
    # '.iloc' is the code that help to get the data from the Data Frame by integer location
    ## It allows you to select data based on its numerical position in the DataFrame or Series, rather than by label.
    ### in this code, {item_type_list.iloc[0]["Item Type"]} means that get the data from DataFrame: item_type_list, with the index in the 1st row in the 'Item Type' column
    mmr4.append(f'We profited from {item_type_list.iloc[0]["Item Type"]} the most\n')

# Write the output lines to a text file
with open('Data/MM_Ranking.txt', 'a') as text:
    text.writelines(mmr4)


# ## 3F: Discuss what is being shown in the boxplots amd do some business analytics around what sort of use this sort of chart might help in making decisions. Are there any unexpected results? Discuss them
# 

# In[25]:


# Create the boxplot using Seaborn
plt.figure(figsize = (20,10))
ax = sns.boxplot(x='Item Type', y='Total Profit', data = mmCleandata)

# Set the title and axis labels
ax.set_title('Total Profits Distribution by Item Type')
ax.set_xlabel('Item Type')
ax.set_ylabel('Total Profit')

# Show the plot
plt.show()


# ### Discuss: 
# #### The Seaborn boxplot shows the distribution of total profits across different item types. Each box represents the interquartile range (IQR) of the data, with the median value shown as a line in the middle of the box. The whiskers extend to the minimum and maximum values within 1.5 times the IQR, and any data points beyond the whiskers are considered outliers and shown as individual points.
# #### This chart can help businesses identify which item types are generating the most profit and whether there are any significant differences in profitability between different item types. It can also help identify potential outliers that may require further investigation.
# #### For instance, suppose a company sees that a particular item type is consistently generating lower profits than other types. In that case, they may want to consider adjusting their pricing strategy or marketing efforts to increase sales for that item type. Alternatively, if the company sees that there are many outliers in the data for a specific item type, they may want to investigate why these outliers are occurring and whether any corrective actions are necessary.

# ### Unexpected result:
# #### There is a box of the 'Fruits item type' that unexpected extremely low. So, as a Business Analytics, I need to either increase the marketing for this this item, or I need to stop selling this type of order in order to reduce the cost for Business/Company.

# ## 4. Please determine the sum, average and maximum values for the 'Units Sold', 'Unit Cost', 'Total Revenue', 'Total Cost' and 'Total Profit'. Please put this in a report

# ### 4 A,B,C. Produce the data above for the sum, average, maximum values of the requested columns. 
# 

# In[40]:


import pandas as pd

# Load the CSV file into a DataFrame
mmCleandata = pd.read_csv('Data/MM_Sales_clean.csv')

# Select the column you want to sum
col_name = ['Units Sold', 'Unit Cost', 'Total Revenue', 'Total Cost', 'Total Profit']
column = mmCleandata[col_name]

# Calculate the sum of each column
total_sum = column.sum()

# Calculate the average of each column
average_column = column.mean()

# Determine the maximum value of each column
maximum_value = column.max()

# Print the result
print(f'The sum of each column is:\n{total_sum}\n')
print(f'The average of each column is:\n{average_column}\n')
print(f'The maximum value of each column is:\n{maximum_value}\n')


# ### 4D: Create two line plots using Seaborn or Matplotlib, one for the sums and one for both the averages and the maximums. DO NOT INCLUDE UNITS SOLD OR UNITS COST. 

# In[27]:


# 'Sums': A list of three numbers representing the sum of each set of numbers.
# 'Average': A list of three numbers representing the average (mean) of each set of numbers.
# 'Maximums': A list of three numbers representing the maximum value in each set of numbers.
stats = {'Sums': [66145004417.17, 46629032915.81, 19515971501.36],
         'Average': [1323667.82, 933121.87, 390545.95],
         'Maximums': [6682031.73, 5249075.04, 1738178.39]}

mmCleandata = pd.DataFrame(stats, index = ['Total Revenue', 'Total Cost', 'Total Profit'])

# plt.figure(figsize=(20,5)) creates a new figure with a specified size of (20,5) inches. 
plt.figure(figsize=(20,5))

# So, the code plt.plot(mmCleandata.index, mmCleandata.Sums) is likely plotting a line graph of the values in the 'Sums' column of mmCleandata over time.
plt.plot(mmCleandata.index, mmCleandata.Sums)

# Set the Title of the chart
plt.title('Sums by Columns')

# create the x-axis label
plt.xlabel('Categories')

# create the y-axis label
plt.ylabel('Amounts')
plt.show()


# In[28]:


# plt.figure(figsize=(20,5)) creates a new figure with a specified size of (20,5) inches. 
plt.figure(figsize=(20,5))

# plotting a line graph of the values in the 'Average' column of mmCleandata over time, with the line labeled as 'Averages'. 
plt.plot(mmCleandata.index, mmCleandata.Average, label= 'Averages')

# plotting a line graph of the values in the 'Maximums' column of mmCleandata over time, with the line labeled as 'Maximums'. 
plt.plot(mmCleandata.index, mmCleandata.Maximums, label= 'Maximums')

# Set the Title of the chart
plt.title('Averages and Maximums by Columns')

# adding a legend to a previously created plot, with the legend being automatically positioned in the most suitable location for the plot.
plt.legend(loc = 'best')

# create the x-axis label
plt.xlabel('Categories')

# create the y-axis label
plt.ylabel('Amounts')
plt.show()


# ### 4E: Now you will save these calculations below to a text file called MM_Calc.txt.

# In[41]:


# save the calculations to a text file called MM_Calc.txt
with open('Data/MM_Calc.txt', 'w') as file:
    file.write(f'Sums:\n{total_sum}\n\n')
    file.write(f'Averages:\n{average_column}\n\n')
    file.write(f'Maximums:\n{maximum_value}\n\n')


# # Part 3: Cross-Reference Statistics 
# 

# In[42]:


import pandas as pd

# Load the input CSV file
region_df = pd.read_csv('Data/MM_Sales_clean.csv')

# Drop duplicate rows in the Region and Country columns
region_df = region_df.drop_duplicates(subset=['Region', 'Country'])

# Get a list of unique regions
regions = region_df['Region'].unique()

# Loop through the unique regions and store the countries for each region in a dictionary
region_country_dict = {}
for region in regions:
    countries = region_df[region_df['Region'] == region]['Country'].unique()
    region_country_dict[region] = countries

# Convert the dictionary to a DataFrame
result_df = pd.DataFrame.from_dict(region_country_dict, orient='index')

# Transpose the DataFrame so that the regions become the columns
result_df = result_df.transpose()

# Write the DataFrame to a new CSV file
result_df.to_csv('Data/Countries_By_Region.csv', index=False)


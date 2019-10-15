import pandas as pd
import numpy as np
import pymysql

# STEP 6
# Q. Now your mysql installation contains BSCY4 database that contains 1 table,
# AVOCADO. Use pymysql module to import contents of the table via pandas.
# A. 
connection = pymysql.connect(host='127.0.0.1', user='root', password ='', db='BSCY4')
df = pd.read_sql('SELECT * FROM AVOCADO', con =connection)
cleanData = df

# STEP 7
# Q. Cleanse the content of the field "region".
cleanData['region'] = df['region'].str.replace(' ','')
cleanData['region'] = df['region'].str.replace('-','')

# Q. What can you say about the regions represented?
# A. 
print(df['region'].unique())
# The regions represented are very poorly categorised. Some values are for states and 
# others are for regions within these states. Therefore there are overlapping values.
# Other values simply indicate direction with no context e.g. 'West'.One uniform 
# naming convention should be implemented.

# Q. How many different regions there are?
# A. 54 regions after cleaning.
print("Total regions after cleaning: ", len(cleanData['region'].unique()))

# Q. Are there problems with this variable, if yes, what are the problems and how many?
# A. Yes.
print(df['region'].unique())
# There are multiple errors in this column:
# (1) 'Baltimore-Washington' should not contain a hyphen.
# (2) ' Denver' should not have a space at the begining 
# (3) ' Denver ' should not have a space at the begining or the end

# STEP 8
# Q. What years are represented?
# A. 2015 2016 2017 2018 are the years represented.
print(df['year'].unique())

# Q. Describe any errors that you see in data.
# A. Some 2017 values are represented as 17, some 2018 values are represented as 18.

# Q. How many rows are affected?
# A. 3208 rows were affected.
error = pd.to_datetime(df['year'], errors='coerce', format='%Y')
print ("Total errors: ", sum(error.isna()))

# Q. Cleanse the content of the field "year".
cleanData['year'] = df['year'].replace(17, 2017)
cleanData['year'] = df['year'].replace(18, 2018)

# '18': '2018'

# STEP 9
# Q. Describe any errors that you see. 
# A. Conventional is present with a capital and with out a capital.
# Because th CSV table contained conventional with no capital I will
# assume that that is correct.

# Q. How many rows are affected? 
# A. 169 rows are effected.
print (len(df['type']) - sum(df['type'] =='conventional'))

# Q. What avocado type are represented?
print (df['type'].unique())
# A. 'conventional' is the only type represented.

# Q. Cleanse the content of the field "type".
cleanData['type'] = df['type'].str.lower()




import pandas as pd;

# STEP 1
# Q. Import	data from "BSCY4.csv".
# A.
df = pd.read_csv('BSCY4.csv')

# STEP 2
# Q. Do all rows follow the same format when it comes to "date"?
# A. 
print(df['Date'].unique())
# No there are three seperate types of data:
# (1) YYYY-MM-DD
# (2) DD-MM-YYYY
# (3) DD/MM

# Q. What formats are there and how many entries per each format?
ymdFormat = pd.to_datetime(df['Date'], errors='coerce', format='%Y-%m-%d')
print ("There is", sum(pd.notna(ymdFormat)), "Values in format of YY-MM-DD")
dmyFormat = pd.to_datetime(df['Date'], errors='coerce', format='%d-%m-%Y')
print ("There is", sum(pd.notna(dmyFormat)), "Values in format of DD-MM-YY")
dmFormat = pd.to_datetime(df['Date'], errors='coerce', format='%d/%m')
print ("There is", sum(pd.notna(dmFormat)), "Values in format of DD/MM")

# Q. Cleanse information in the "date".
# A.
cleanData = df

# Add year to rows missing year
for index, row in cleanData['Date'].items():
  if len(str(row)) == 5:
    row = '{0}/{1}'.format(row, cleanData['year'].at[index])
    row = row[:10]

cleanData['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='%Y-%m-%d')

#STEP 3
# Q. How many genuine categories are present?
# A. 
print(cleanData['type'].unique())
# If we assume that 'organic' and 'Org.' are intended to
# be the same then there are 2 genuine categories.

# Q. Do you see problems with how the categories represented?
# A. Yes. The 'Org.' value throws the data off. The data should 
# be represented in lower case with no abbreviation.

# Q. How many entries have errors? 
# A. 169
print ("Total 'Org.' values: ", sum(df['type'] =='Org.'))

# Q. Cleanse	 the	 data	in	 the	 field	 "type".
# A. 
cleanData['type'] = df['type'].replace({'Org.': 'organic'})

# STEP 4
# Q. How many genuine missing values are there?
# A. There are 20 genuine missing values.
print("Total genuine missing values: ",df['AveragePrice'].isna().sum())

# Q. How many entries have erroneous string-based representation?
# A. There are 30 erroneous string-based representations.
errors = df['AveragePrice'].str.contains(',')
print("Total erroneous strings:", sum(errors == True))

# Q. Cleanse the content of the field "average price".
# A.
cleanData['AveragePrice'] = df['AveragePrice'].str.replace(',', '.')

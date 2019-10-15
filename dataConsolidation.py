import pandas as pd
import numpy as np
import pymysql

# STEP 10
# Q. Perform Visual Inspection of the results of the two previous imports.
# A. 
import sqlData
import csvData
print(sqlData.cleanData)
print(csvData.cleanData)

# Q. Are the two data frames suitable for consolidation? 
# A. The data frames are suitable for condsolidation, however the 
# inconsistencies in the column names must be corrected first.

# Q. What problems do you see? Correct the problems.
# A. There are problems with the colum heading not matching.
# Because 'Total Volume' and 'TotalValue' are homoscedastic we can assume that they are the same.
# The following headings need correcting:
#       CSV Data                SQL Data            Corrcted
#       Total Volume            TotalValue          TotalValue
#       4046                    c4046               4046
#       4225                    c4225               4225
#       4770                    c4770               4770
#       Total Bags              TotalBags           TotalBags
#       Small Bags              SmallBags           SmallBags
#       Large Bags              LargeBags           LargeBags
#       XLarge Bags             XLargeBags          XLargeBags

csvData.cleanData = csvData.cleanData.rename(columns={ "Total Volume": "TotalValue", 
                    "Total Bags": "TotalBags",
                    "Small Bags" : "SmallBags",
                    "Large Bags" : "LargeBags",
                    "XLarge Bags" : "XLargeBags"})

sqlData.cleanData = sqlData.cleanData.rename(columns={ "c4046": "4046", 
                    "c4225": "4225",
                    "c4770" : "4770"})

print(sqlData.cleanData)
print(csvData.cleanData)

# There is also an extra heading on the csv table: 'Unnamed: 0'

# STEP 11
# Q. What method should you use to consolidate the two frames correctly? Perform the consolidation.
# A. An inner join, inner merge or inner concat can be used to consolidate the frames.
# I will us ean inner concat.
consolidated = pd.concat([csvData.cleanData, sqlData.cleanData], sort=True)
print(consolidated)
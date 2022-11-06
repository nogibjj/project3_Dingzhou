import sqlite3
import pandas as pd
conn = sqlite3.connect("covid_data.db")
cursor = conn.cursor()


# ## create new table for covid_data.csv
# table = 'CREATE TABLE covid (date DATE, county TEXT, state TEXT, fips INTEGER, cases INTEGER, deaths INTEGER)'
# cursor = conn.cursor()
# cursor.execute(table)
# conn.commit()
# print('Table created successfully')
# # # load the data into a Pandas DataFrame
# covids = pd.read_csv('covid_data.csv')
# # write the data to a sqlite table
# covids.to_sql('covid', conn, if_exists='append', index = False)


# fetch all rows from cars table
cursor.execute('''SELECT * FROM covid''').fetchall()

# Select first 5 record from the table
query_select = 'SELECT * FROM covid LIMIT 5'
for i in cursor.execute(query_select):
    print(i)

#query 1: select top 3 case covid data
query1 =  """SELECT date,county,cases
           FROM covid
           Order by cases DESC
           LIMIT 3;"""
top_cases = cursor.execute(query1).fetchall()
print("\n Top 3 case covid data:")
for case in top_cases:
    print(case)


#query 2: select top 3 fips covid data
query2 =  """SELECT date,county,fips
           FROM covid
           Order by fips ASC
           LIMIT 3;"""
top_fips = cursor.execute(query2).fetchall()
print("\n Top 3 fips covid data:")
for covid in top_fips:
    print(covid)


#query 3: select top 3 county(in CA) have max total cases
query3 =  """SELECT date,county,SUM(cases) as total
           FROM covid Where state='California'
           Group by county
           Order by total DESC
           LIMIT 3;"""
top_burger = cursor.execute(query3).fetchall()
print("\n Top 3 county:")
for covid in top_burger:
    print(covid)




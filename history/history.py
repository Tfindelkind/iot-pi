import pymssql
from secrets import *
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

 
conn = pymssql.connect(server, user, password, database)
cur = conn.cursor()
cur.execute('SELECT * FROM saving_all')
row = cur.fetchone()  
while row:  
    print(str(row[0]))     
    row = cur.fetchone()  

#Consumption
sql_str = "INSERT INTO dbo.consumption_all_h (total) "+" SELECT * FROM dbo.consumption_all;";    
cur.execute(sql_str)  

sql_str = "INSERT INTO dbo.consumption_year_h (total,year) "+" SELECT * FROM dbo.consumption_year;";    
cur.execute(sql_str)  

sql_str = "INSERT INTO dbo.consumption_month_h (total,year,month) "+" SELECT * FROM dbo.consumption_month;";    
cur.execute(sql_str)  


#Saving
sql_str = "INSERT INTO dbo.saving_all_h (total) "+" SELECT * FROM dbo.saving_all;";    
cur.execute(sql_str)  

sql_str = "INSERT INTO dbo.saving_year_h (total,year) "+" SELECT * FROM dbo.saving_year;";    
cur.execute(sql_str)  

sql_str = "INSERT INTO dbo.saving_month_h (total,year,month) "+" SELECT * FROM dbo.saving_month;";    
cur.execute(sql_str)  


#PowerTOGrid
sql_str = "INSERT INTO dbo.power_to_grid_all_h (total) "+" SELECT * FROM dbo.power_to_grid_all;";    
cur.execute(sql_str)  

sql_str = "INSERT INTO dbo.power_to_grid_year_h (total,year) "+" SELECT * FROM dbo.power_to_grid_year;";    
cur.execute(sql_str)  

sql_str = "INSERT INTO dbo.power_to_grid_month_h (total,year,month) "+" SELECT * FROM dbo.power_to_grid_month;";    
cur.execute(sql_str) 

#Costs
sql_str = "INSERT INTO dbo.costs_all_h (total) "+" SELECT * FROM dbo.costs_all;";    
cur.execute(sql_str)  

sql_str = "INSERT INTO dbo.costs_year_h (total,year) "+" SELECT * FROM dbo.costs_year;";    
cur.execute(sql_str)  

sql_str = "INSERT INTO dbo.costs_month_h (total,year,month) "+" SELECT * FROM dbo.costs_month;";    
cur.execute(sql_str) 

conn.commit()
conn.close()  
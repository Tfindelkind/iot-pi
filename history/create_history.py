import PyMySql 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tfindelkind.database.windows.net' 
database = 'iot-pi' 
user = 'admin' 
password = '2Tausend17!' 
 
conn = pymssql.connect(server, user, password, database)
cur = conn.cursor()
cur.execute('SELECT * FROM saving_all')
row = cursor.fetchone()  
while row:  
    print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]))     
    row = cursor.fetchone()  
conn.close()  
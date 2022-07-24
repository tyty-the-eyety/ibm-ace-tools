#!/usr/bin/env python
import csv
import ibm_db
import ibm_db_dbi
import datetime
import sys
import base64
import configparser

__author__ = "Tyron Esch"

__version__ = "1.0.1"
__maintainer__ = "tyronesch@gmail.com"
__email__ = "tyronesch@gmail.com"
__status__ = "WIP"

#def connect_db(self, dsn, db_nm):

def check_if_table_exists( con, table , schema):
    #check if the table exists 
    table_check = "SELECT count(1) FROM SYSIBM.SYSTABLES WHERE NAME = '" + table + "' AND CREATOR = '"+ schema + "' AND TYPE = 'T' WITH UR "
    stmt = ibm_db.prepare(con,table_check)
    result = ibm_db.execute(stmt)
    result_dict = ibm_db.fetch_assoc(stmt)
    if_exists = result_dict['1']
    return if_exists

def rename_table( con ,pcon, cursor,table , schema, time):
    print('Renaming Table '+ table)
    rename_table = 'RENAME TABLE ' + schema+'.'+table + ' TO ' + table+time.strftime("%Y%m%d%H%M%S") +';'
    cursor.execute(rename_table)
    pcon.commit()
    print('Table Renamed to '+ table+time.strftime("%Y%m%d%H%M%S"))
    
def create_table( con ,pcon, cursor ,table , schema , folder ):
    print('Recreating Table '+ table)
    create_table = open(folder+'/'+table+".sql", "r").read()
    cursor.execute(create_table)
    pcon.commit()
    print('Created Table '+create_table)
    
def populate_table( con ,pcon, cursor ,table , schema , folder):
    print('Populating Table Time '+ table)
    with open(folder+'/'+table+'.csv', 'r') as f:
       rows = csv.reader(f, delimiter=',')
       # get column names from header in first line
       columns = ','.join(next(rows))
       for row in rows:
           # build sql with placeholders for insert
           placeholders = ','.join('?' * len(row))
           #print(placeholders)
           sql = 'insert into {} ({}) values ({});'.format(schema+'.'+table , columns, placeholders)
           
           print('Inserting Data ' + sql , row)
           # execute parameterized database insert
           cursor.execute(sql, row)
           pcon.commit()


def main():
        
    config = configparser.ConfigParser()
    config.read('db_properties.ini')
    
    print ('DataBase and Environmet updating to: ' + sys.argv[1])#DB to connect to 
    print ('Updating Schema: ' + sys.argv[2])# Schema of table
    print ('Updating Table: ' + sys.argv[3])# Table to update
    
    host = config[sys.argv[1]]['host']
    user = config[sys.argv[1]]['user']
    passwd = base64.b64decode((config[sys.argv[1]]['passwd'])).decode('utf-8')
    db = config[sys.argv[1]]['db']
    port = config[sys.argv[1]]['port']
    db_conn = 'DATABASE='+db+';HOSTNAME='+host+';UID='+user+';PWD='+passwd+';PORT='+port+';PROTOCOL=TCPIP;AUTHENTICATION=SERVER;'
    
    conn = ibm_db.connect(db_conn , "", "")
    pconn = ibm_db_dbi.Connection(conn)
    cursor = pconn.cursor()
    
    schema = str(sys.argv[2])
    table = str(sys.argv[3])
    now=datetime.datetime.now()
    print(now)
    
    if_exists = check_if_table_exists(conn , str(sys.argv[3]) , str(sys.argv[2]))
    #Rename the table if it exists
    if if_exists == 1:
       print('Table Exists time to rename!' )
       rename_table( conn ,pconn, cursor , str(sys.argv[3]) ,  str(sys.argv[2]), now)
       
    
    create_table(conn ,pconn, cursor, table , schema , sys.argv[1])
    populate_table(conn ,pconn, cursor, table , schema, sys.argv[1])
    
    r = ibm_db.close(conn)
    print(r)

if __name__ == "__main__":
    main()











    
    

        

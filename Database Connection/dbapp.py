import sqlite3


try:
    dbcon=sqlite3.connect("mydb.db")
    print("Database connected!")
except Exception as e:
    print(e)

# Table Create
tbl_create="create table studinfo(id int primary key, name text, sub text)"
try:
    dbcon.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)

# Insert Data
insert_data="insert into studinfo values(1,'sanket','python'),(2,'ashok','java'),(3,'mitesh','php'),(4,'hitesh','angular')"
try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)


# Update Data
update_data="update studinfo set sub='node' where id=4"
try:
    dbcon.execute(update_data)
    dbcon.commit()
    print("Record Updated!")
except Exception as e:
    print(e)

# Delete Data
delete_data="delete from studinfo where id=4"
try:
    dbcon.execute(delete_data)
    dbcon.commit()
    print("Record Deleted!")
except Exception as e:
    print(e)

# Show Data

cur=dbcon.cursor()
select_data="select * from studinfo"
try:
    cur.execute(select_data)
    #data=cur.fetchall()
    #data=cur.fetchmany(2)
    data=cur.fetchone()
    print(data)
except Exception as e:
    print(e)
    

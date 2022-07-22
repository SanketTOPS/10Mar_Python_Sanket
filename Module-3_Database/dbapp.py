import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='pydb')
    print("Database connected!")
except Exception as e:
    print(e)

# Table Create

cur=dbcon.cursor()

create_tbl="create table tops(id int primary key,fname text,sub text,city text)"
try:
    cur.execute(create_tbl)
    print("Table created...")
except Exception as e:
    print(e)

# Insert Data
insert_data="insert into tops values(1,'sanket','python','rajkot'),(2,'gaurav','php','ahmedabad'),(3,'rahul','java','baroda'),(4,'pritesh','react','surat')"

try:
    cur.execute(insert_data)
    dbcon.commit()
    print("Record inserted...")
except Exception as e:
    print(e)

# Update Data
update_data="update tops set sub='iOS' where id=2"

try:
    cur.execute(update_data)
    dbcon.commit()
    print("Record updated...")
except Exception as e:
    print(e)

# Delete Data
delete_data="delete from tops where id=4"

try:
    cur.execute(delete_data)
    dbcon.commit()
    print("Record deleted...")
except Exception as e:
    print(e)

# Select Data
show_data="select * from tops"

try:
    cur.execute(show_data)
    data=cur.fetchall()
    #data=cur.fetchmany(2)
    #data=cur.fetchone()
    #print(data)
    n=1
    for i in data:
        #print(i[3])
        print(f"Record[{n}] = {i}")
        n+=1

except Exception as e:
    print(e)


    

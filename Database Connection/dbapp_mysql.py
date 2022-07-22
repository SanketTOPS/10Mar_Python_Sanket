import pymysql

#dbcon=pymysql.connect(host='127.0.0.1')
try:
    dbcon=pymysql.connect(host="localhost",user="root",password="",database="testdbapp")
    print("Database connected!")
except Exception as e:
    print(e)


cur=dbcon.cursor()
# Table Create
create_tbl="create table studinfo(id int primary key, name text, sub text, city text)"
try:
    cur.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)

# Insert Data
"""insert_data="insert into studinfo values(1,'sanket','python','rajkot'),(2,'nirav','java','ahmedabad'),(3,'mitesh','php','baroda')"
try:
    cur.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)
"""

# ---------------------------------------------------- #

"""stid=input("Enter ID:")
stnm=input("Enter Name:")
stsub=input("Enter Subject:")
stcity=input("Enter City:")

insert_data=f"insert into studinfo values({stid},'{stnm}','{stsub}','{stcity}')"
try:
    cur.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

# ---------------------------------------------------- #

"""def userinsert():
    stid=input("Enter ID:")
    stnm=input("Enter Name:")
    stsub=input("Enter Subject:")
    stcity=input("Enter City:")

    insert_data=f"insert into studinfo values({stid},'{stnm}','{stsub}','{stcity}')"
    try:
        cur.execute(insert_data)
        dbcon.commit()
        print("Record inserted!")
    except Exception as e:
        print(e)

n=int(input("Enter number of students:"))

for i in range(n):
    userinsert()"""

# ---------------------------------------------------- #

# Update data

"""update_data="update studinfo set sub='web-designing',city='rajkot' where id=107"
try:
    cur.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)
"""

# Delete data
"""delete_data="delete from studinfo where id=4"
try:
    cur.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

# Show Data
select_data="select * from studinfo"
try:
    cur.execute(select_data)
    data=cur.fetchall()
    #data=cur.fetchmany(4)
    #data=cur.fetchone()
    #print(data)

    for i in data:
        #print(i[1:3])
        print(f"Name={i[1]} and Subject={i[2]}")
except Exception as e:
    print(e)

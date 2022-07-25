import mysql.connector as sc
sqlcon=sc.connect(host='localhost',user='root',password='1234',database='pratham')
if sqlcon.is_connected():
    print('sucess\n')
cursor=sqlcon.cursor()

def schoolcreate():
    school="create table school (Name varchar(30),Tally integer)"
    cursor.execute(school)
    sqlcon.commit()
    x=int(input('How many students do you want to add?'))
    for i in range(x):
        name=input('Enter nominee name:')
        t=0
        st="insert into school values('{}',{})".format(name,t)
        cursor.execute(st)
        sqlcon.commit()
    y=input('would you like to view the table?(Yes/No)')
    if y=='Yes':
        display="select * from school"
        cursor.execute(display)
        L=cursor.fetchall()
        for j in L:
            print(j)
            
    return

def sportscreate():
    sports="create table sports (Name varchar(30),Tally integer)"
    cursor.execute(sports)
    sqlcon.commit()
    x=int(input('How many students do you want to add?'))
    for i in range(x):
        name=input('Enter nominee name:')
        t=0
        st="insert into sports values('{}',{})".format(name,t)
        cursor.execute(st)
        sqlcon.commit()
    y=input('would you like to view the table?(Yes/No)')
    if y=='Yes':
        display="select * from sports"
        cursor.execute(display)
        L=cursor.fetchall()
        for j in L:
            print(j)
            
    return

def healthcreate():
    health="create table health (Name varchar(30),Tally integer)"
    cursor.execute(health)
    sqlcon.commit()
    x=int(input('How many students do you want to add?'))
    for i in range(x):
        name=input('Enter nominee name:')
        t=0
        st="insert into health values('{}',{})".format(name,t)
        cursor.execute(st)
        sqlcon.commit()
    y=input('would you like to view the table?(Yes/No)')
    if y=='Yes':
        display="select * from health"
        cursor.execute(display)
        L=cursor.fetchall()
        for j in L:
            print(j)
            
    return

def literarycreate():
    literary="create table literary (Name varchar(30),Tally integer)"
    cursor.execute(literary)
    sqlcon.commit()
    x=int(input('How many students do you want to add?'))
    for i in range(x):
        name=input('Enter nominee name:')
        t=0
        st="insert into literary values('{}',{})".format(name,t)
        cursor.execute(st)
        sqlcon.commit()
    y=input('would you like to view the table?(Yes/No)')
    if y=='Yes':
        display="select * from literary"
        cursor.execute(display)
        L=cursor.fetchall()
        for j in L:
            print(j)
            
    return

def culturalcreate():
    cultural="create table cultural (Name varchar(30),Tally integer)"
    cursor.execute(cultural)
    sqlcon.commit()
    x=int(input('How many students do you want to add?'))
    for i in range(x):
        name=input('Enter nominee name:')
        t=0
        st="insert into cultural values('{}',{})".format(name,t)
        cursor.execute(st)
        sqlcon.commit()
    y=input('would you like to view the table?(Yes/No)')
    if y=='Yes':
        display="select * from cultural"
        cursor.execute(display)
        L=cursor.fetchall()
        for j in L:
            print(j)
            
    return



print('Hello Maam/Sir!\n')
print('1.Add nominations')
print('2.Modify nominations')
print('3.Display results\n')
ch=int(input('Please choose:'))   
print('1.School Captain')
print('2.Sports Captain')
print('3.Health Captain')
print('4.Literary Captain')
print('5.Cultural Captain')

if ch==1:
    while True:
        ch1=int(input('please choose which table :'))
        if ch1==1:
            schoolcreate()        
        if ch1==2:
            sportscreate()
        if ch1==3:
            healthcreate()
        if ch1==4:
            literarycreate()
        if ch1==5:
            culturalcreate()
        ch2=input('Would you like to add more tables?(yes/no)')
        if ch2=='yes':
            continue
        else:
            break
            
    


        

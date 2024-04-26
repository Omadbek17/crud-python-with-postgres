import psycopg2

host = 'localhost'
user = 'postgres'
password = 'omad2006'
database = 'n42'
port = 5432

conn = psycopg2.connect(host=host, database=database, user=user, password=password, port=port)
cur = conn.cursor()



#Table Create qilish
create_mobile_phones = """
create table if not exists mobile_phones (
id serial primary key,
name varchar(50) default null ,
color varchar(50) default 'white',
price integer default 0
);
"""

cur.execute(create_mobile_phones)
conn.commit()



#Insert qilish yaniy malumot qo'shish
insert_mobile_phones_query = """
insert into mobile_phones(name, color, price)
values('Iphone 15', 'Black', 1200), 
('Samsung S24 Ultra', 'Green', 2100),
('Samsung S23', 'SummitBlue', 1000),
('Redmi', 'Black', 1200)
"""

cur.execute(insert_mobile_phones_query)
conn.commit()



#Tableni drop qilish
# drop_table_query = """
# DROP TABLE IF EXISTS mobile_phones;
# """

# cur.execute(drop_table_query)
# conn.commit()



#Bu datagripdan malumotlarni ko'rish
cur = conn.cursor()
select_mobile_phones = '''
select * from mobile_phones
'''

cur.execute(select_mobile_phones)
for i in cur.fetchall():
    print(i)

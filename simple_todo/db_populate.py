import psycopg2
from factory import Faker
from factory.django import DjangoModelFactory

conn = psycopg2.connect(
    database="simpletodo_database", user="simpletodo_user", password="p5cLW7lvmC5Ep50j", host="postgres", port="5432"
)
print ("Opened database successfully")
cur = conn.cursor()

for i in range(10):
    Id = fake.random_digit_not_null()
    name = fake.name()
    age = fake.random_number(digits=None)
    adress = fake.address()
    salary = fake.random_int(min=0, max=9999)
    cur.execute(
        "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (%s, %s, %s, %s, %s)", (Id, name, age, adress, salary)
    )

conn.commit()
print "Records created successfully"
conn.close()

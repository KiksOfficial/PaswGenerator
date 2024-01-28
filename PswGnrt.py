import secrets
import string
import mysql.connector

def generate_pass(length=12):
    characters = string.ascii_letters + string.punctuation + string.digits
    psw = ''.join(secrets.choice(characters) for i in range (length))
    return psw

print(generate_pass())

Website = input('Website name: ')
user = input('Username: ')

generated = generate_pass()

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='mydb'
)
cursor = mydb.cursor()

formula = 'INSERT INTO kasutajad (website, user_name, pass_word) VALUES (%s, %s, %s)'
idk = (Website, user, generated)

cursor.execute(formula, idk)
mydb.commit()

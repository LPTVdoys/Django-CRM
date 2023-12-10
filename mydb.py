import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'DOOM'

	)

# обьект курсора
cursorObject = dataBase.cursor()

# создание датабазы
cursorObject.execute("CREATE DATABASE clubase")

print("Gotovo ")
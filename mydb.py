# -*- coding: utf-8 -*-

import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Akashmahi@17'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE sampleqa")

print("Database 'sampleqa' created successfully!")

cursorObject.close()
database.close()

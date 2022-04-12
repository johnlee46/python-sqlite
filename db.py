#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
import json

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print ('Database created and Successfully Connected to SQLite')

    sqlite_select_Query = 'select sqlite_version();'
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print ('SQLite Database Version is: ', record)
    cursor.close()
    jsonFile = open('data.json')
    data = json.load(jsonFile)
    c = sqliteConnection.cursor()
    c.execute('CREATE TABLE trees (recordid varchar(50), data json)')
	console.log(data)
    for tree in data:
        c.execute('insert into trees values (?, ?)', [tree['recordid'],
                  json.dumps(tree)])
        sqliteConnection.commit()
except sqlite3.Error as error:
    print (error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print ('The SQLite connection is closed')

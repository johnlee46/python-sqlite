#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
import json

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print('Database created and Successfully Connected to SQLite')
    sqlite_select_Query = 'select * from trees where TREE_ID = 118157'
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print(record)
    cursor.close()
except sqlite3.Error as error:
    print(error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('The SQLite connection is closed')

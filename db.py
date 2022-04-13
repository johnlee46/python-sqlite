#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
import pandas as pd

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    print('Database created and Successfully Connected to SQLite')
    trees = pd.read_excel(
        'data.xlsx',
        sheet_name='Sheet',
        header=0)
    # if_exists can be changed to append or replace, append just keeps adding the same lines in
    trees.to_sql('trees', sqliteConnection, if_exists='replace', index=False)
except sqlite3.Error as error:
    print(error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('The SQLite connection is closed')

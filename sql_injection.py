#!/usr/bin/env python

import sqlite3
import sys

def main(arg):
    conn = sqlite3.connect(':memory:')

    conn.execute('''
    CREATE TABLE USERS (
        ID INT PRIMARY KEY NOT NULL,
        EMAIL TEXT NOT NULL,
        PASSWORD INT NOT NULL
    );
    ''')

    conn.execute('''
    INSERT INTO 
        USERS 
    VALUES
        ('1', 'admin@example.org', 'admin123'),
        ('2', 'aepp.r@example.org', 'user456'),
        ('3', 'test@example.org', 'specialsecret')
    ;''')

    sql_command = "SELECT * FROM USERS WHERE EMAIL='{}';".format(arg)
    print("SQL Command to be executed: {}".format(sql_command)) # CWE-134
    cursor = conn.execute(sql_command) # CWE-89

    result_set = cursor.fetchall()

    if len(result_set) > 0:
        for row in result_set:
            print(row)
    else:
        print("No dentries found.")

    conn.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        main(arg)



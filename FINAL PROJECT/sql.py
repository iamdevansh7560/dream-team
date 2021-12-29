import sqlite3
team2=sqlite3.connect("dreamteam.db")

cuur=team2.cursor()
sql= "SELECT name FROM teams;"
cuur.execute(sql)
cur=cuur.fetchone()
print(cur)

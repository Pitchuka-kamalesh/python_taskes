import cx_Oracle

# Connect string format: [username]/[password]@//[hostname]:[port]/[DB service name]
conn = cx_Oracle.connect("system/kamal@//localhost:1521/XEPDB1")
cur = conn.cursor()
cur.execute("SELECT 'Hello World!' FROM dual")26
res = cur.fetchall()
print(res)
cur.close()
conn.close()


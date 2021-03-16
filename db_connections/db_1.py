import cx_Oracle
conn = cx_Oracle.connect("system/kamal@localhost")
print(conn.version)
conn.close()



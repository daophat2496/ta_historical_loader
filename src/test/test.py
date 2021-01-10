import psycopg2 as pgc

file = open("./object_queries/test.sql", "r")
cmd1 = "SELECT count(*) FROM test_cases;"
cmd = file.read()
conn = pgc.connect(database = "qtestprod", user= "postgres", password = "d4wsK5v55okL", host = "useast-qtest-demo.cvesbh2vkyxd.us-east-1.rds.amazonaws.com")
cursor = conn.cursor()
cursor.execute(cmd)
print(cmd)
print(type(cmd))
result = cursor.fetchall()
print(result)
print(type(result))
print(type(result[0]))
cursor.close()
conn.close()

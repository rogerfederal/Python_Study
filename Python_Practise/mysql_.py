import pymysql

conn = pymysql.connect(host='130.49.136.103', port=3306, user='remote', passwd='Zking2001', db='student', charset='utf8')
cursor = conn.cursor()
# for i in range(1,11):
#     cursor.execute("INSERT INTO userinfo(username, passwd) VALUES (\"admin{}\", \"000000\")".format(i));
# cursor.execute("select * from userinfo")
# row_1 = cursor.fetchall()
# print(row_1)
for i in range(1,11):
    cursor.execute("UPDATE userinfo SET passwd = \"666666\" WHERE username = \"admin{}\"".format(i))
    # print("UPDATE userinfo SET passwd = \"666666\" WHERE username = \"admin{}\"".format(i))
conn.commit()
cursor.close()
conn.close()

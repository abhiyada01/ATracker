import sqlite3 as sq

conn = sq.connect('data.db')


# cursor = conn.execute("SELECT * from f1_data")
# for row in cursor:
#     print("Part_name = ", row[0])
#     print("Admin = ", row[1])
#     print("AOI = ", row[2])
#     print("TCL = ", row[3])
#     print("PREWAVE = ", row[4])
#     print("POSTWAVE = ", row[5])
#     print("TESTING = ", row[6])
#     print("COATING = ", row[7], "\n")
#
# print("Operation done successfully")
# conn.close()

def find_all():
    cursor = conn.execute("SELECT * from f1_data")
    aa = [row for row in cursor]
    conn.close()
    return aa

import sqlite3

department = ['国語','数学','理科','社会','英語']
names = ['山本', '常平','平林','都築']
dep = ['kokugo','math','science','social','english']
x = 0

conn = sqlite3.connect("schools.db")
cur = conn.cursor();
cur.execute("CREATE TABLE IF NOT EXISTS scores\
            (id INTEGER  PRIMARY KEY AUTOINCREMENT,\
            name TEXT NOT NULL,\
            kokugo INTEGER NOT NULL,\
            math INTEGER NOT NULL,\
            science INTEGER NOT NULL,\
            social INTEGER NOT NULL,\
            english INTEGER NOT NULL)")

def student():
    for name in names:
        print(name)
        kokugo = int(input(department[0] + ":"))
        sugaku = int(input(department[1] + ":"))
        rica = int(input(department[2] + ":"))
        shakai = int(input(department[3] + ":"))
        eig = int(input(department[4] + ":"))
        cur.execute("INSERT INTO scores (name, kokugo, math, science, social, english) VAlUES (?, ?, ?, ?, ?, ?)",(names, kokugo,sugaku,rica,shakai,eig))
    conn.commit()


def data():
    z = int(input("どの点数をみますか？ 国語:1 数学:2 理科:3 社会:4 英語5"))
    '''
    if (z == 1):
        v = "kokugo"
    elif(z == 2):
        v = "math"
    elif (z == 3):
        v = "science"
    elif(z == 4):
        v = "social"
    elif (z == 5):
        v = "english"
    '''
    v = dep[z - 1]

    cur.execute(f"SELECT name, {v} FROM scores")
    for row in cur.fetchall():
        print(row)

def total():
    '''
    cur.execute("SELECT SUM(kokugo) FROM scores")
    kokt = cur.fetchone()[0]
    cur.execute("SELECT AVG(kokugo) FROM scores")
    koka = cur.fetchone()[0]
    print("国語 合計:" + str(kokt) + "平均:" + str(koka))
    '''
    count = 0
    total = 0
    while count < len(department):
        cur.execute(f"SELECT SUM({dep[count]}) FROM scores")
        to = cur.fetchone()[0]
        cur.execute(f"SELECT AVG({dep[count]}) FROM scores")
        oka = cur.fetchone()[0]
        print(f"{department[count]} 合計: {to} 平均: {oka}")
        total += to
        count += 1
    print(f"合計: {total}")
    while():
        cur.execute(f"SELECT name, kokugo + math + science + social + english AS totals FROM scores")
        rows = cur.fetchall()

        for name, total in rows:
            print(f"{name}: 合計 {total}点")

    

y = int(input("何をしますか入力:1 表示:2") )
if y == 1:
    student()
elif y == 2:
    data()
elif y == 3:
    total()
else :
    print("ERROR")

conn.close()

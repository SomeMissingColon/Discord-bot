import sqlite3


def open_db():
    conn = sqlite3.connect('main.db')
    c = conn.cursor()
    return c, conn


def create_table(c):
    c.execute("CREATE TABLE IF NOT EXISTS users (idprofile INTEGER PRIMARY KEY, author TEXT, ign TEXT, tier TEXT, rank TEXT, rvalue INTEGER)")


def dynamic_data_entry(idprofile,author, ign, tier, rank, rvalue, c, conn):
    try:
        c.execute("INSERT INTO users (idprofile,author, ign, tier, rank, rvalue) VALUES (?, ?, ?, ?,?,?)",
                  (idprofile,author, ign, tier, rank, rvalue))

    except sqlite3.IntegrityError:
        c.execute('DELETE FROM users WHERE idprofile =' + str(idprofile))

        c.execute("INSERT INTO users (idprofile,author, ign, tier, rank, rvalue) VALUES (?, ?, ?, ?,?,?)",
                  (idprofile,author, ign, tier, rank, rvalue))
        return 1

    except Exception as e:
        print(e)
        return 0

    conn.commit()
    c.close
    conn.close()


def push_myrank(idprofile,author, ign, tier, rank, rvalue):
    c, conn = open_db()
    create_table(c)
    # ERROR HANDLING#
    if dynamic_data_entry(idprofile,author, ign, tier, rank, rvalue, c, conn) == 1:
        return 1
    if dynamic_data_entry(idprofile,author, ign, tier, rank, rvalue, c, conn) == 0:
        return 0

    dynamic_data_entry(idprofile,author, ign, tier, rank, rvalue, c, conn)


def pull_myrank(idprofile):
    c, conn = open_db()
    idprofile = str(idprofile)
    c.execute("SELECT * FROM users WHERE idprofile=" + idprofile)

    return c.fetchall()


def pull_teamates(r_min,r_max,idprofile):
    c, conn = open_db()
    r_min,r_max,idprofile= str(r_min),str(r_max),str(idprofile)
    c.execute("SELECT * FROM users WHERE rvalue >="+r_min+" AND rvalue <= "+r_max+" AND idprofile != "+idprofile)
    data = c.fetchall()

    return data
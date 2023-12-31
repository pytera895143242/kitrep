import sqlite3

def reg_user(id,full_name):
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sql.execute(""" CREATE TABLE IF NOT EXISTS black_list (
            id BIGINT,
            stat
            ) """)
    db.commit()

    sql.execute(""" CREATE TABLE IF NOT EXISTS user_time (
        id BIGINT,
        prokladka,
        finish_stat,
        full_name
        ) """)
    db.commit()

    sql.execute(f"SELECT id FROM user_time WHERE id ='{id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO user_time VALUES (?,?,?,?)", (id, '1','0', full_name))
        db.commit()

def status_access(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    b = sql.execute(f"SELECT prokladka FROM user_time WHERE id ='{id}'").fetchone()[0]
    return b

def update_status_access(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE user_time SET prokladka = '0' WHERE id = '{id}'")
    db.commit()






def info_members(): # Количество челов, запустивших бота
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    a = sql.execute(f'SELECT COUNT(*) FROM user_time').fetchone()[0]
    b = sql.execute(f'SELECT COUNT(*) FROM user_time WHERE finish_stat = "1"').fetchone()[0]

    return a,b

def change_status(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE user_time SET finish_stat = '1' WHERE id = '{id}'")
    db.commit()


def change_prokladka(id, p):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE user_time SET prokladka = '{p}' WHERE id = '{id}'")
    db.commit()

def add_black(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sql.execute(f"SELECT id FROM black_list WHERE id = '{id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO black_list VALUES (?,?)", (int(id), '0'))
        sql.execute(f"INSERT INTO black_list VALUES (?,?)", (str(id), '0'))
        db.commit()

def cheak_black(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"SELECT id FROM black_list WHERE id = '{id}'")
    if sql.fetchone() is None: #Список пуст, разрешает
        return 0
    else: #Запрещаем
        return 1
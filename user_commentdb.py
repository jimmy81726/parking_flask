import sqlite3


# 建立資料表
def create_commentdb():
    sqlstr = """
    CREATE TABLE IF NOT EXISTS user_comment(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    park_site TEXT,
                    rating INTEGER,
                    comment TEXT,
                    creation_date DATETIME
    )
    """

    conn = sqlite3.connect("comment_db.db")
    cursor = conn.cursor()
    cursor.execute(sqlstr)
    conn.commit()
    conn.close()


# 顯示資料表
def show_comments(park_site=None):
    conn = sqlite3.connect("comment_db.db")
    cursor = conn.cursor()
    # 不同站的評論點進來只顯示那個站的評論,所以帶參數一個回傳以篩選
    if park_site is not None:
        cursor.execute("SELECT * FROM user_comment WHERE park_site = ?", (park_site,))
    else:
        cursor.execute("SELECT * FROM user_comment")
    comments = cursor.fetchall()
    conn.close()
    return comments


# 寫入資料表
def write_db(name, park_site, comment, rating, creation_date):
    conn = sqlite3.connect("comment_db.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO user_comment (name, park_site, comment, rating, creation_date) VALUES (?, ?, ?, ?, ?)",
        (name, park_site, comment, rating, creation_date),
    )

    conn.commit()

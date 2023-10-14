import sqlite3


def create_commentdb():
    sqlstr = """
    CREATE TABLE IF NOT EXISTS user_comment(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    phone TEXT,
                    email TEXT,
                    park_site TEXT,
                    comment TEXT,
                    datacreationdate DATETIME
    )
    """

    conn = sqlite3.connect("comment_db.db")
    cursor = conn.cursor()
    cursor.execute(sqlstr)
    conn.commit()
    conn.close()


def show_comments():
    conn = sqlite3.connect("comment_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_comment")
    comments = cursor.fetchall()
    conn.close()
    return comments


def write_db(name, phone, email, park_site, comment, creation_date):
    conn = sqlite3.connect("comment_db.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO user_comment (name, phone, email, park_site, comment, datacreationdate) VALUES (?, ?, ?, ?, ?, ?)",
        (name, phone, email, park_site, comment, creation_date),
    )

    conn.commit()

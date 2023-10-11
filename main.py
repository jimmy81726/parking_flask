from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

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


@app.route("/")
def index():
    return render_template("./index.html", **locals())


@app.route("/comment", methods=["GET", "POST"])
def get_usercomment():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]
        parking = request.form["parking"]
        comment = request.form["comment"]
        creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 连接到数据库
        conn = sqlite3.connect("comment_db.db")
        cursor = conn.cursor()

        # 插入数据到数据库
        cursor.execute(
            "INSERT INTO user_comment (name, phone, email, park_site, comment, datacreationdate) VALUES (?, ?, ?, ?, ?, ?)",
            (name, phone, email, parking, comment, creation_date),
        )
        conn.commit()
        conn.close()
    return render_template("./comment.html")


if __name__ == "__main__":
    app.run(debug=True)

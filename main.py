from flask import Flask, render_template, request
from datetime import datetime
from user_commentdb import write_db, show_comments, create_commentdb
from parking import get_parkinginfo

app = Flask(__name__)


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
        write_db(name, phone, email, parking, comment, creation_date)
    comments = show_comments()
    return render_template("./comment.html", comments=comments)


@app.route("/parkinginfo", methods=["GET", "POST"])
def show_parkinginfo():
    if request.method == "GET":
        all_values, columns = get_parkinginfo()
    if request.method == "POST":
        all_values, columns = get_parkinginfo()
    return render_template("./parkinginfo.html", **locals())


if __name__ == "__main__":
    create_commentdb()
    app.run(debug=True)

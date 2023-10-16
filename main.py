from flask import Flask, render_template, request
from datetime import datetime
from user_commentdb import write_db, show_comments, create_commentdb
from parking import get_parkinginfo

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("./index.html", **locals())


@app.route("/comment/<string:park_site>", methods=["GET", "POST"])
# 取的評論的資訊回傳給資料庫
def get_usercomment(park_site):
    if request.method == "POST":
        name = request.form["name"]
        comment = request.form["comment"]
        rating = int(request.form["rating"])
        creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 取完馬上寫入資料庫
        write_db(name, park_site, comment, rating, creation_date)
    # 為了讓各別停車位有各別評論,要回傳給show_comments()做處理
    comments = show_comments(park_site)
    all_values, _ = get_parkinginfo()
    return render_template("./comment.html", comments=comments, all_values=all_values)


@app.route("/parkinginfo", methods=["GET", "POST"])
# 取得即時資訊然後回傳給parkinginfo.html頁面來做顯示
def show_parkinginfo():
    if request.method == "GET":
        all_values, columns = get_parkinginfo()
    if request.method == "POST":
        # 將選擇汽車的動作做回傳
        if request.form.get("sort") == "carspace":
            all_values, columns = get_parkinginfo(1)
        # 將選擇機車的動作做回傳
        elif request.form.get("sort") == "motspace":
            all_values, columns = get_parkinginfo(2)
        else:
            all_values, columns = get_parkinginfo()
    return render_template("./parkinginfo.html", **locals())


if __name__ == "__main__":
    create_commentdb()
    app.run(debug=True)

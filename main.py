from flask import Flask, render_template, request, redirect, make_response
import datetime
from orm import model, ormanager
# 创建app
app = Flask(__name__)
# 配置缓存更新时间
app.send_file_max_age_default = datetime.timedelta(seconds=1)
app.debug = True


# 将url和视图函数绑定
@app.route("/")
# 创建视图函数
def index():
    b1 = model.Book(1, "一个叫欧威的男人决定去死", 10)
    b2 = model.Book(2, "局外人", 20)
    b3 = model.Book(3, "了不起的盖茨比", 30)
    # return "<h1>hello world</h1>"
    user = request.cookies.get("name")
    return render_template("index.html", booklist=[b1, b2, b3], userinfo=user)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        # args = request.args
        # print(args.get("name"))
        # print(args.get("value1"))
        print("收到get请求，返回注册页面")
        return render_template("register.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # 将注册信息存入数据库
        ormanager.insertUser(username, password)
        print("收到post请求，可以提取表单参数")
        return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        try:
            # 判断用户名和密码是否输入正确
            if ormanager.checkUser(username, password):
                # 设置响应头
                res = make_response(redirect("/"))
                res.set_cookie("name", username, expires=datetime.datetime.now() + datetime.timedelta(days=7))
                return res
            else:
                return redirect("/login")
        except:
            return redirect("/login")


@app.route("/detail/<info>")
def detail(info):
    return render_template("detail.html")


@app.route("/quit")
def quit():
    # 当点击退出的时候清除cookie
    res = make_response(redirect("/"))
    res.delete_cookie("name")
    return res


if __name__ == "__main__":
    app.run()

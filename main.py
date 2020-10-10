import flask
from flask import session
import time
app = flask.Flask("test", template_folder="C:/Users/pc/PycharmProjects/HTML/")

app.config["SECRET_KEY"] = str(time.time())
# var1 = 0
var = 0

@app.route("/",methods=["GET"], defaults={"page":1})
@app.route("/<int:page>", methods=["GET"])
def rootPage(page):
    return "PAGE:" + str(page)

@app.route("/home",methods=["GET"])
def homePage():
    global session
    if "var" not in session:
        session["var"] = 0
    session["var"] = int(session["var"]) + 1
    return "Hello var1:" + str(session.get("var"))

@app.route("/get",methods=["GET", "POST"])
def getPage():
    print(flask.request.form)
    print("=============================")
    print(flask.request.files["photo"].filename)
    flask.request.files["photo"].save(flask.request.files["photo"].filename)
    print("=============================")
    return "POST"

@app.route("/form",methods=["GET"])
def formPage():
    return flask.render_template("form.html", title="註冊表單")

@app.route("/download",methods=["GET"])
def downloadPage():
    return flask.send_from_directory("C:/Users/pc/PycharmProjects/HTML/", "h3.mp4", as_attachment=True)

@app.route("/google",methods=["GET"])
def googlePage():
    return flask.redirect("https://www.google.com.tw/")

@app.route("/resp",methods=["GET"])
def respPage():
    page = flask.make_response("ABC")
    page.status_code = 500
    return page

app.run(
    host="localhost",
    port=80
)
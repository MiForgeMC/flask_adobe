from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/partners')
def partners():
    return render_template("partners.html")

@app.route('/production/after_effects')
def after_effects():
    return render_template("product1.html")

@app.route('/production/illustrator')
def illustrator():
    return render_template("product2.html")

@app.route('/production/premiere_pro')
def premiere_pro():
    return render_template("product3.html")


@app.route("/data/<string:name>/<int:idd>")
def data(name, idd):
    return f"{name} - {str(idd)}"

if __name__ == "__main__":
    app.run(debug=True)
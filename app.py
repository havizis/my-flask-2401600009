from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

# Untuk menjalankan CSS saat dites secara lokal
@app.route("/style.css")
def style():
    return send_from_directory("public", "style.css")

if __name__ == "__main__":
    app.run(debug=True)
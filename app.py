from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    ssl_context = ("openssl/server.crt", "openssl/private.key")
    app.run(debug=True, ssl_context=ssl_context)

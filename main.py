#! /usr/bin/env python3

from flask import Flask, render_template, request

app = Flask(__name__)
host = "127.0.0.1"
port = 7080
debug = True

@app.route("/", methods=["GET"])
def index():
    return render_template("main.html", message="Welcome to SHARN CTF!", title="Welcome")
@app.route("/secret_route", methods=["GET", "POST"])
def secret_route():
    if request.method == "GET":
        return render_template("main.html", message="You Accessed the Secret Endpoint with GET Request", title="Wrong Request Method")
    elif request.method == "POST":
        browser = str(request.headers.get("User-Agent"))
        if browser != "sharn":
            return render_template("main.html", message=f"You Accessed the Secret Endpoint with POST Request, but your browser was {browser}. We only accept post request from *sharn* browser", title="Browser not Allowed")
        else:
            return render_template("main.html", message="Part 4 of flag => 1_$h0u1d_h@ve_@dded_m0re_he@der$}", title="Browser not Allowed")

if __name__ == "__main__":
    app.run(host=host, port=port, debug=debug)
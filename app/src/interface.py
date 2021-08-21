# import modules and frameworks
import os
import flask
from flask import Flask, render_template, jsonify, request, redirect, url_for
import requests
import find


app = Flask(__name__)

# set debug mode
app.config["DEBUG"] = True

# landing page
@app.route("/", methods=["GET", "POST"])
def home_page():
    return render_template("home_page.html")


# after hitting the search button
@app.route("/search", methods=["POST", "GET"])
def search():
    query = None
    if request.method == "POST":
        query = request.form.get("search_query")
    if query is None:
        code = 400
        r = {
            "message": "Required parameter(query): please enter a valid string to search"
        }
    else:
        code = 200
        perfom = find.perfom_search()
        r = perfom.search(query)
    return {"results": r}


# ping the service
def ping(url):
    try:
        r = requests.get("https://" + url, timeout=5)
        if r.status_code == 200:
            time_lapse = r.elapsed.total_seconds()
        else:
            time_lapse = -1
    except:
        time_lapse = -1

    return time_lapse


# health check...later implement CI/CD
# Do proper health check using docker and kubernetes
@app.route("/health")
def check_health():

    r = {
        "Itunes_response_time": ping(
            "itunes.apple.com/search?term=jack+johnson&limit=5"
        ),
        "Google_response_time": ping(
            "www.googleapis.com/books/v1/volumes?filter=full&maxResults=5&printType=BOOKS&q=Flowers"
        ),
    }
    return {"results": r}


if __name__ == "__main__":
    app.run()
    # HOST = "0.0.0.0"
    # PORT = 80
    # #to connect multiple users, uncomment below
    # app.run(host=HOST, port = PORT, threaded = True)

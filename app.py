from flask import Flask, render_template, request
import requests

app = Flask(__name__)

GIPHY_API_KEY = 'GYTUnE9gh7QPNrlbNi8kEnMnDizZMKyY'

@app.route("/", methods=["GET", "POST"])
def index():
    gifs = []
    if request.method == "POST":
        search_term = request.form.get("query")
        url = f"https://api.giphy.com/v1/gifs/search"
        params = {
            "api_key": GIPHY_API_KEY,
            "q": search_term,
            "limit": 5
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            gifs = [item["images"]["original"]["url"] for item in data["data"]]
    return render_template("index.html", gifs=gifs)

if __name__ == "__main__":
    app.run(debug=True)

# -*- coding: utf-8 -*-
from flask import Flask, jsonify, send_from_directory
import random, datetime, os

app = Flask(__name__, static_folder='../frontend', static_url_path='')

SPORTS = [
    {"sport":"foci","display":"Foci"},
    {"sport":"kosarlabda","display":"Kosárlabda"},
    {"sport":"tenisz","display":"Tenisz"},
    {"sport":"jegkorong","display":"Jégkorong"}
]

def generate_tip_for(sport):
    odds = round(random.uniform(1.80, 2.60),2)
    tip = random.choice(["Hazai","Vendég","Over 2.5","Under 2.5"])
    prob = random.randint(52,84)
    ev = round((prob/100.0)*(odds-1) - (1 - prob/100.0),4)
    return {
        "sport": sport["sport"],
        "display": sport["display"],
        "meccs": f"{sport['display']} – AI választás",
        "odds": odds,
        "prob": f"{prob}%",
        "ev": ev,
        "tipp": tip
    }

@app.route("/api/tips")
def api_tips():
    now = datetime.datetime.now()
    tips = [generate_tip_for(s) for s in SPORTS]
    return jsonify({
        "dátum": now.strftime("%Y-%m-%d %H:%M:%S"),
        "napi_tippek": tips
    })

# Serve frontend files
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

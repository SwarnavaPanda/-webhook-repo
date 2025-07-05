from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv
import pytz

load_dotenv()

app = Flask(__name__)
CORS(app)

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["webhook_db"]
collection = db["events"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    event_type = request.headers.get('X-GitHub-Event')
    payload = request.json

    # Format timestamp in IST
    ist = pytz.timezone('Asia/Kolkata')
    timestamp = datetime.now(ist).strftime("%d %B %Y - %I:%M %p IST")

    entry = {}

    if event_type == "push":
        entry = {
            "request_id": payload.get("after", ""),  # commit SHA
            "author": payload["pusher"]["name"],
            "action_type": "push",
            "from_branch": None,  # not applicable in push
            "to_branch": payload["ref"].split("/")[-1],
            "timestamp": timestamp
        }

    elif event_type == "pull_request":
        pr = payload["pull_request"]
        author = pr["user"]["login"]
        from_branch = pr["head"]["ref"]
        to_branch = pr["base"]["ref"]
        merged = pr.get("merged", False)
        action = payload.get("action")

        if action == "opened":
            entry = {
                "request_id": str(pr["id"]),  # pull request ID
                "author": author,
                "action_type": "pull_request",
                "from_branch": from_branch,
                "to_branch": to_branch,
                "timestamp": timestamp
            }
        elif action == "closed" and merged:
            entry = {
                "request_id": str(pr["id"]),  # same PR ID
                "author": author,
                "action_type": "merge",
                "from_branch": from_branch,
                "to_branch": to_branch,
                "timestamp": timestamp
            }

    if entry:
        collection.insert_one(entry)

    return '', 200

@app.route('/events', methods=['GET'])
def get_events():
    events = list(collection.find({}, {'_id': 0}))
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

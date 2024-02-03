# fallback-solution/app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def fallback_solution():
    return "Work is underway on the site!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
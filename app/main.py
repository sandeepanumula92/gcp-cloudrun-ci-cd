from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        "index.html",
        app_name="Cloud DevOps POC",
        environment=os.getenv("ENV", "dev"),
        region=os.getenv("REGION", "europe-west2"),
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

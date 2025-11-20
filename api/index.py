from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def index():
    html_path = os.path.join(os.path.dirname(__file__),"..", "ensem_marks_estimator_v1.html")

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    return render_template_string(html)

# Vercel handler
handler = app

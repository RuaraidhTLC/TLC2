
import os
from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route("/")
def index():
    return render_template("index.html")

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Features Page
@app.route("/features")
def features():
    return render_template("features.html")

# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Thank You Page
@app.route("/thank_you")
def thank_you():
    return render_template("thank_you.html")

# Charge Calculator
@app.route("/charge_calculator")
def charge_calculator():
    return render_template("charge_calculator.html")

# Calculator Results
@app.route("/calculator_results")
def calculator_results():
    return render_template("calculator_results.html")

# Financial Snapshot
@app.route("/financial_snapshot")
def financial_snapshot():
    return render_template("financial_snapshot.html")

# Image Testing
@app.route("/test_images")
def test_images():
    return render_template("test_images.html")

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

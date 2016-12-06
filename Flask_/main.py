from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    countries = ("Denmark", "Sweden", "Finland")
    return render_template("index.html", countries=countries, show=True)

if __name__ == "__main__":
    app.run(debug=True)
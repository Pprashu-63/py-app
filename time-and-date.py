from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date as a string
    return f"Hello the Current Date and Time: {formatted_date}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

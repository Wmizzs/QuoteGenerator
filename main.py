from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "You miss 100% of the shots you don’t take.",
    "Success is not final, failure is not fatal.",
    "What we think, we become.",
    "Hard work beats talent when talent doesn't work hard.",
    "Do what you can, with what you have, where you are.",
    "All we have to decide is what to do with the time that is given us.",
    "What we fear doing most is usually what we most need to do.",
    "The best time to plant a tree was 20 years ago. The second best time is now.",
    "Focus is a matter of deciding what things you will not do.",
    "The only way to do great work is to love what you do."
]

@app.route("/")
def quote():
    return f"""
    <html>
      <head>
        <meta charset="UTF-8">
        <title>Random Quote</title>
        <style>
          body {{
            font-family: sans-serif;
            text-align: center;
            padding-top: 10px;
            font-size: 1.5rem;
            color: #333;
            background: transparent;
          }}
        </style>
      </head>
      <body>
        “{random.choice(quotes)}”
      </body>
    </html>
    """



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

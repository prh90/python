from flask import Flask

app = Flask(__name__)


@app.route('/')  # 'http://www.google.com/' it is the slash
def homw():
    return "Hello World"


app.run(port=5000)

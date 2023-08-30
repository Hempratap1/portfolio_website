from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/portfolio")
def portfolio():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True, port=5001)
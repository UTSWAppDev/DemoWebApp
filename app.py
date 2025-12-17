from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Hello")


@app.route('/greeting.html', methods=['GET', 'POST'])
def greeting():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        return f"Hello, {escape(name)}!"
    return render_template('greeting.html', title='Greeting')

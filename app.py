from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/panduan')
def panduan():
    return render_template('panduan.html')


@app.route('/persiapan')
def persiapan():
    return render_template('persiapan.html')


@app.route('/kontak')
def kontak():
    return render_template('kontak.html')


if __name__ == '__main__':
    app.run(debug=True)

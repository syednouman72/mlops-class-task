from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/result')
def result_page():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)

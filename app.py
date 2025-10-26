from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tech')
def tech():
    return render_template('tech.html')

@app.route('/sum/<xx>/<yy>')
def sum_numbers(xx, yy):
    try:
        result = int(xx) + int(yy)
        message = f"The result of sum between {xx} and {yy} is {result}"
    except ValueError:
        message = "You are using miss data type for operation"
    return render_template('result.html', message=message)

@app.route('/concat/<xx>/<yy>')
def concat(xx, yy):
    result = f"{xx}{yy}"
    message = f"The result of concatenate between {xx} and {yy} is {result}"
    return render_template('result.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
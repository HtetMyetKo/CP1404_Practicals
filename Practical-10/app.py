"""http://127.0.0.1:5000/"""

"""http://127.0.0.1:5000/greet"""

"""http://127.0.0.1:5000/greet/htetmyetko"""


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    # return 'Hello World!'
    return '<h1>Hello World :)</h1>'

@app.route('/greet')
def hello():
    """Greet the user"""
    return "Hello !"

@app.route('/greet/htetmyetko')
def greet(name="HtetMyetKo"):
    """Greet with name"""
    return "Hello {}".format(name)

@app.route('/f/<celsius>')
def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return celsius * 9 / 5 + 32

if __name__ == '__main__':
    app.run()

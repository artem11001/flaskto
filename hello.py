from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return ('<h1> Hello World!</h1><br><p>Your browser is %s</p><br>url list %s' % (user_agent, app.url_map))


if __name__ == '__main__':
    app.run(debug=True)
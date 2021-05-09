from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/register', methods=['POST'])
def register():
    pass


@app.route('/register/<string:service>/routes', methods=['POST'])
def register_routes(service):
    pass

if __name__ == '__main__':
    app.run()

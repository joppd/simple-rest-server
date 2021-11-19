from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    _payload_dict = {
        'app_name': 'test',
        'content': 'hello world',
    }
    return json.dumps(_payload_dict, ensure_ascii=False, indent=2)

@app.route("/user/<string:user_name>")
def hello_user(user_name:str):
    _payload_dict = {
        'app_name': 'test',
        'content': 'hello {}!'.format(user_name),
    }
    return json.dumps(_payload_dict, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('run app start.')
    _port = 24573
    app.run(host='0.0.0.0', port=_port, debug=True)
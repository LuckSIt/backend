from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'Мир')  # По умолчанию 'Мир', если параметр не передан
    message = request.args.get('message', 'Привет')  # По умолчанию 'Привет!', если параметр не передан
    return f"Hello {name}! {message}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


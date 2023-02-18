from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def hello():
    language = request.args.get('language')
    if language == 'English':
        return 'Hello world'
    elif language == 'French':
        return 'Bonjour le monde'
    elif language == 'Hindi':
        return 'Namastey sansar'
    else:
        return 'Language not supported'
@app.route('/')
def hi():
    return 'Hello'


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)

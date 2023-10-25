from flask import Flask, request
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'GET':
        return """
        <html><head><title>https://pythonbasics.org</title></head>
        <p>Request: {}</p>
        <body>
        <p>This is an example web server.</p>
        </body></html>
        """.format(request.path)
    elif request.method == 'POST':
        date = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
        return f'{{"time": "{date}"}}'

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)

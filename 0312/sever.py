from flask import Flask, request

app = Flask(__name__)

@app.route('/<path>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD'])
def handle_all(path):
    return {
        "method": request.method,
        "path": path,
        "data": request.data.decode(),
        "headers": dict(request.headers)
    }, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
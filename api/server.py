from sanic import Sanic
from sanic.response import json

HOST, PORT = '0.0.0.0', 8000

app = Sanic()

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)

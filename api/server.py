from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS, cross_origin
from colorthief import ColorThief
from io import BytesIO

HOST, PORT = '0.0.0.0', 8000

app = Sanic()
CORS(app)

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

@app.route('/color/what', methods=['POST', 'OPTIONS'])
async def whatColorImage(request):
    key = list(request.files.keys())[0]
    file = request.files.get(key)

    with BytesIO(file.body) as input_file:
        color_thief = ColorThief(input_file)
        # get the dominant color
        dominant_color = color_thief.get_color(quality=1)

        return json({'color': dominant_color})

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)

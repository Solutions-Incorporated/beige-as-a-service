from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS, cross_origin
from colorthief import ColorThief
from PIL import ImageColor
from io import BytesIO

from color import color_hex_to_name, scheme_from_rgb, rgb_to_hex, color_from_name
from PIL import ImageColor

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
        dominant_color_hex = rgb_to_hex(dominant_color)

        return json({'color': dominant_color_hex})

@app.route('/color/scheme', methods=['POST', 'OPTIONS'])
async def color_scheme_handler(request):
    color_hex = request.json['color']
    color_name = color_hex_to_name(color_hex)
    color_rgb = ImageColor.getrgb(color_hex)

    scheme = scheme_from_rgb(color_rgb)
    mapped_scheme = map(color_hex_to_name, scheme)

    return json({
        'name': color_name,
        'scheme': list(mapped_scheme),
    })

@app.route('/color/name/', methods=['POST', 'OPTIONS'])
async def find_by_name(request):
    color_name = request.json['name']
    return json({'color': color_from_name(color_name)})

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)

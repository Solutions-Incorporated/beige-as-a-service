from sanic import Sanic
from sanic.response import json
from colorthief import ColorThief
from io import BytesIO

from color import rgb_to_name

HOST, PORT = '0.0.0.0', 8000

app = Sanic()

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

@app.route('/color/what', methods=['POST'])
async def whatColorImage(request):
    key = list(request.files.keys())[0]
    file = request.files.get(key)

    with BytesIO(file.body) as input_file:
        color_thief = ColorThief(input_file)
        # get the dominant color
        dominant_color = color_thief.get_color(quality=1)

        return json({'color': dominant_color})

@app.post('/color/scheme')
async def color_scheme_handler(request):
    color_name = rgb_to_name(request.json['color'])

    return json({
        'name': color_name,
        'scheme': [],
    })

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)

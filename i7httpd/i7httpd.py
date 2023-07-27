import http.server
from inky.auto import auto
from smbus2 import SMBus
from PIL import Image, ImageDraw

class HTTPRequestHandler (http.server.SimpleHTTPRequestHandler):
    def do_PUT(self):
        ctype = self.headers['Content-Type']
        length = int(self.headers['Content-Length'])
        print("Type: " + ctype)
        print("Length: " + self.headers['Content-Length'])

        with open("/tmp/inkyimg",'wb') as f:
            f.write(self.rfile.read(length))

        print("displaying image")
        print((display.width, display.height))
        with Image.open("/tmp/inkyimg") as im:
            imresized = im.resize((display.width, display.height))
            display.set_image(imresized)
            display.show()
        print("done")

if __name__ == '__main__':
    display = auto(i2c_bus=SMBus(0))
    http.server.test(HandlerClass=HTTPRequestHandler, port=80)


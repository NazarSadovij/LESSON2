from PIL import Image, ImageFilter

class ImageEditor():
    def __init__ (self, filename):
        self.filename = filename
        self.original = None
        self.changed = []

    def open (self):
        try:
                self.original = Image.open(self.filename)

                self.original.show()
        except:
            print("file not found")

    def do_right(self):
        rotate = self.original.transpose(Image.ROTATE_270)

        self.changed.append(rotate)
        rotate.show()
    
        def do_left(self):
        rotate = self.original.transpose(Image.ROTATE_90)

        self.changed.append(rotate)

    def mirror(self):
        rotate = self.original.transpose(FLIP_LEFT_RIGHT)

        self.changed.append(rotate)
        rotate.show()


img = ImageEditor("ball.png")
img.open()
img.do_left()
import numpy as np
from PIL import Image

ascii_gradient = {
    0: " ",
    1: " ",
    2: "'",
    3: ".",
    4: ",",
    5: ":",
    6: "-",
    7: "=",
    8: "+",
    9: "*",
    10: "o",
    11: "&",
    12: "8",
    13: "#",
    14: "@",
    15: "@"
}

class image_handler:
    def __init__(self, fileName):
        img = Image.open(fileName).convert("RGB")

        self.arr = np.array(img).tolist()

        self.height = len(self.arr)
        self.length = len(self.arr[0])
        self.depth = len(self.arr[0][0])

        del img

    def convert_monochrome(self):
        image_out = []
        for i in range(self.height):
            row = self.arr[i]

            new_row = []

            for j in range(self.length):
                pixel = row[j]

                r = pixel[0]
                g = pixel[1]
                b = pixel[2]

                # find luminosity (range 0 to 256)
                luminosity = 0

                luminosity += int(r * 0.21)
                luminosity += int(b * 0.72)
                luminosity += int(b * 0.07)

                new_row.append(luminosity)

            image_out.append(new_row.copy())

        self.arr = image_out.copy()


    def pixelate_monochrome(self, newHeight, newLength):
        currHeight = self.height
        currLength = self.length

        length_scale = currLength / newLength
        height_scale = currHeight / newHeight

        image_out = []

        for i in range(newHeight):
            row = []
            for j in range(newLength):
                x_start = int(j * length_scale)
                x_end = int((j+1) * length_scale)
                y_start = int(i * height_scale)
                y_end = int((i+1) * height_scale)

                pixel_region = [
                        self.arr[y][x]
                        for y in range(y_start, min(y_end, currHeight))
                        for x in range(x_start, min(x_end, currLength))
                        ]

                avg_color = sum(pixel_region) // len(pixel_region)

                row.append(avg_color)
            image_out.append(row.copy())

        self.arr = image_out.copy()
        
        self.height = len(self.arr)
        self.length = len(self.arr[0])
        # self.depth = len(self.arr[0][0])

    def convert_16_bit(self):
        out = []

        for row in self.arr:
            newRow = []
            for val in row:
                val //= 16
                new_val = ascii_gradient[val]
                newRow.append(new_val)

            out.append(newRow.copy())

        self.arr = out.copy()

                
    def print_img_debug(self, mod):
        for row in self.arr:
            for i in range(self.length):
                if i % mod == 0:
                    print(row[i], end = '')

            print()


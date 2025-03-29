from image_handler import image_handler
import os

terminal_size = os.get_terminal_size()

rows = terminal_size.lines
cols = terminal_size.columns

img = image_handler("3VJmL.jpg")

img_rows_to_cols_ratio = img.height / img.length
img.convert_monochrome()
img.pixelate_monochrome(rows, cols)
img.convert_16_bit()
img.print_img_debug(1)



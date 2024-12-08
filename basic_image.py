from PIL import Image, ImageDraw

img = Image.new("RGB", (250, 250), "white")

draw = ImageDraw.Draw(img)

draw.line((5, 5, 240, 10), fill="black", width=3)
draw.rectangle((50, 50, 200, 200), outline="blue", width=3)
draw.rectangle((100, 100, 150, 150), fill="green")
draw.ellipse((60, 60, 180, 180), outline="red", width=3)
draw.ellipse((80, 80, 120, 120), fill="yellow")

draw.text((20, 220), "Hello, Pillow!", fill="purple")

img.show()

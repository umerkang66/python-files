from PIL import Image, ImageFilter

# processing pikachu image file
# img = Image.open('./images/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.SHARPEN)
# # this will convert the image into grey scale
# filtered_img = filtered_img.convert("L")
# crooked = filtered_img.rotate(90)
# resized_img = crooked.resize((300, 300))
# cropped_img = resized_img.crop((100, 100, 400, 400))
# cropped_img.save("blur.png", "png")
# cropped_img.show()

# processing astronaut image file
img = Image.open("./images/astro.jpg")
# thumbnail is used instead of resize if we want to keep the aspect ratio intact
# it also doesn't return anything
img.thumbnail((400, 400))
img.save("new_astro.jpeg", "jpeg")
img.show()

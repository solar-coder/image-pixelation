# Author: SolarCoder
# Instagram | @solarcoder

from PIL import Image

# opening image
image = Image.open("./image.jpg")

# we scale the image down, so some information
# is lost
smallImage = image.resize((64,64), resample=Image.BILINEAR)

# then, we scaale it back up again to tthe original size,
# so we still get the same dimensions as the photo
res = smallImage.resize(image.size, Image.NEAREST)

# outputting the image
res.save("output.png")
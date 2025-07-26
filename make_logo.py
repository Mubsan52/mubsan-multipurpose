from PIL import Image, ImageDraw, ImageFont

# Create a blank image (600x200 pixels)
img = Image.new('RGBA', (600, 200), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# Colors
dark_blue = (44, 62, 80)
green = (37, 211, 102)

# Draw a simple green rectangle (icon placeholder)
draw.rectangle([20, 50, 100, 130], fill=green)

# Load a font
try:
    font = ImageFont.truetype("arial.ttf", 40)
except:
    font = ImageFont.load_default()

# Write text next to the rectangle
draw.text((120, 70), "Mubsan Multipurpose", fill=dark_blue, font=font)

# Save as logo.png
img.save("logo.png")

print("Logo generated and saved as logo.png!")
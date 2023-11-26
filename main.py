import requests
from PIL import Image
from fpdf import FPDF

# file you want to create:
filename = "fullpage.pdf"

# URL of the image
image_url = "https://2.bp.blogspot.com/pw/ADCreHdvJ4KSZoT0nJjnZUdiYh54A3R1YvpB5W9lnob4nVhL4KSKkavOOu_vM0mCEKDCOx6_jzpp5Qfs4S9UAc33ytD3PJq_taKwlQXVOToglC2S6nPlqQ=s0?rhlupa=MTY1LjIyNy4yMTcuNjc=&rnvuka=TW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBIZWFkbGVzc0Nocm9tZS8xMTQuMC41NzM1LjEzMyBTYWZhcmkvNTM3LjM2"

# Create a new pdf and get full image
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
fullImage = Image.open(requests.get(image_url, stream=True).raw)

# Split the image into equal halves
width, height = fullImage.size
half_width = width // 2
left_half = fullImage.crop((0, 0, half_width, height))
right_half = fullImage.crop((half_width, 0, width, height))

# full and split images
fullImage.save(f"fullpageImage.jpg")
left_half.save(f"firstHalf.jpg")
right_half.save(f"secondHalf.jpg")

# adding pages
pdf.add_page()
pdf.image(f"firstHalf.jpg", 0, 0, 210, 297)  # A4 size, adjust as needed
pdf.add_page()
pdf.image(f"secondHalf.jpg", 0, 0, 210, 297)  # A4 size, adjust as needed

pdf.output(f"{filename}", "F")
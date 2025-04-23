import pytesseract
from PIL import Image, ImageEnhance

# Set your Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load the screenshot image
img = Image.open("vault_pattern.png")  # Replace with your filename if different

# Crop the area where pattern unlock text normally appears
# Wider and taller than before to be safe
cropped = img.crop((0, 870, 800, 1080))  # (left, top, right, bottom)

# Improve contrast to help OCR
enhancer = ImageEnhance.Contrast(cropped)
cropped = enhancer.enhance(2.0)  # Try 1.5–3.0 if needed

# Show cropped region (optional)
cropped.show()

# Perform OCR
text = pytesseract.image_to_string(cropped)

# Print raw text output (with hidden characters shown)
print("🔍 Raw OCR Output:")
print(repr(text))

# Detect pattern message
if "pattern" in text.lower() and "extract" in text.lower():
    print("✅ Pattern available to claim!")
else:
    print("❌ No pattern extract prompt detected.")

import pyautogui
import pytesseract
from PIL import Image, ImageEnhance, ImageOps
import time

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# OCR region where the pattern text appears
ocr_crop = (500, 890, 1320, 1055)
threshold = 150

print("🕒 Scanning starts in 3 seconds — switch to Destiny 2 vault now!")
time.sleep(3)

# Scan all 5 rows (rows 1 to 5)
for row in range(5):
    y = 400 + row * 100  # vertical spacing per row
    vault_row_slots = [(500 + i * 100, y) for i in range(10)]  # 10 items per row

    for idx, (x, y_actual) in enumerate(vault_row_slots):
        print(f"\n🔄 Hovering over Row {row + 1}, Slot {idx + 1} at ({x}, {y_actual})")

        pyautogui.moveTo(x, y_actual, duration=0.2)
        time.sleep(0.8)  # Hover long enough to trigger inspect tooltip

        # Take screenshot and crop to pattern detection region
        screen = pyautogui.screenshot()
        cropped = screen.crop(ocr_crop)

        # Enhance for OCR
        cropped = ImageOps.grayscale(cropped)
        enhancer = ImageEnhance.Contrast(cropped)
        cropped = enhancer.enhance(2.5)
        bw = cropped.point(lambda px: 255 if px > threshold else 0, '1')

        # OCR
        text = pytesseract.image_to_string(bw, config="--psm 6")
        print("📖 OCR:", repr(text))

        if "pattern" in text.lower() and "extract" in text.lower():
            print("✅ Pattern can be claimed!")
        else:
            print("❌ No pattern extract prompt detected.")

        time.sleep(0.3)

print("\n✅ Full vault page scan complete.")

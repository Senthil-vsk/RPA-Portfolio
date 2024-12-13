import pytesseract
import cv2

def extract_text_from_image(image_path):
    # Load image
    img = cv2.imread(image_path)
    
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to improve OCR accuracy
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    # Extract text using Tesseract
    text = pytesseract.image_to_string(thresh)
    
    return text

# Usage example
text = extract_text_from_image('invoice_image.jpg')
print(text)

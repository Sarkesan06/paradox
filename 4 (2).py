import pytesseract
from PIL import Image
from gtts import gTTS
import os

# Function to extract text from image using OCR with the selected language
def extract_text_from_image(image_path, lang='eng'):
    """
    Extracts text from an image using pytesseract OCR. 
    Supports multiple languages (e.g., 'eng' for English, 'fra' for French, etc.).
    """
    # Open the image file
    img = Image.open(image_path)
    
    # Use pytesseract to extract text from the image in the specified language
    extracted_text = pytesseract.image_to_string(img, lang=lang)
    
    return extracted_text

# Improved summarization: Taking the first few paragraphs as summary
def long_summarize(text, num_paragraphs=5):
    """
    Summarizes the text by taking the first few paragraphs.
    """
    paragraphs = text.split('\n\n')  # Split the text into paragraphs
    summary = '\n\n'.join(paragraphs[:num_paragraphs])  # Join the first 'num_paragraphs' paragraphs
    return summary

# Function to convert text to speech in the specified language
def text_to_speech(text, language='en'):
    """
    Converts the input text to speech in the specified language.
    """
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")  # For Windows, on Mac/Linux use 'open' or 'xdg-open'

# Main function to run the OCR, summarize, and convert text to speech
def main(image_path, ocr_language='eng', tts_language='en'):
    """
    Extracts text from the image, summarizes it, and converts the summary to speech.
    Supports both OCR and TTS in different languages.
    """
    # Extract text from the image using the specified OCR language
    extracted_text = extract_text_from_image(image_path, lang=ocr_language)
    print("Extracted Text:\n", extracted_text)
    
    # Summarize the extracted text by taking the first 5 paragraphs
    summary = long_summarize(extracted_text)
    print("\nSummary:\n", summary)
    
    # Convert the summary to speech in the specified language
    text_to_speech(summary, tts_language)

# Example usage
if __name__ == "__main__":
    image_path = r'C:\Users\henry\Downloads\news1.jpeg'  # Replace with your image file path
    
    # Example usage with different OCR and TTS languages
    ocr_language = 'fra'  # Language for OCR (e.g., 'fra' for French, 'eng' for English, 'spa' for Spanish)
    tts_language = 'it'  # Language for TTS (e.g., 'fr' for French, 'en' for English, 'es' for Spanish)
    
    main(image_path, ocr_language, tts_language)

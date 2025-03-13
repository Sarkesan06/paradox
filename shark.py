import pytesseract
from PIL import Image
from gtts import gTTS
import os

# Function to perform OCR on an image
def extract_text_from_image(image_path):
    try:
        # Open the image using PIL
        img = Image.open(image_path)
        
        # Use Tesseract to extract text
        text = pytesseract.image_to_string(img)
        
        return text
    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return None

# Function to convert text to speech in a given language
def text_to_speech(text, output_folder, language='en'):
    if not text:
        print("No text to convert to speech.")
        return
    
    try:
        # Create a gTTS object
        tts = gTTS(text=text, lang=language)
        
        # Save the speech as an mp3 file in the output folder
        audio_file = os.path.join(output_folder, 'output.mp3')
        tts.save(audio_file)
        
        # Play the audio file
        if os.name == 'nt':  # Windows
            os.system(f"start {audio_file}")
        else:  # Linux/MacOS
            os.system(f"mpg321 {audio_file}")
        
        print(f"Audio saved as {audio_file} and played successfully.")
    except Exception as e:
        print(f"Error converting text to speech: {e}")

# Main function to run the OCR and text-to-speech
def ocr_and_voice_over(image_path, language='en'):
    # Check if the image path is valid
    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' does not exist.")
        return
    
    # Check if the path points to a file (not a directory)
    if not os.path.isfile(image_path):
        print(f"Error: '{image_path}' is not a valid file. Please provide the path to an image file.")
        return
    
    # Get the folder of the input image
    output_folder = os.path.dirname(image_path)
    if not output_folder:
        output_folder = os.getcwd()  # Use current directory if no folder is specified
    
    # Extract text from the image
    text = extract_text_from_image(image_path)
    if text:
        print("Extracted Text:")
        print(text)
    else:
        print("No text was extracted from the image.")
    
    # Convert the extracted text to speech
    text_to_speech(text, output_folder, language)

# Example usage
image_path = r'D:\Delta Headlines\097c1588-4bf1-4ea7-a4df-77ba98375e7b.jpg'  # Replace with the path to your image file
language = 'en'  # You can change the language to any supported language (e.g., 'fr', 'es', 'de', etc.)

ocr_and_voice_over(image_path, language)

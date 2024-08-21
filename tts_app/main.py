import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tts_app.pdf_processor import extract_text_from_pdf
from tts_app.tts_engine import text_to_speech

def main(pdf_filename, output_audio_file):
    pdf_path = os.path.join("pdfs", pdf_filename)
    text = extract_text_from_pdf(pdf_path)
    if text:
        text_to_speech(text, output_audio_file)
        print(f"Audio file saved as: {output_audio_file}")
    else:
        print("No text found in the PDF.")

if __name__ == "__main__":
    pdf_filename = "sample4.pdf"  # Replace with your PDF file name
    output_audio_file = "output_audio4.mp3"  # Desired output audio file name
    main(pdf_filename, output_audio_file)

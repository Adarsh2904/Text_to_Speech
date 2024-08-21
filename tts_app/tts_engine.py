import pyttsx3

def text_to_speech(text, output_file):
    try:
        engine = pyttsx3.init()
        engine.save_to_file(text, output_file)
        engine.runAndWait()
    except Exception as e:
        print(f"Error converting text to speech: {e}")

import speech_recognition as sr
from pynput.keyboard import Key, Controller

keyboard = Controller()

def listen_to_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a command...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        return command
    except sr.UnknownValueError:
        return None

def execute_game_action(command):
    if command == "faster boy":
        print("Speeding up the horse!")
        keyboard.press(Key.shift)
        # You may want to hold the key for some time
        # Example: time.sleep(1) followed by keyboard.release(Key.shift)
    else:
        print(f"Command '{command}' not recognized.")

if __name__ == "__main__":
    while True:
        command = listen_to_command()
        if command:
            execute_game_action(command)


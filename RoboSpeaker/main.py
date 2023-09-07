import os
import platform
import pyttsx3

# this is supported on Mac and windows only

if __name__ == '__main__':
    # os.system("say 'Hello welcome to robo speaker'")

    current_system_os = platform.system()

    while True:
        print("Hello and welcome to the robo speaker program!")
        x = input("Please tell me what should i say: ")
        if x == 'q':
            break
        if current_system_os == "Darwin":
            command = f"say {x}"
            os.system(command)
        elif current_system_os == "Windows":
            # Initialize the text-to-speech engine
            engine = pyttsx3.init()
            # Convert and play the text as speech
            engine.say(x)

            # Wait for the speech to finish
            engine.runAndWait()
        else:
            print('Unsupported operating system')

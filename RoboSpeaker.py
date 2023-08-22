# import pyttsx3

# def speak_text(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# if __name__ == "__main__":
#     x = input("Enter Word: ")
#     speak_text(x)



import os

def texttospeech(text):
    command = f'echo "{text}" | powershell -command "& {{Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak([Console]::In.ReadToEnd())}}"'
    os.system(command)

if __name__ == "__main__":
    while True:
        x = input("Enter Word: ")
        if x == '0':
            break
        else:            
            texttospeech(x)
import os.path
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import openai

api_key = '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'


def ai(prompt):
    openai.api_key = api_key
    text = f"OpenAI response for Prompt {prompt} \n *********************************************  \n\n"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Attempt to extract the response content
    try:
        response_content = response["choices"][0]["message"]["content"]
        print(response_content)
        text += response_content
    except KeyError as e:
        print(f"Error: {e}")
        text += "Error: Unable to extract content from the response."


    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt","w") as f:
        f.write(text)



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'talksy' in command:
                command = command.replace('talksy', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')  # 12hr format
        print(time)
        talk("current time is " + time)
    elif 'who is' in command or 'what is' in command:
        person = command.replace('who is', '').replace('what is', '').strip()
        if person:
            try:
                info = wikipedia.summary(person, 1)  # 1 line
                print(info)
                talk(info)
            except wikipedia.exceptions.PageError:
                talk(f"Sorry, I couldn't find information about {person} on Wikipedia.")
        else:
            talk("Please provide a valid person's name.")
    elif 'date' in command:
        talk('Sorry, I have a boyfriend')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'linkedin' in command:
        talk("Opening linkedin")
        webbrowser.open("https://www.linkedin.com/in/manika-sethi/")
    elif 'using artificial intelligence' in command:
        ai(prompt=command)
    else:
        talk("Please say the command again")
while True:
    run_alexa()



"""

First you have to install below libraries:
To install a library in python, you should open your terminal in pycharm and type: "pip install "the_name_of_the_library" "

pip install SpeechRecognition
(a Python library that allows you to recognize and transcribe speech from various sources)

pip install pyttsx3
(a Python library that enables text-to-speech conversion.)

pip install pywhatkit
(pywhatkit is a Python library that provides a range of functionalities. It simplifies these tasks by providing easy-to-use functions)

pip install wikipedia
(a Python library that allows you to retrieve information from Wikipedia, the popular online encyclopedia)

pip install pyjokes
(pyjokes is a Python library that generates random, often humorous, jokes.)

pip install pyAudio
(a Python library allowing you to easily record and play audio streams in your Python programs)

"""


# importing the libraries that we want to use for our project

# importing speech_recognition as sr, means instead of using speech_recognition, I will simply write sr ()
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import webbrowser


# below line will set the AI voice speed, lower the number --> lower the speed of AI talking
voice_rate = 160

# We will use below line to use sr (speech_recognition) as our voice recognizer. we call it listener
listener = sr.Recognizer()


# in below lines we will set the necessary things needed to use pyttsx3
# pyttsx3 is an AI that can transform text to Audio

# Starting the engine for AI
engine = pyttsx3.init()

# getting the voices that we can have using pyttsx3
voices = engine.getProperty('voices')

# we will use one of the above voices ("voices[0].id") as the voice of our AI
engine.setProperty('voice', voices[0].id)

# below line will set the speed of the talking to voice_rate that we set earlier
engine.setProperty('rate', voice_rate)



def take_command():

    """
    This function is responsible to take the commands
    first, it will use our microphone as the source of input, it will listen to the source using the listener that we
    set earlier. Then, it will transform our audio into a text format.

    :return: the output of this function is our command in the text format
    """

    try:
        # using our microphone as the source
        with sr.Microphone() as source:
            # print listening ... to notify the user
            print("listening ...")
            # listening to the command and storing the audio command
            voice = listener.listen(source)
            # below code will transform the audio command into the text format and store it in command variable
            command = listener.recognize_google(voice)
            # printing the command which is now in the text format
            print(command)
            # returning the text format of command as the output of the function
            return command

    except:
        # if anything goes wrong, and the above code couldn't run, we will print something to notify the user
        print("repeat the question again")



def talk(text):
    """
    This function is responsible to convert a text file into audio and say it out loud.
    :param text: the input is a text that we want AI to say it
    :return: This function will not return anything as a result, so there is no output
    """
    # saying the text out loud
    engine.say(text)
    # run the engine and wait again for future commands
    engine.runAndWait()


def run_alex():
    """
    This is the main function. We wil control the program here and decide what to do based on the command.
    :return: the function does not have any output
    """

    # calling take_command() function to get the audio voice from microphone, and gives us the text format of the
    # command. We will store the output of the function in my_command
    my_command = take_command()

    # the text format of a command could be in uppercase or lowercase. by using my_command.lower(), we can convert every
    # thing into lower case. Therefore, we can now check the words in the command.

    # if "hello" as in the command, call talk() function to say something.
    # whatever we want it to say, we just have to give that as a text to talk function as an input
    if "hello" in my_command.lower():
        talk("Hello there!")

    # when we want to have a chain of if conditions, we can use elif.
    elif "play music" in my_command.lower():
        # we can also ask a follow up question. in this case, if the user says play music. we can again ask the user
        # what music he wants to play?
        talk("what song would you like me to play?")
        # we can store the name of the music in "song_name variable"
        song_name = take_command()
        if song_name:
            talk(f"Playing {song_name}")
            # we can use below code to play the music
            pywhatkit.playonyt(song_name)

    elif "time" in my_command.lower():
        time = datetime.datetime.now()
        talk(f'current time is {time}')

    elif "mail" in my_command.lower():
        talk("opening your email")
        # we can use webbrowser library to open any website that we want. We just have to give the URL of the website
        # as the input. below code shows you how you can use this library
        webbrowser.open('https://mail.google.com')

    elif "joke" in my_command.lower():
        # we can use below code to use pyjokes library to tell us some jokes
        # the result of below line is a joke in the text format.Then we can use talk() function to say the joke out loud
        joke_ = pyjokes.get_joke()
        talk(joke_)

    """
    As you can see, now you are able to add more and more to your AI and make it better and better. You can ask follow
    up questions like we did in "play music". you can set some customized answers to make to more exciting.
    And you can open any website using webbrowser.open('URL of the website'). 
    Manipulate the program as you wish and make it more interesting!
    """


if __name__ == "__main__":

    """
    This is the start of the program
    """

    # calling the run_alex() function over and over again
    while True:
        run_alex()








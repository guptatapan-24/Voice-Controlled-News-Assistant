import urllib.request, json
import speech_recognition as sr
import pyttsx3

# Function to speak the given text using text-to-speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initialize the text-to-speech engine
engine=pyttsx3.init()
engine.setProperty("rate", 180) # Speed of speech

# Introduction of the News Assistant
intro="Hello there! I am your News Assistant providing you the latest news of the day"\
" from around the world.\nTell me your interested category or a keyword related to which"\
" you want to know the news.\nYou can also change the country by giving the country code."\
"\nDefault country is India."

speak(intro)

# Initialize the speech recognizer
r=sr.Recognizer()

# Function to get the news based on the user's input
def news():
    try:
        with sr.Microphone() as source:
            audio = r.listen(source) # Capture audio input

            # Check if the user wants the news based on the category
            if "category" in r.recognize_google(audio):
                url = f"https://gnews.io/api/v4/top-headlines?category={r.recognize_google(audio).split()[-1].lower()}&lang=en&country=in&max=10&apikey=0168dcfeeed7e5801dc8d761de2e6593"
                with urllib.request.urlopen(url) as response:
                    data = json.loads(response.read().decode("utf-8"))
                    articles = data["articles"]

                    # Iterate and read the news articles
                    for idx, article in enumerate(data['articles'], start=1):
                        print(f"Article {idx}:")
                        print(f"{article['title']}")
                        print("="*50)
                        speak(f"Article {idx}:")
                        speak(f"{article['title']}")
            
            # Check if the user wants the news based on a keyword
            elif "about" in r.recognize_google(audio):
                url = f"https://gnews.io/api/v4/top-headlines?q={r.recognize_google(audio).split()[-1].lower()}&lang=en&country=in&max=10&apikey=0168dcfeeed7e5801dc8d761de2e6593"
                with urllib.request.urlopen(url) as response:
                    data = json.loads(response.read().decode("utf-8"))
                    articles = data["articles"]

                    # Iterate and read the news articles
                    for idx, article in enumerate(data['articles'], start=1):
                        print(f"Article {idx}:")
                        print(f"{article['title']}")
                        print("="*50)
                        speak(f"Article {idx}:")
                        speak(f"{article['title']}")
            
            # Check if the user wants to change the country
            elif "change country" in r.recognize_google(audio):
                url = f"https://gnews.io/api/v4/top-headlines?category=general&lang=en&country={r.recognize_google(audio).split()[-1].lower()}&max=10&apikey=0168dcfeeed7e5801dc8d761de2e6593"
                with urllib.request.urlopen(url) as response:
                    data = json.loads(response.read().decode("utf-8"))
                    articles = data["articles"]

                    # Iterate and read the news articles
                    for idx, article in enumerate(data['articles'], start=1):
                        print(f"Article {idx}:")
                        print(f"{article['title']}")
                        print("="*50)
                        speak(f"Article {idx}:")
                        speak(f"{article['title']}")
    
    # Handle errors
    except Exception as e:
        speak("Sorry, I could not understand the audio.")

# Main loop to get the news
while True:
    news() # Function call
    try:
        # Ask if the user wants to know more news
        speak("Do you want to know more news?")
        with sr.Microphone() as sour:
            aud=r.listen(sour) # Capture audio input
            if "yes" in r.recognize_google(aud).lower():
                speak("OK! Tell me your interested category or a keyword.")
                news()
            elif 'no' in r.recognize_google(aud).lower():
                speak("Thank you for using the News Assistant. Have a great day!")
                break
    except Exception as e:
        # Handle errors
        speak("Sorry, I could not understand the audio.")
        break
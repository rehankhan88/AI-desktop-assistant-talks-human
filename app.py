import os

import speech_recognition as sr
import pyttsx3
import webbrowser
import openai

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # Adjusts for ambient noise
        r.pause_threshold = 1  # Pause threshold before assuming user is done speaking
        print("Listening...")
        try:
            audio_data = r.listen(source)
            print("Recognizing...")
            query = r.recognize_google(audio_data, language="en-PK")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""
        except Exception as e:
            print(f"An error occurred: {e}")
            return ""

if __name__ == '__main__':
    print('PyCharm')
    say("Hello, I am AI")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [
        ["Google", "https://www.google.com"],
        ["Bing", "https://www.bing.com"],
        ["Yahoo", "https://www.yahoo.com"],
        ["DuckDuckGo", "https://www.duckduckgo.com"],
        ["Baidu", "https://www.baidu.com"],

        ["Facebook", "https://www.facebook.com"],
        ["Twitter", "https://www.twitter.com"],
        ["Instagram", "https://www.instagram.com"],
        ["LinkedIn", "https://www.linkedin.com"],
        ["TikTok", "https://www.tiktok.com"],

        ["YouTube", "https://www.youtube.com"],
        ["Vimeo", "https://www.vimeo.com"],
        ["Dailymotion", "https://www.dailymotion.com"],
        ["Twitch", "https://www.twitch.tv"],

        ["Amazon", "https://www.amazon.com"],
        ["eBay", "https://www.ebay.com"],
        ["Alibaba", "https://www.alibaba.com"],
        ["Etsy", "https://www.etsy.com"],
        ["Walmart", "https://www.walmart.com"],

        ["BBC", "https://www.bbc.com"],
        ["CNN", "https://www.cnn.com"],
        ["The New York Times", "https://www.nytimes.com"],
        ["The Guardian", "https://www.theguardian.com"],
        ["Reuters", "https://www.reuters.com"],

        ["TechCrunch", "https://www.techcrunch.com"],
        ["Wired", "https://www.wired.com"],
        ["The Verge", "https://www.theverge.com"],
        ["Gizmodo", "https://www.gizmodo.com"],
        ["Ars Technica", "https://www.arstechnica.com"],

        ["Coursera", "https://www.coursera.org"],
        ["Khan Academy", "https://www.khanacademy.org"],
        ["edX", "https://www.edx.org"],
        ["Udemy", "https://www.udemy.com"],
        ["MIT OpenCourseWare", "https://ocw.mit.edu"],

        ["Netflix", "https://www.netflix.com"],
        ["Hulu", "https://www.hulu.com"],
        ["Disney+", "https://www.disneyplus.com"],
        ["Spotify", "https://www.spotify.com"],
        ["HBO Max", "https://www.hbomax.com"],

        ["Google Drive", "https://www.drive.google.com"],
        ["Dropbox", "https://www.dropbox.com"],
        ["OneDrive", "https://www.onedrive.live.com"],
        ["iCloud", "https://www.icloud.com"],
        ["Box", "https://www.box.com"],

        ["TripAdvisor", "https://www.tripadvisor.com"],
        ["Expedia", "https://www.expedia.com"],
        ["Booking.com", "https://www.booking.com"],
        ["Airbnb", "https://www.airbnb.com"],
        ["Skyscanner", "https://www.skyscanner.com"],

        ["LinkedIn Jobs", "https://www.linkedin.com/jobs"],
        ["Indeed", "https://www.indeed.com"],
        ["Glassdoor", "https://www.glassdoor.com"],
        ["Monster", "https://www.monster.com"],
        ["CareerBuilder", "https://www.careerbuilder.com"],

        ["GitHub", "https://www.github.com"],
        ["Stack Overflow", "https://www.stackoverflow.com"],
        ["GitLab", "https://www.gitlab.com"],
        ["Bitbucket", "https://www.bitbucket.org"],
        ["HackerRank", "https://www.hackerrank.com"],

        ["PayPal", "https://www.paypal.com"],
        ["Stripe", "https://www.stripe.com"],
        ["Robinhood", "https://www.robinhood.com"],
        ["Coinbase", "https://www.coinbase.com"],
        ["Bloomberg", "https://www.bloomberg.com"],

        ["Reddit", "https://www.reddit.com"],
        ["Quora", "https://www.quora.com"],
        ["Stack Exchange", "https://www.stackexchange.com"],
        ["4chan", "https://www.4chan.org"],
        ["Disqus", "https://www.disqus.com"],
        ["wikipedia", "https://www.wikipedia.com"]
    ]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir....")
                webbrowser.open(site[1])

        import os

        if "open music" in query:
            musicPath = r"C:\Users\MUHIB\Downloads\Deep learning project end to end _ Potato Disease Classification - 2 _Data collection_ preprocessing(720P_HD).mp4"
            os.system(f"start {musicPath}")
        import datetime

        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir, the time is {hour} bajjke {min} minutes")

        if "open vs code " in query.lower():
            os.system("open /System/Applications/Visual Studio Code.app")

        if query:
           say(query)

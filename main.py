import random
import chatgtp
import pyttsx3
import speech_recognition as sr

def speak(text):
  # Use pyttsx3 to speak the text
  engine = pyttsx3.init()
  engine.say(text)
  engine.runAndWait()

def generate_response(message):
  # Use Chatgtp to generate a response based on the message
  response = chatgtp.Chatgtp().get_response(message)
  return response

def listen_and_respond():
  # Set up the recognizer
  r = sr.Recognizer()

  # Start listening to the microphone
  with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)

  # Try to recognize the speech and handle the response
  try:
    message = r.recognize_google(audio)
    print("You said: " + message)
    response = generate_response(message)
    print("Chatbot: " + response)
    speak(response)
  except sr.UnknownValueError:
    print("Could not understand audio")
  except sr.RequestError as e:
    print("Error while requesting results: {0}".format(e))

# Start the chatbot
print("Hello! I'm a chatbot powered by Chatgtp. How can I help you today?")
while True:
  listen_and_respond()

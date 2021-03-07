import speech_recognition as sr 
import pyttsx3


#Initialize speechRecognizer.
recognizer=sr.Recognizer()

#Function to convert text to speech .
def Speech_To_Text(what_has_come_out_of_your_mouth):
    #Initialize the engine.
    convert=pyttsx3.init()
    convert.say(what_has_come_out_of_your_mouth)
    convert.runAndWait()
    #Loop infinitely for users to speak .
while True:
        #Let the microphone be your source of input .
        try:
           with sr.Microphone() as mic:
                  recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                   #Listen for the users input .
                  audio_sound=recognizer.listen(mic)
                   #Using google to recognize audio.
                  myText=recognizer.recognize_google(audio_sound)
                  myText=myText.lower()
                  
                  print("This is what you  have just said: "+myText)
                  Speech_To_Text(myText)
        except sr.RequestError as e:
            print("Could not request the result {0}".format(e))
        except sr.UnknownValueError:
            print("Waiting for you to say something......")
            convert=pyttsx3.init()
            convert.say("Waiting for you to say something")
            convert.runAndWait()
           

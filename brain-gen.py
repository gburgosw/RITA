import behavior.naochat.aiml as aiml
import os
import time
import pyttsx

k = aiml.Kernel()
k.learn("std-startup.xml")
k.respond("LOAD AIML B")
k.saveBrain("behavior/naochat/standard.brn")
engine = pyttsx.init()
os.system("clear")
engine.say('hola')
engine.runAndWait()

print "RITA:  Hola!"

while True:
    a = raw_input("USUARIO:  ")
    Cadena = k.respond(a)
    print "RITA:  "+Cadena
    engine.say(Cadena)
    engine.runAndWait()
    time.sleep(0.25)

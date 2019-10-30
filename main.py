#Módulos
from Chatbot import Chatbot
import pyttsx3
import speech_recognition as sr

#Iniciando engine de voz
en = pyttsx3.init()
en.setProperty('voice', b'brazil')
rec = sr.Recognizer()

while True:
    #Selecionando qual tipo de bot usar, Chatbot ou Voicebot
    tipo = input('''Selecione como você quer usar:
[1] Escrita
[2] Voz
''').lower()

    #Classe do voicebot reutilizando a classe do chatbot
    if tipo == '2' or tipo == 'voz':
        class Voicebot(Chatbot):
            def escuta(self, frase=None):
                try:
                    with sr.Microphone() as mic:
                        rec.adjust_for_ambient_noise(mic)
                        fala = rec.listen(mic)
                    frase = rec.recognize_google(fala, language='pt')
                    print(frase)
                except sr.UnknownValueError:
                    print('Deu erro na identificação')
                    return ''
                return super().escuta(frase=frase)

            def fala(self, frase):
                en.say(frase)
                en.runAndWait()
                super().fala(frase)

        bot = Voicebot('Bobozinha')

    if tipo == '1' or tipo == 'escrita':
        bot = Chatbot('Bobozinha')

    #Bot em funcionamento
    while True:
        frase = bot.escuta()
        resp = bot.pensa(frase)
        bot.fala(resp)
        if resp == 'Trocando...' or resp == 'Até mais...':
            break
    if resp == 'Até mais...':
        break

from Chatbot import Chatbot
import pyttsx3 as tts

bot = Chatbot('Bobozinho')
VozOuEscrito = input('Você quer conversar por escrita ou voz?\n>')
VozOuEscrito = VozOuEscrito.lower()
while True:
    if 'escrita' in VozOuEscrito:
        frase = bot.escutaescrito()
        tipo = 0
    if 'voz' in VozOuEscrito:
        print('Escutando...')
        frase = bot.escutavoz()
        tipo = 1
    resp = bot.pensa(frase, tipo)
    bot.fala(resp, tipo)
    if resp == 'Até mais...':
        exit()

from Chatbot import Chatbot

bot = Chatbot('Bobozinho')
while True:
    frase = bot.escuta()
    resp = bot.pensa(frase)
    bot.fala(resp)
    if resp == 'Até mais...':
        break
import telepot
from Chatbot import Chatbot

telegram = telepot.Bot("678363271:AAGhFF9uv82YxMfftV3vqum8uG1fiX4eG5U")

bot = Chatbot("BobotelBot")

def recebendoMsg(msg):
    frase = bot.escuta(frase=msg['text'])
    resp = bot.pensa(frase)
    bot.fala(resp)
    #chatID = msg['chat']['id']
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    if 'http' or '.exe' in resp:
        telegram.sendMessage(chatID,'Abrindo...')
    else:    
        telegram.sendMessage(chatID,resp)
    
telegram.message_loop(recebendoMsg)

while True:
    pass
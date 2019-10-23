import json
import sys
import os
import subprocess as sp
import time
import telepot
import random
import pyttsx3 as tts
import speech_recognition as sr

class Chatbot():
    def __init__(self, nome):
        try:    
            memoria = open(nome+'.json', 'r')
        except FileNotFoundError:
            memoria = open(nome+'.json', 'w')
            memoria.write('[["alexandre", "xnd"], {"oi": "Olá, qual o seu nome?", "sair": "Até mais...", "abra bloco de notas": "executa notepad", "salve": "Tá salvado"}]')
            memoria.close()
            memoria = open(nome+'.json', 'r')
        self.nome = nome
        self.conhecidos, self.dicio = json.load(memoria)
        memoria.close()
        self.historico = [None]
        print('Olá, me chamo {} e estou aqui para fazer o que eu puder para satisfazer seus desejos :)'.format(self.nome))

    def escutaescrito(self, frase=None):
        if frase == None:    
            frase = input('>')
        frase = str(frase)
        if 'executa ' in frase:
            return frase
        frase = frase.lower()
        return frase
    
    def escutavoz(self, frase=None):
        rec = sr.Recognizer()
        with sr.Microphone() as fala:
            frase = rec.listen(fala)
            frase = rec.recognize_google(frase, language='pt-BR')
            print(frase)
        if 'executa ' in frase:
            return frase
        frase = frase.lower()
        return frase

    def pensa(self, frase, tipo):
        if frase in self.dicio:
            return self.dicio[frase]
        ultimaFrase = self.historico[-1]
        if 'o cruzeiro vai ganhar o próximo jogo' in frase:
            c = random.randint(0, 2)
            if c == 1:
                resp = 'Sim'
            else:
                resp = 'Não'
            return resp
        if frase == 'aprenda':
            if tipo == 0:
                return 'Digite a frase:'
            if tipo == 1:
                return 'Diga a frase'
        if ultimaFrase == 'Digite a frase:' or ultimaFrase == 'Diga a frase':
            self.chave = frase
            if tipo == 0:
                return 'Digite a resposta:'
            if tipo == 1:
                return 'Diga a resposta'
        if ultimaFrase == 'Digite a resposta:' or ultimaFrase == 'Diga a resposta':
            resp = frase
            self.dicio[self.chave] = resp
            self.grava_memoria()
            return 'Aprendido'
        if ultimaFrase == 'Olá, qual o seu nome?':
            resp = self.pega_nome(frase)
            return resp
        try:
            resp = str(eval(frase))
            return resp
        except:
            pass
        return 'Não entendi'

    def pega_nome(self, frase):
        nomesp = frase.split()
        if len(nomesp) > 2:
            if 'meu nome eh' in frase:
                frase.replace('eh', 'é')
                nome = frase[12:]
                if nome in self.conhecidos:
                    return 'Salve {}'.format(nome.title())
                else:
                    self.conhecidos.append(nome)
                    self.grava_memoria()
                    return 'Prazer em conhecê-lo {}'.format(nome.title())
            else:
                nome = frase[12:]
                if nome in self.conhecidos:
                    return 'Salve {}'.format(nome.title())
                else:
                    self.conhecidos.append(nome)
                    self.grava_memoria()
                    return 'Prazer em conhecê-lo {}'.format(nome.title())           
        else:
            if frase in self.conhecidos:
                return 'Salve {}'.format(frase.title())
            else:
                self.conhecidos.append(frase)
                self.grava_memoria()
                if frase[len(frase)-1] == 'a':
                    return 'Prazer em conhecê-la {}'.format(frase.title())
                if frase[len(frase)-1] == 'o':
                    return 'Prazer em conhecê-lo {}'.format(frase.title())    
                return 'Prazer em conhecê-lo {}'.format(frase.title())

    def grava_memoria(self):
        memoria = open(self.nome+'.json', 'w')
        json.dump([self.conhecidos, self.dicio], memoria)
        memoria.close()

    def fala(self, frase, tipo):
        if tipo == 0:
            if 'executa ' in frase:
                plataforma = sys.platform
                comando = frase.replace('executa ', '')
                if 'win' in plataforma:
                    os.startfile(comando)
                if 'linux' in plataforma:
                    try:
                        sp.Popen(comando)
                    except FileNotFoundError:
                        sp.Popen(['xdg-open', comando])  
            else:
                print(frase)
                self.historico.append(frase)
                print(self.historico)
        if tipo == 1:
            if 'executa ' in frase:
                plataforma = sys.platform
                comando = frase.replace('executa ', '')
                if 'win' in plataforma:
                    os.startfile(comando)
                if 'linux' in plataforma:
                    try:
                        sp.Popen(comando)
                    except FileNotFoundError:
                        sp.Popen(['xdg-open', comando])  
            else:    
                en = tts.init()
                en.say(frase)
                en.runAndWait()
                self.historico.append(frase)

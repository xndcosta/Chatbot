import json
import sys
import os
import subprocess as sp
import time

class Chatbot():
    def __init__(self, nome):
        try:    
            memoria = open(nome+'Nomes.json', 'r')
        except FileNotFoundError:
            memoria = open(nome+'Nomes.json', 'w')
            memoria.write('["alexandre", "xnd"]')
            memoria.close()
            memoria = open(nome+'Nomes.json', 'r')
        try:    
            dicio = open(nome+'Dicionario.json', 'r')
        except FileNotFoundError:
            dicio = open(nome+'Dicionario.json', 'w')
            dicio.write('{"oi":"Olá, qual o seu nome?", "qual o seu nome?": "Eu me chamo "+self.nome, "sair":"Até mais..."}')
            dicio.close()
            dicio = open(nome+'Nomes.json', 'r')
        self.nome = nome
        self.conhecidos = json.load(memoria)
        self.dicio = json.load(dicio)
        memoria.close()
        dicio.close()
        self.historico = []
        print('Olá, me chamo {} e estou aqui para fazer o que eu puder para satisfazer seus desejos :)'.format(self.nome))

    def escuta(self):
        frase = input('>')
        frase = frase.lower()
        return frase

    def pensa(self, frase):
        if frase in self.dicio:
            return self.dicio[frase]
        if frase == 'aprende':
            chave = input('Digite a frase: ')
            resp = input('Digite a resposta: ')
            self.dicio[chave] = resp
            dicio = open(self.nome+'Dicionario.json', 'w')
            json.dump(self.dicio, dicio)
            dicio.close
            return 'Aprendido'
        try:
            if self.historico[-1] == 'Olá, qual o seu nome?':
                resp = self.pega_nome(frase)
                return resp
        except:
            pass
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
                    memoria = open(self.nome+'Nomes.json', 'w')
                    json.dump(self.conhecidos, memoria)
                    memoria.close()
                    return 'Prazer em conhecê-lo {}'.format(nome.title())
            else:
                nome = frase[12:]
                if nome in self.conhecidos:
                    return 'Salve {}'.format(nome.title())
                else:
                    self.conhecidos.append(nome)
                    memoria = open(self.nome+'Nomes.json', 'w')
                    json.dump(self.conhecidos, memoria)
                    memoria.close()
                    return 'Prazer em conhecê-lo {}'.format(nome.title())           
        else:
            if frase in self.conhecidos:
                return 'Salve {}'.format(frase.title())
            else:
                self.conhecidos.append(frase)
                memoria = open(self.nome+'Nomes.json', 'w')
                json.dump(self.conhecidos, memoria)
                memoria.close()
                if frase[len(frase)-1] == 'a':
                    return 'Prazer em conhecê-la {}'.format(frase.title())
                if frase[len(frase)-1] == 'o':
                    return 'Prazer em conhecê-lo {}'.format(frase.title())    
                return 'Prazer em conhecê-lo {}'.format(frase.title())

    def fala(self, frase):
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

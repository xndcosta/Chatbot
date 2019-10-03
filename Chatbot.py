import json

class Chatbot():
    def __init__(self, nome):
        try:    
            memoria = open(nome+'.json', 'r')
        except FileNotFoundError:
            memoria = open(nome+'.json', 'w')
            memoria.write('["alexandre", "xnd"]')
            memoria.close()
            memoria = open(nome+'.json', 'r')
        self.nome = nome
        self.conhecidos = json.load(memoria)
        memoria.close()
        self.historico = []
        self.frases = {'oi':'Olá, qual o seu nome?', 'sair':'Até mais...'}

    def escuta(self):
        frase = input('>')
        frase = frase.lower()
        return frase

    def pensa(self, frase):
        if frase in self.frases:
            return self.frases[frase]
        if frase == 'aprende':
            chave = input('Digite a frase: ')
            resp = input('Digite a resposta: ')
            self.frases[chave] = resp
            return 'Aprendido'
        if self.historico[-1] == 'Olá, qual o seu nome?':
            resp = self.pega_nome(frase)
            return resp

        return 'Não entendi'

    def pega_nome(self, nome):
        conhecidos = self.conhecidos
        nomesp = nome.split()
        if len(nomesp) > 1:
            nome = nomesp[0]
            for c in range(len(conhecidos)):
                if nome in conhecidos:
                    return 'Salve {}'.format(nome.title())
                else:
                    nome = nomesp[-1]
                    if nome in conhecidos:
                        return 'Salve {}'.format(nome.title())
                    else:
                        self.conhecidos.append(nome)
                        memoria = open(self.nome+'.json', 'w')
                        json.dump(self.conhecidos, memoria)
                        memoria.close()
                        return 'Prazer em conhecê-lo {}'.format(nome.title())
        else:
            for c in range (len(conhecidos)):
                if nome in conhecidos:
                    return 'Salve {}'.format(nome.title())
                else:
                    self.conhecidos.append(nome)
                    memoria = open(self.nome+'.json', 'w')
                    json.dump(self.conhecidos, memoria)
                    memoria.close()
                    return 'Prazer em conhecê-lo {}'.format(nome.title()) 
    
    def fala(self, frase):
        print(frase)
        self.historico.append(frase)

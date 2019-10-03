conhecidos = ['alexandre', 'xnd']
sair = 0

# Início do bot
nome = input('Olá, qual o seu nome?\n')
nome = nome.lower()
nomesp = nome.split()

#funções
def reconhecer_nome(nome_do_usuario):
    if len(nomesp) > 1:
        nome_do_usuario = nomesp[0]
        for c in range(len(conhecidos)):
            if nome_do_usuario in conhecidos:
                return 'Salve {}'.format(nome_do_usuario.title())
            else:
                nome_do_usuario = nomesp[-1]
                if nome_do_usuario in conhecidos:
                    return 'Salve {}'.format(nome_do_usuario.title())
                else:
                    return 'Prazer em conhecê-lo {}'.format(nome_do_usuario.title())
    else:
        for c in range (len(conhecidos)):
            if nome_do_usuario in conhecidos:
                return 'Salve {}'.format(nome_do_usuario.title())
            else:
                return 'Prazer em conhecê-lo {}'.format(nome_do_usuario.title)    

def reconhecer_resposta(resposta):
    if resposta == 'sair':
        print('Até mais!')
        return 'sair'

#bot rodando
saudacao = reconhecer_nome(nome)
print(saudacao)
while sair == 0:
    resp = input('O que você deseja?\n').lower()
    resp = reconhecer_resposta(resp)
    if resp == 'sair':
        sair = 1

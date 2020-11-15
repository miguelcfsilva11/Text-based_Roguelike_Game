import Funcoes as f

dicR = {} # keys - perguntas ; values - resposta certa
dicP = {} # keys - perguntas ; values - respostas
dicQ = {} # keys - nome do quiz ; values - perguntas
dicD = {} # keys - número do quiz ; values - nome do quiz
dicN = {} # keys - número do quiz ; values - quantidade de perguntas

def adicionarR(x):
    res = input('{0})'.format(x))
    respostas.append('{0}) {1}'.format(x, res))

def adicionarP(x):
    per = input('Pergunta {0}: '.format(x))
    perguntas.append(per)
    print('Adicionar 4 opções:')
    for i in 'abcd':
        adicionarR(i)
    certa = f.certa('Indique a opção certa: ')
    dicR[per] = certa
    dicP[per] = respostas

def terminarQ(x):
    nome = input('Dê um nome ao seu Quiz: ')
    nomequiz.append(nome)
    dicQ[nome] = perguntas
    dicD[n] = nome
    dicN[n] = x


nomequiz = []
perguntas = []
while True:
    print('\nO que pretende fazer?\n1 - Criar quiz.\n2 - Editar quiz.\n3 - Jogar quiz\n4 - Sair.')
    while True:
        opcao1 = f.fint('↪ ')
        if opcao1 > 4:
            print('𝘍𝘶𝘯𝘤𝘪𝘰𝘯𝘢𝘭𝘪𝘥𝘢𝘥𝘦 𝘥𝘦𝘴𝘤𝘰𝘯𝘩𝘦𝘤𝘪𝘥𝘢.')
            continue
        else:
            break
    n = 0
    if opcao1 == 1:
        n += 1
        x = 1
        while True:
            respostas = []
            if x == 1:
                adicionarP(x)
            print('\n1.1 - Adicionar pergunta.\n1.2 - Terminar Quiz.')
            while True:
                opcao2 = f.ffloat('↪ ')
                if opcao2 != 1.1 and opcao2 != 1.2:
                    print('Opção desconhecida.')
                    continue
                else:
                    break
            if opcao2 == 1.1:
                x += 1
                adicionarP(x)
            elif opcao2 == 1.2:
                terminarQ(x)
                break

    #todo elif opcao1 == 2:

    elif opcao1 == 3:
        if nomequiz == []:
            print('Não há quizes disponíveis.')
        else:
            y = 0
            print('\nEscolha um Quiz:')
            for i in nomequiz:
                y += 1
                print('{0} - {1}'.format(y, i))
            while True:
                decisao3 = f.fint(' → ') #todo
                if decisao3 > len(nomequiz):
                    print('Opção inválida')
                    continue
                else:
                    break
            perguntas = dicQ[dicD[decisao3]]
            z = 0
            pontos = 0
            print('\n' + dicD[decisao3])
            for i in perguntas:
                z += 1
                respostas = dicP[i]
                print('\n{0}. {1}'.format(z, i))
                for t in respostas:
                    print(t)
                resposta = f.certa('Resposta: ')
                print('Resposta certa: {0}'.format(dicR[i]))
                if resposta == dicR[i]:
                    pontos += 1
            nota = round(pontos*100/dicN[decisao3], 1)
            print('\nClassificação: {0}%'.format(nota))

    elif opcao1 == 4:
        break
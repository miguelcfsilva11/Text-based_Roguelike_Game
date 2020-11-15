def soma(x,y):
    return x+y

def sub(x, y):
    return x-y

def mult(x, y):
    return x*y

def div(x, y):
    return x/y

#Funções para devolver int, float ou str.
def fint(prompt):
    while True:
        w = 1
        value = input(prompt)
        if not value.isnumeric():
            print('𝘐𝘯𝘷𝘢́𝘭𝘪𝘥𝘰.')
            continue
        else:
            break
    return int(value)

def ffloat(prompt):
    while True:
        w = 0
        ponto = 0
        menos = 0
        value = input(prompt)
        for i in value:
            if i != '.' and i != '-' and not i.isnumeric():
                w = 1
            if i == '.':
                ponto += 1
            if i == '-':
                menos += 1
        if w == 1:
            print('𝘐𝘯𝘷𝘢́𝘭𝘪𝘥𝘰.')
            continue
        elif ponto > 1 or menos > 1 :
            print('𝘐𝘯𝘷𝘢́𝘭𝘪𝘥𝘰.')
            continue
        else:
            break
    if ponto == 1 or menos == 1:
        return float(value)
    else:
        return int(value)

def fstr(prompt):
    while True:
        w = 0
        value = input(prompt)
        for i in value:
            if i != ' ' and not i.isalpha():
                w = 1
        if w == 1:
            print('𝘐𝘯𝘷𝘢́𝘭𝘪𝘥𝘰.')
            continue
        else:
            break
    return value



#Funções para o FT4 - 5. Numeros_de_telemovel
def adicionar(i):
    num = fint('Nº de telemóvel: ')
    lista[i] = num

def listat(i):
    return lista[i]

#Funções específicas
def fint9(prompt):
    while True:
        w = 1
        value = input(prompt)
        if not value.isnumeric():
            w = 0
        if len(value) != 9:
            w = 0
        if w == 0:
            print('𝘕𝘶́𝘮𝘦𝘳𝘰 𝘯𝘢̃𝘰 𝘷𝘢́𝘭𝘪𝘥𝘰.')
            continue
        else:
            break
    return int(value)

def fint0_20(prompt):
    while True:
        w = 1
        value = input(prompt)
        if not value.isnumeric():
            print('𝘐𝘯𝘵𝘳𝘰𝘥𝘶𝘻𝘢 𝘶𝘮 𝘯𝘶́𝘮𝘦𝘳𝘰 𝘷𝘢́𝘭𝘪𝘥𝘰 𝘥𝘦 1 𝘢 20.\n')
            continue
        if int(value) > 20:
            print('𝘐𝘯𝘵𝘳𝘰𝘥𝘶𝘻𝘢 𝘶𝘮 𝘯𝘶́𝘮𝘦𝘳𝘰 𝘷𝘢́𝘭𝘪𝘥𝘰 𝘥𝘦 1 𝘢 20.\n')
            continue
        else:
            break
    return int(value)

def certa(prompt):
    while True:
        value = input(prompt)
        if value != 'a' and value != 'b' and value != 'c' and value != 'd':
            print('𝘐𝘯𝘥𝘪𝘲𝘶𝘦 𝘢𝘱𝘦𝘯𝘢𝘴 𝘢 𝘭𝘦𝘵𝘳𝘢 𝘥𝘢 𝘳𝘦𝘴𝘱𝘰𝘴𝘵𝘢 𝘤𝘦𝘳𝘵𝘢')
            continue
        else:
            break
    return value
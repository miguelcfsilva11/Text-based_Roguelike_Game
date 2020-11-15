from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
import pygame



#Funções



def voltar_menu():
    e1.place_forget()
    label2.place_forget()
    label3.place_forget()
    label4.place_forget()
    label5.place_forget()
    label6.place_forget()
    label7.place_forget()
    label8.place_forget()
    label9.place_forget()
    label10.place_forget()
    label11.place_forget()
    label12.place_forget()
    label13.place_forget()
    label14.place_forget()
    label15.place_forget()
    label16.place_forget()
    label17.place_forget()
    label18.place_forget()
    label19.place_forget()
    label20.place_forget()
    label21.place_forget()
    label21e.place_forget()
    label22.place_forget()
    label23.place_forget()
    label24.place_forget()
    label25.place_forget()
    label26.place_forget()
    label27.place_forget()
    label28.place_forget()
    label29.place_forget()
    b3.place_forget()
    b4dec1.place_forget()
    b5dec1.place_forget()
    b6dec2.place_forget()
    b7dec2.place_forget()
    b8dec2.place_forget()
    b9dec3.place_forget()
    b10dec3.place_forget()
    b11dec4.place_forget()
    b12dec4.place_forget()
    b13dec3.place_forget()
    b14dec3.place_forget()
    b15dec4.place_forget()
    b16dec4.place_forget()
    b17dec5.place_forget()
    b18dec5.place_forget()
    b19dec3.place_forget()
    b20dec4.place_forget()
    b21dec4.place_forget()
    b22dec5.place_forget()
    b23dec5.place_forget()
    b24dec6.place_forget()
    b25dec6.place_forget()
    r1.place_forget()
    r2.place_forget(  )
    retry1.place_forget()
    continue1.place_forget()
    continue2.place_forget()
    continue3.place_forget()
    continue4.place_forget()
    continue5.place_forget()
    continue6.place_forget()
    continue7.place_forget()
    continue8.place_forget()
    continue9.place_forget()
    org.place_forget()
    b1.place(relx=.3, rely=.7)
    b2.place(relx=.3, rely=.8)
    label1.place(relx=.2, rely=.2)

def b1_jogar():
    b1.place_forget()
    b2.place_forget()
    label1.place_forget()
    label2.after(120, label1.place_forget())
    label2.place(relx=.2, rely=.2)
    e1.place(relx=.2, rely=.4)
    b3.place(relx=.3, rely=.7)
    r1.place(relx=.1, rely=.1)
    r2.place_forget()


def b3_começar():
    nome3 = nome.get()
    if nome3.isalpha():
        b3.place_forget()
        e1.place_forget()
        label2.place_forget()
        label3.place(relx=.1, rely=.2)
        b4dec1.place(relx=.6, rely=.8)
        b5dec1.place(relx=.2, rely=.8)
        retry1.place_forget()
        label4.config(height=11, width=50, pady=10, text=(
                    "Hesitante, atuas tarde demais.\nDe longe, observas a chegada de um grupo de\n militares armados ao local, seguindo atrás do seu\n aparente chefe."
                    " \n'Não te podes esconder para sempre, {0}'".format(nome3) + "-\n provoca ele, num tom apático. Contato visual é criado\napós notarem na tua presença."
                    " Já sem escolha,\n corres por entre as árvores que te encobrem,\n alcançando um ponto onde uma nova decisão te aguarda.\n "
                    "São 3 os locais por onde podes continuar.\n "
                    "Qual deles será o escolhido?"), font= ("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor=N)

        label10.config(height=2, width=50, pady=10,
                       text="'Porque é que abandonaste a organização, {0}?'".format(nome3) + "\n - questiona o homem."
                       , font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white",
                       anchor=N)
        label28.config(height=4, width=50, pady=10,
                       text="Corres até à luz do fundo.\n ‘Falhas-te a tua missão, {0}’".format(
                           nome3) + "– sussurra uma voz\n no teu consciente. Ainda assim, prossegues\n até ao final, fugindo por fim daquele lugar."
                       , font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white",
                       anchor=N)

    else:
        messagebox.showinfo("Information", "Nome inválido, introduza novamente")
        retry1.place(relx=.3, rely=.7)
        b3.place_forget()

def besconder_1():
    nome = e1.get()
    label3.place_forget()
    b4dec1.place_forget()
    b5dec1.place_forget()
    label21.place(relx=.1, rely=.2)
    continue4.place(relx=.3, rely=.8)


def b4_fugir():
    nome = e1.get()
    label3.place_forget()
    b4dec1.place_forget()
    b5dec1.place_forget()
    label4.place(relx=.1, rely=.2)
    b6dec2.place(relx=.4, rely=.8)
    b7dec2.place(relx=.1, rely=.8)
    b8dec2.place(relx=.7, rely=.8)
    label21.place_forget()
    continue4.place_forget()

def b6_rio():
    nome = e1.get()
    label4.place_forget()
    b6dec2.place_forget()
    b7dec2.place_forget()
    b8dec2.place_forget()
    label5.place(relx=.1, rely=.2)
    b9dec3.place(relx=.2, rely=.8)
    b10dec3.place(relx=.6, rely=.8)

def b7_floresta():
    nome = e1.get()
    label4.place_forget()
    b6dec2.place_forget()
    b7dec2.place_forget()
    b8dec2.place_forget()
    label7.place(relx=.1, rely=.2)
    b13dec3.place(relx=.2, rely=.8)
    b14dec3.place(relx=.6, rely=.8)

def b8_precipicio():
    nome = e1.get()
    label4.place_forget()
    b6dec2.place_forget()
    b7dec2.place_forget()
    b8dec2.place_forget()
    label20.place(relx=.1, rely=.2)
    b10dec3.place(relx=.2, rely=.8)
    b19dec3.place(relx=.6, rely=.8)


def b9_suster():
    nome = e1.get()
    label5.place_forget()
    b9dec3.place_forget()
    b10dec3.place_forget()
    label6.place(relx=.1, rely=.2)
    r2.place(relx=.3, rely=.8)
    r1.place_forget()

def b10_enfrentas():
    nome = e1.get()
    label5.place_forget()
    b9dec3.place_forget()
    b10dec3.place_forget()
    label9.place(relx=.1, rely=.2)
    continue1.place(relx=.3, rely=.8)
    b10dec3.place_forget()
    b19dec3.place_forget()
    label20.place_forget()

def b10_continuar():
    nome = e1.get()
    label9.place_forget()
    continue1.place_forget()
    label10.place(relx=.1, rely=.2)
    org.place(relx=.3, rely=.8)
    b10dec3.place_forget()
    b19dec3.place_forget()
    label20.place_forget()

def b10_org():
    nome = e1.get()
    label10.place_forget()
    org.place_forget()
    label11.place(relx=.1, rely=.2)
    b11dec4.place(relx=.2, rely=.8)
    b12dec4.place(relx=.6, rely=.8)
    b10dec3.place_forget()
    b19dec3.place_forget()
    label20.place_forget()

def b11_arma():
    nome = e1.get()
    label11.place_forget()
    b11dec4.place_forget()
    b12dec4.place_forget()
    label12.place(relx=.1, rely=.2)
    r2.place(relx=.3, rely=.8)
    r1.place_forget()
    b10dec3.place_forget()
    b19dec3.place_forget()
    label20.place_forget()

def b11_fugir():
    nome = e1.get()
    label11.place_forget()
    b11dec4.place_forget()
    b12dec4.place_forget()
    label13.place(relx=.1, rely=.2)
    r2.place(relx=.3, rely=.8)
    r1.place_forget()
    b10dec3.place_forget()
    b19dec3.place_forget()
    label20.place_forget()

def b13_direita():
    nome = e1.get()
    label7.place_forget()
    b13dec3.place_forget()
    b14dec3.place_forget()
    label14.place(relx=.1, rely=.2)
    b15dec4.place(relx=.2, rely=.8)
    b16dec4.place(relx=.6, rely=.8)

def b14_frente():
    nome = e1.get()
    label7.place_forget()
    b13dec3.place_forget()
    b14dec3.place_forget()
    label8.place(relx=.1, rely=.2)
    r2.place(relx=.3, rely=.8)
    r1.place_forget()

def b15_foges():
    nome = e1.get()
    label14.place_forget()
    b15dec4.place_forget()
    b16dec4.place_forget()
    label15.place(relx=.1, rely=.2)
    r2.place(relx=.3, rely=.8)

def b16_esconder():
    nome = e1.get()
    label14.place_forget()
    b15dec4.place_forget()
    b16dec4.place_forget()
    label16.place(relx=.1, rely=.2)
    continue2.place(relx=.3, rely=.8)

def b16_continuar():
    nome = e1.get()
    label16.place_forget()
    continue2.place_forget()
    label17.place(relx=.1, rely=.2)
    b17dec5.place(relx=.2, rely=.8)
    b18dec5.place(relx=.6, rely=.8)

def b17_ignorar():
    nome = e1.get()
    label17.place_forget()
    b17dec5.place_forget()
    b18dec5.place_forget()
    label19.place(relx=.1, rely=.2)
    continue9.place(relx=.3, rely=.8)

def b17_ignorarfinal():
    nome = e1.get()
    label19.place_forget()
    continue9.place_forget()
    label18.place(relx=.1, rely=.2)
    continue3.place(relx=.3, rely=.8)

def b18_bebefinal():
    nome = e1.get()
    label17.place_forget()
    b17dec5.place_forget()
    b18dec5.place_forget()
    label18.place(relx=.1, rely=.2)
    continue3.place(relx=.3, rely=.8)

def b18_continuar():
    messagebox.showinfo("Informação", "Parabéns! Completou a DEMO!\nPara continuar pague a versão Premium!")
    continue3.place_forget()
    r2.place(relx=.3, rely=.8)

def b19_saltar():
    nome = e1.get()
    label20.place_forget()
    b10dec3.place_forget()
    b19dec3.place_forget()
    label21e.place(relx=.1, rely=.2)
    b20dec4.place(relx=.2, rely=.8)
    b21dec4.place(relx=.6, rely=.8)

def b20_sais():
    nome = e1.get()
    label21e.place_forget()
    b20dec4.place_forget()
    b21dec4.place_forget()
    label22.place(relx=.1, rely=.2)
    continue5.place(relx=.3, rely=.8)

def b21_vais():
    nome = e1.get()
    label21e.place_forget()
    b20dec4.place_forget()
    b21dec4.place_forget()
    label23.place(relx=.1, rely=.2)
    continue5.place(relx=.3, rely=.8)

def b20_continuar():
    nome = e1.get()
    continue5.place_forget()
    label22.place_forget()
    label23.place_forget()
    label24.place(relx=.1, rely=.2)
    b22dec5.place(relx=.2, rely=.8)
    b23dec5.place(relx=.6, rely=.8)

def b22_ignorar():
    nome = e1.get()
    label24.place_forget()
    b22dec5.place_forget()
    b23dec5.place_forget()
    label25.place(relx=.1, rely=.2)
    r2.place(relx=.3, rely=.8)

def b23_entras():
    nome = e1.get()
    label24.place_forget()
    b22dec5.place_forget()
    b23dec5.place_forget()
    label26.place(relx=.1, rely=.2)
    b24dec6.place(relx=.2, rely=.8)
    b25dec6.place(relx=.6, rely=.8)

def b24_comes():
    nome = e1.get()
    label26.place_forget()
    b24dec6.place_forget()
    b25dec6.place_forget()
    label27.place(relx=.1, rely=.2)
    continue6.place(relx=.3, rely=.8)

def b24_continuar():
    nome = e1.get()
    label27.place_forget()
    continue6.place_forget()
    label28.place(relx=.1, rely=.2)
    continue7.place(relx=.3, rely=.8)

def b24_parabens():
    nome = e1.get()
    messagebox.showinfo("Informação", "Parabéns! Completou a DEMO!\nPara continuar pague a versão Premium!")
    continue7.place_forget()
    continue8.place_forget()
    r2.place(relx=.3, rely=.8)
    r1.place_forget()

def b25_fome():
    nome = e1.get()
    label26.place_forget()
    b24dec6.place_forget()
    b25dec6.place_forget()
    label27.place(relx=.1, rely=.2)
    continue8.place(relx=.3, rely=.8)

def b25_continuar():
    nome = e1.get()
    label27.place_forget()
    continue6.place_forget()
    label29.place(relx=.1, rely=.2)
    continue8.place_forget()
    continue7.place(relx=.3, rely=.8)

#Root e a sua apresentação


root = Tk()
root.title("Dias de um Futuro Perdido")
root.geometry("600x800")
root.resizable(0, 0)
pygame.init()


#Items da root


root.config(cursor='circle red red')
root.iconbitmap(r"revolveico.ico")
img1 = PhotoImage(file="forest.png")
img2 = PhotoImage(file="back1.png")


#Background


background_label = Label(root, image=img1)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#Entries

nome = StringVar()

e1 = Entry(root, text="Introduza o nome do seu personagem", textvariable= nome, font=("Agency FB", 31, "italic"), borderwidth=3,
           relief="sunken")



#Labels


label1 = Label(root, text="Dias de um Futuro Perdido", font=("Agency FB", 25, "bold italic"), borderwidth=10,
               relief="groove", bg="#6688af", fg="white")
label2 = Label(root, text="Qual é o nome do seu personagem?", font=("Agency FB", 18, "bold italic"), borderwidth=10,
               relief="groove", bg="#6688af", fg="white")


label3 = Label(root, text="Acordas, sobressaltado."
"\nOs teus olhos abrem-se, despertos uma vez mais sob a \nluz que neles incide. Sentes uma dor latejante tomar conta \ndo teu corpo,"
" mas ainda assim tentas-te pôr de pé.\n Cravas os dedos nas raízes que se erguem à tua frente\n e levantas-te, por fim."
" Árvores negras ocupam as \nredondezas, dissimulando o que na escuridão se esconde.\n Ignorando tal receio, inspiras fundo.\n "
"O ar seco da região é reconfortante, de certa forma.\n "
"Contudo, o disparar de uma bala quebra o teu foco,\n apanhando-te desprevenido. "
"O ruído ensurdece-te, \ne tudo se aclara por um breve instante.\n "
"Qual é o teu próximo passo?"


, font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor=N)


label4 = Label(root)


label5 = Label(root, text="Desces pela colina até ao curso de água.\nLá, vês-te encurralado em pouco tempo,\n apercebendo-te da aproximação inevitável do grupo\n armado. "
                          "Atentando nas tuas vestes, reparas no canhão\n  de mão que carregas à cintura, carregado e pronto \na utilizar."
                          " Contemplas ainda a única forma de esconderes\n num lugar daqueles: esperar de baixo de água.\n "
                          "Mas será essa a melhor opção?"
                          , font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor=N)


label6 = Label(root, text="A corrente da água é demasiado forte.\nNum último esforço, tentas subir até à tona da água\n para buscar o ar que tanto te falta, já em vão.\n"
                          "Aceitando o teu destino, deixas o rio levar\n teu corpo inconsciente até à foz onde desagua.\n "
                          "És encontrado morto dias depois."
                          , font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor=N)


label7 = Label(root, text="O caminho montanhoso da floresta acaba por se\n dividir em duas direções diferentes, deixando-te\n com uma escolha apressada por fazer.\n"
                          "Seguirás tu pela frente, ou virarás à direita?"
                          , font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor=N)

label8 = Label(root, text="Escutas o rugir de um animal selvagem.\n Temendo o pior, recuas rapidamente."
                          " Porém, deparas-te\n com um tigre de grande porte, que te ataca com frieza.\n"
                          "És morto no local."
                          , font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor=N)


label9 = Label(root, text="Decides enfrentá-los na hora.\n Ainda assim, e para tua surpresa, apenas dois do \ngrupo de soldados chegam ao local onde os esperas,\n separados da restante formação. "
                          "Avaliando a diferença \n de números, esticas a mão para alcançar a tua arma.\n Contudo, um outro sujeito antecipa-se, baleando os \ndois guardas mortalmente."
                          "O homem aproxima-se\n logo depois para confirmar o abate e aperta o teu braço.\n"
                          " 'Segue-me' – comanda, um pouco nervoso.\n Confuso, decides segui-lo."
                          , font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor=N)


label10 = Label(root)


label11 = Label(root, text="'O presidente deu uma ordem e tu ignoraras-te…\n Dececionaste-me, nome – admite, entristecido.\n "
                           " Movido pelo desabafo, a tua cabeça volta a latejar\n fortemente. "
                           "Em pânico, pressionas as têmporas \nque tanto te magoam, à medida que memórias de um\n passado distante surgem, uma por uma.\n"
                           " Abres os olhos ainda atordoado, apenas para ver o\n teu colega cair já sem vida, alvejado naquele\n compasso de espera. "
                           "Olhas para a direita. \nO chefe do esquadrão tinha chegado."
                          , font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor= N)


label12 = Label(root, text="Puxas o gatilho, sem sucesso.\n "
                           "Ouves algo estalar dentro da tua arma, que explode\n logo depois com um barulho estridente.\n"
                           " Procurando por defesa, pegas na pistola que \no teu amigo carregava. Tudo fica escuro, subitamente.\n"
                           " Uma energia opressora leva-te a cair,\n emanada do canhão de mão pousado no solo.\n "
                           "Momentos depois, os guardas encontram-te\n inconsciente, imóvel junto das árvores que te rodeiam.\n"
                           "O teu fim é ali."
                          , font=("Agency FB", 18, " italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor= N)


label13 = Label(root, text="Corres sem hesitação alguma.\n Despes as vestes de combate com que caminhaste\n até então, tentando atingir uma velocidade maior\n enquanto galgas pela colina abaixo.\n"
                           " Contudo, todo esse esforço revela-se em vão.\n"
                           " Os soldados atingem-te sem grande dificuldade,\n impedindo a tua fuga. "
                           "Arrastas-te pelo chão\n durante uns longos cinco segundos, até que \nés morto por aqueles que te perseguem.\n "
                           "A tua vida chega a um fim."
                          , font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor= N)


label14 = Label(root, text="Encontras um bote, um pouco mais à frente."
                          , font=("Agency FB", 18, " italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor = N)


label15 = Label(root, text="Tentas carregá-lo às costas enquanto executas\n a tua fuga. "
                           "Pesado como é, o bote impede-te de\n prosseguir com rapidez, causado o diminuir\n da distância entre ti e aqueles que te perseguem.\n"
                           "Uma bala é disparada, projetando-te contra\n o chão aquando o impacto contra o teu corpo.\n"
                           "Quando voltas a abrir os olhos, já os guardas te têm \ncercado, prontos para levar a cabo a sua última missão.\n "
                           "Exterminar-te."
                          , font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor= N)


label16 = Label(root, text="Felizmente, os guardas não te veem.\n Passam por ti a toda a velocidade, continuando\n a perseguição fútil pela floresta fora.\n"
                           "Já sem perigo, sais de dentro dele e \nlevas o bote até ao rio, para atravessá-lo."
                          , font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor= N)


label17 = Label(root, text="Já na outra margem, ouves um choro de um bebé.\n "
                           "Rapidamente percebes que se encontra\n próximo de ti, tendo em conta a intensidade do som."
                          , font=("Agency FB", 18, " italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor= N)


label18 = Label(root, text="Encontras o recém-nascido, depois de uma\n procura intensa. ‘Tu…’ – murmuras, ao \n reconhecer o brasão que a criança carrega ao peito.\n"
                           "O teu instinto faz com que tu pegues nele,\n apesar das circunstâncias em que te encontras.\n ‘Até que enfim’ – declara uma outra voz.\n "
                           "Inclinas a cabeça lentamente, assim que a ouves.\n "
                           "Acompanhado por dez homens armados, um senhor\n de meia idade aproxima-se de ti, olhando-te fixamente.\n"
                           " 'Até que enfim, agente. Estávamos à sua espera'."
                          , font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor= N)


label19 = Label(root, text="'Segue a tua missão' – \ngrita uma voz dentro da tua cabeça.\n Sentes uma tontura e cais.\n "
                           "Algo no teu íntimo diz-te para acudires o bebé.\n Seguindo o teu instinto, corres até à sua beira."
                          , font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor= N)


label20 = Label(root, text="Chegas ao fim da linha.\n Vês-te encurralado, sem lugar para onde fugir.\n"
                           " Por baixo de ti, existe apenas o rio.\n "
                           "Passo a passo, os agressores aproximam-se de ti,\n enquanto tu te questionas sobre o que fazer de seguida.\n"
                           " Seria uma queda daquela altura mortal?"
                          , font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor= N)


label21 = Label(root, text="Por detrás de uma árvore, ouves os guardas\n conversarem entre si:\n "
                           "'Ele é um assassino treinado, ajam com precaução'.\n"
                           " Impaciente, moves-te por entre os arbustos de\n forma a ouvir melhor a discussão.\n "
                           "Durante o processo, porém, calcas um galho."
                          , font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor= N )

label21e = Label(root, text="Saltas para o rio com confiança.\n O impacto é intenso, deixando-te inconsciente\n por um breve instante."
                            " Notas que a corrente é forte,\n especialmente nas profundezas do leito onde te encontras."
                          , font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor= N )

label22 = Label(root, text="Não encontras força suficiente para \nsubir até à tona. "
                           "Ao invés de lutar contra\n o inevitável, deixas as águas \nlevarem-te até à entrada de uma gruta escura,\n"
                           " onde o rio parece continuar já com menos profundidade."

                          ,font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor= N )

label23 = Label(root, text="Aceitando o inevitável, deixas as águas\n levarem-te até à entrada de uma gruta escura,\n "
                           "onde o rio parece continuar já com menos profundidade."
                            , font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor = N )


label24 = Label(root, text="A gruta é grande e húmida.\n O ar dentro dela, por sua vez, é seco e agradável.\n"
                           " Ficas indeciso entre ignorá-la continuando\n pela floresta ou explorar o desconhecido."
                            , font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor = N )


label25 = Label(root, text="Escutas o rugir de um animal selvagem.\n Temendo o pior, recuas rapidamente."
                           " Porém, deparas-te\n com um leão de grande porte, que te ataca com frieza.\n"
                           "És morto no local."
                          , font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor = N)


label26 = Label(root, text="Encontras fruta logo depois da entrada.\n São uvas. Têm uma textura\n estranha e um sabor ácido."
                          , font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor= N)

label27 = Label(root, text="Segues em frente até ao fim da caverna.\n Lá, uma luz parece ter lugar."
                          , font=("Agency FB", 18, "italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor = N )

label28 = Label(root)

label29 = Label(root, text="'Até que enfim' – declara uma outra voz.\n Inclinas a cabeça lentamente, assim \nque a ouves. As lanternas dos guardas revelam-se\n de uma vez só."
                           " Acompanhado por dez homens armados,\n um senhor de meia idade aproxima-se de ti,\n olhando-te fixamente.\n"
                           " 'Até que enfim, agente. Estávamos à sua espera'."
                          , font=("Agency FB", 18, " italic"), borderwidth=10, relief="groove", bg="#8a9a91", fg="white", anchor= N )




#Botões ocasionais


r1 = Button(root, image=img2, borderwidth=3, relief="raised", command=voltar_menu)

r2 = Button(root, text="Voltar ao menu", bg="#aa5850", command=voltar_menu, borderwidth=7, relief="raised",
            font=("Agency FB", 22, "italic"), fg="white" )
continue1 = Button(root, text="Continuar", bg="#8291a2", command=b10_continuar, borderwidth=7, relief="raised",
            font=("Agency FB", 22, "italic"), fg="white" )
continue2 = Button(root, text="Continuar", bg="#8291a2", command= b16_continuar, borderwidth=7, relief="raised",
            font=("Agency FB", 22, "italic"), fg="white" )
continue3 = Button(root, text="Continuar", bg="#8291a2", command= b18_continuar, borderwidth=7, relief="raised",
            font=("Agency FB", 22, "italic"), fg="white" )
continue4 = Button(root, text="Continuar", bg="#8291a2", command= b4_fugir, borderwidth=7, relief="raised",
            font=("Agency FB", 22, "italic"), fg="white")
continue5 = Button(root, text="Continuar", command= b20_continuar, bg="#8291a2", borderwidth=7, relief="raised",
            font=("Agency FB", 22, "italic"), fg="white")
continue6 = Button(root, text="Continuar", command= b24_continuar, bg="#8291a2", borderwidth=7, relief="raised",
            font=("Agency FB", 22, "italic"), fg="white")
continue7 = Button(root, text="Continuar", command= b24_parabens, bg="#8291a2", borderwidth=7, relief="raised",
            font=("Agency FB", 22, "italic"), fg="white")
continue8 = Button(root, text="Continuar", command= b25_continuar, bg="#8291a2", borderwidth=7, relief="raised",
            font=("Agency FB", 22, "italic"), fg="white")
continue9 = Button(root, text="Continuar", command= b17_ignorarfinal, bg="#8291a2", borderwidth=7, relief="raised",
            font=("Agency FB", 22, "italic"), fg="white")
org = Button(root, text="'Organização?'", bg="#8291a2", command=b10_org, borderwidth=7, relief="raised",
            font=("Agency FB", 22, "italic"), fg="white" )
retry1= Button(root, text="Tentar novamente", bg="#8291a2", command=b3_começar, borderwidth=7, relief="raised",
            font=("Agency FB", 22, "italic"), fg="white" )
explore = Button(root, text="Explorar", bg="#8291a2", command=b3_começar, borderwidth=7, relief="raised",
            font=("Agency FB", 22, "italic"), fg="white" )

#Botões de decisão


b1 = Button(root, text="Jogar", bg="#8291a2", command=b1_jogar, borderwidth=7, relief="raised",
            font=("Agency FB", 20, "italic"), fg="white")
b2 = Button(root, text="Sair", bg="#8291a2", command=root.quit, borderwidth=7, relief="raised",
            font=("Agency FB", 20, "italic"), fg="white")
b3 = Button(root, text="Começar", bg="#8291a2", command=b3_começar, borderwidth=7, relief="raised",
            font=("Agency FB", 20, "italic"), fg="white")
b4dec1 = Button(root, text="Fugir", bg="#8291a2", command= b4_fugir, borderwidth=7, relief="raised",
            font=("Agency FB", 20, "italic"), fg="white" )
b5dec1 = Button(root, text="Esconder", bg="#8291a2", command= besconder_1, borderwidth=7, relief="raised",
            font=("Agency FB", 20, "italic"), fg="white" )
b6dec2 = Button(root, text="Rio", bg="#8291a2", command= b6_rio, borderwidth=7, relief="raised",
            font=("Agency FB", 20, "italic"), fg="white" )
b7dec2 = Button(root, text="Floresta", command= b7_floresta, bg="#8291a2", borderwidth=7, relief="raised",
            font=("Agency FB", 20, "italic"), fg="white" )
b8dec2 = Button(root, text="Precipício", command= b8_precipicio, bg="#8291a2", borderwidth=7, relief="raised",
            font=("Agency FB", 20, "italic"), fg="white" )
b9dec3 = Button(root, text="Suster Respiração", bg="#8291a2", command= b9_suster, borderwidth=7, relief="raised",
            font=("Agency FB", 17, "italic"), fg="white")
b10dec3 = Button(root, text="Enfrentar", command= b10_enfrentas, bg="#8291a2", borderwidth=7, relief="raised",
            font=("Agency FB", 20, "italic"), fg="white" )
b11dec4 = Button(root, text="Enfrentas", command= b11_arma, bg="#8291a2", borderwidth=7, relief="raised",
            font=("Agency FB", 20, "italic"), fg="white" )
b12dec4 = Button(root, text="Foges", bg="#8291a2", borderwidth=7, relief="raised",
            font=("Agency FB", 20, "italic"), command= b11_fugir, fg="white" )
b13dec3 = Button(root, text="Direita", command= b13_direita, bg="#8291a2", borderwidth=7, relief="raised",
            font=("Agency FB", 20, "italic"), fg="white" )
b14dec3 = Button(root, text="Sempre em frente", bg="#8291a2", command= b14_frente, borderwidth=7, relief="raised",
            font=("Agency FB", 17, "italic"), fg="white")
b15dec4 = Button(root, text="Foges", bg="#8291a2", command= b15_foges, borderwidth=7, relief="raised",
            font=("Agency FB", 20, "italic"), fg="white" )
b16dec4 = Button(root, text="Escondes-te dentro dele", bg="#8291a2", command= b16_esconder, borderwidth=7, relief="raised",
            font=("Agency FB", 16, "italic"), fg="white" )
b17dec5 = Button(root, text="Ignoras", bg="#8291a2", command= b17_ignorar, borderwidth=7, relief="raised",
            font=("Agency FB", 20, "italic"), fg="white" )

b18dec5 = Button(root, text="Procuras pelo bebé", bg="#8291a2", command= b18_bebefinal, borderwidth=7, relief="raised",
            font=("Agency FB", 17, "italic"), fg="white" )
b19dec3 = Button(root, text="Saltas para o rio", bg="#8291a2", command= b19_saltar, borderwidth=7, relief="raised",
            font=("Agency FB", 19, "italic"), fg="white" )
b20dec4 = Button(root, text="Sais do rio", bg="#8291a2", command= b20_sais, borderwidth=7, relief="raised",
            font=("Agency FB", 20, "italic"), fg="white" )
b21dec4 = Button(root, text="Deixas-te ir", command= b21_vais, bg="#8291a2", borderwidth=7, relief="raised",
            font=("Agency FB", 20, "italic"), fg="white" )
b22dec5 = Button(root, text="Ignorar", command= b22_ignorar, bg="#8291a2", borderwidth=7, relief="raised",
            font=("Agency FB", 20, "italic"), fg="white" )
b23dec5 = Button(root, text="Entras na gruta", bg="#8291a2", command= b23_entras, borderwidth=7, relief="raised",
            font=("Agency FB", 20, "italic"), fg="white" )
b24dec6 = Button(root, text="Comer as uvas", bg="#8291a2", command= b24_comes, borderwidth=7, relief="raised",
            font=("Agency FB", 20, "italic"), fg="white" )
b25dec6 = Button(root, text="Não comer", command= b25_fome, bg="#8291a2", borderwidth=7, relief="raised",
            font=("Agency FB", 20, "italic"), fg="white" )




#Configuração de botões


r1.config(height=22, width=30)
r2.config(padx= 38)
continue1.config(padx= 60)
retry1.config(padx=20)
b1.config(height=1, width=26)
b2.config(height=1, width=26)
b3.config(height=1, width=18, padx=17)
b4dec1.config(padx=20)
b5dec1.config()
b6dec2.config(padx= 30)
b7dec2.config(padx= 6)
b8dec2.config(padx= 5)
b9dec3.config(pady= 7, padx= 3)
b10dec3.config(padx= 20, pady= 2)
b13dec3.config(padx= 40)
b14dec3.config(pady = 4)
org.config(padx = 35)
b11dec4.config(padx= 20)
b12dec4.config(padx=30)
b15dec4.config(padx=50)
b16dec4.config(pady= 6)
b17dec5.config(padx=40)
b18dec5.config(pady=5)
b10dec3.config(padx=25)
b19dec3.config(pady=5)
b20dec4.config(padx=7)
b21dec4.config()
b22dec5.config(padx=30)
b23dec5.config()
b24dec6.config()
b25dec6.config(padx=20)
continue2.config(padx= 60)
continue3.config(padx= 60)
continue4.config(padx= 60)
continue5.config(padx= 60)
continue6.config(padx= 60)
continue7.config(padx= 60)
continue8.config(padx= 60)
continue9.config(padx= 60)


#Configuração de labels


label1.config(height=2, width=30, padx=1)
label2.config(height=2, width=26, padx=50)
label3.config(height=13, width=50, pady= 10)
label5.config(height=8, width=50, pady=10)
label6.config(height=7, width=50, pady=10)
label7.config(height=4, width=45, pady=15, padx= 30)
label8.config(height=4, width=50, pady=10)
label9.config(height=10, width=50, pady= 10)
label11.config(height=10, width=50, pady= 10)
label12.config(height=10, width=50, pady= 10)
label13.config(height=10, width=50, pady= 10)
label14.config(height=1, width=50, pady=10, padx=20)
label15.config(height=9, width=50, pady= 10)
label16.config(height=5, width=50, pady= 10)
label17.config(height=3, width=50, pady= 10)
label18.config(height=10, width=50, pady= 10)
label19.config(height=5, width=50, pady= 10)
label20.config(height=6, width=50, pady= 10)
label21.config(height=6, width=50, pady= 10)
label21e.config(height=4, width=50, pady= 10)
label22.config(height=5, width=50, pady= 10)
label23.config(height=3, width=50, pady= 10)
label24.config(height=4, width=50, pady= 10)
label25.config(height=4, width=50, pady= 10)
label26.config(height=3, width=50, pady= 10)
label27.config(height=2, width=50, pady= 10)
label29.config(height=7, width=50, pady= 10)


#Placement dos botões e label iniciais



b1.place(relx=.3, rely=.7)
b2.place(relx=.3, rely=.8)
label1.place(relx=.2, rely=.2)






root.mainloop()

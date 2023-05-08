import requests
from bs4 import BeautifulSoup

url = 'https://agrosmart.com.br/blog/como-classificar-os-tipos-de-solo-da-lavoura/'
source_code = requests.get (url)
plain_text = source_code.text #Recolhimento informações
soup = BeautifulSoup(plain_text, 'html.parser') #Deixando as informações bonitas e de bom entendimento 
data1 = soup.find_all('ul') 




while True:
    print('---Selecione seu tipo de solo---')
    print('-'*10)
    print(' 1 - \033[1;33mArgissolo\033[m \n 2 - \033[1;31mLatossolo\033[m \n 3 - \033[1;35mCambissolo\033[m \n 4 - \033[1;32mNeossolo\033[m')
    solo = int(input(' -> '))
    #Primeiro tipo de solo
    if solo == 1:    
        h3 = soup.find_all('h3')
        titulo = h3[0].text
        print(f"\033[1;33m{titulo}:\033[m")
        ta = data1[7]
        resultado = ta.text
        # Transforma a lista em uma string separada por ""
        resultado_str = "".join(resultado)
        # Substitui ";" por "\n" para quebrar em linhas
        resultado_formatado = resultado_str.replace(";", "\n - ")
        print(' -', resultado_formatado)

    #Segundo tipo de solo
    elif solo == 2: 
        h3 = soup.find_all('h3')
        titulo = h3[1].text
        print(f"\033[1;31m{titulo}:\033[m")
        ta = data1[8]
        resultado = ta.text
        # Transforma a lista em uma string separada por ""
        resultado_str = "".join(resultado)
        # Substitui ";" por "\n" para quebrar em linhas
        resultado_formatado = resultado_str.replace(";", "\n - ")
        print(' -', resultado_formatado)

    #Terceiro tipo de solo
    elif solo == 3:
        h3 = soup.find_all('h3')
        titulo = h3[2].text
        print(f"\033[1;35m{titulo}:\033[m")
        ta = data1[9]
        resultado = ta.text
        # Transforma a lista em uma string separada por ""
        resultado_str = "".join(resultado)
        # Substitui ";" por "\n" para quebrar em linhas
        resultado_formatado = resultado_str.replace(";", "\n - ")
        print(' -', resultado_formatado)


    #Quarto tipo de solo
    elif solo == 4:
        h3 = soup.find_all('h3')
        titulo = h3[3].text
        print(f"\033[1;32m{titulo}:\033[m")
        ta = data1[10]
        resultado = ta.text
        # Transforma a lista em uma string separada por ""
        resultado_str = "".join(resultado)
        # Substitui ";" por "\n" para quebrar em linhas
        resultado_formatado = resultado_str.replace(";", "\n - ")
        print(' -', resultado_formatado)

    else:
        print('\033[1;31mOpção inválida\033[m')

    continuar = str(input('Deseja continuar? Digite <S> para \033[1;32msim\033[m ou Digite <N> para \033[1;31mnão\033[m -> '))

    if continuar == 's'or continuar == 'S':
        continue
    elif continuar == 'n' or continuar == 'N':
        print('Tchau')
        break
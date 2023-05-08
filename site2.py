import requests
from bs4 import BeautifulSoup

url = 'https://boaspraticasagronomicas.com.br/artigos/tipos-de-solo/'

response = requests.get(url)

html = response.content

soup = BeautifulSoup(html, 'html.parser')

div_especifica = soup.find('div', {'class': 'mes_blog_item_main_content'})

# encontre todos os elementos h3 dentro da div
elementos_h3 = div_especifica.find_all('h3')

for indice, h3 in enumerate(elementos_h3, start=-3):
    texto = h3.text.strip()
    if texto != "Areia" and texto != "Silte" and texto != "Argila":
        print(f"{indice}. {texto}")

pergunta = input("Qual tipo de solo você deseja saber mais? ")

if pergunta == "0":
  
    h3_argissolos = div_especifica.find('h3', string='Argissolos')
    p_argissolos = h3_argissolos.find_next_sibling('p')
    texto_argissolos = p_argissolos.text.strip()
    p_argissolos = p_argissolos.find_next_sibling('p')
    texto_argissolos_2 = p_argissolos.text.strip()

    print('Argissolos: ',texto_argissolos, texto_argissolos_2)

elif pergunta == "1":
    h3_Cambissolos = div_especifica.find('h3', string='Cambissolos')
    p_Cambissolos = h3_Cambissolos.find_next_sibling('p')
    texto_Cambissolos = p_Cambissolos.text.strip()
    print('Cambissolos: ',texto_Cambissolos)

elif pergunta == "2":
    h3_Chernossolos = div_especifica.find('h3', string='Chernossolos')
    p_Chernossolos = h3_Chernossolos.find_next_sibling('p')
    texto_Chernossolos = p_Chernossolos.text.strip()
    p_Chernossolos = p_Chernossolos.find_next_sibling('p')
    texto_Chernossolos_2 = p_Chernossolos.text.strip()
    print('Chernossolos: ',texto_Chernossolos)

elif pergunta == "3":
    h3_Espodossolos = div_especifica.find('h3', string='Espodossolos')
    p_Espodossolos = h3_Espodossolos.find_next_sibling('p')
    texto_Espodossolos = p_Espodossolos.text.strip()
    p_Espodossolos = p_Espodossolos.find_next_sibling('p')
    texto_Espodossolos_2 = p_Espodossolos.text.strip()
    
    print('Espodossolos: ',texto_Espodossolos, texto_Espodossolos_2)

elif pergunta == "4":
    h3_Gleissolos = div_especifica.find('h3', string='Gleissolos')
    p_Gleissolos = h3_Gleissolos.find_next_sibling('p')
    texto_Gleissolos = p_Gleissolos.text.strip()
    p_Gleissolos = p_Gleissolos.find_next_sibling('p')
    texto_Gleissolos_2 = p_Gleissolos.text.strip()
    print('Gleissolos: ',texto_Gleissolos, texto_Gleissolos_2)

elif pergunta == "5":
    h3_Latossolos = div_especifica.find('h3', string='Latossolos')
    p_Latossolos = h3_Latossolos.find_next_sibling('p')
    texto_Latossolos = p_Latossolos.text.strip()
    print('Latossolos: ',texto_Latossolos)

elif pergunta == "6":
    h3_Luvissolos = div_especifica.find('h3', string='Luvissolos')
    p_Luvissolos = h3_Luvissolos.find_next_sibling('p')
    texto_Luvissolos = p_Luvissolos.text.strip()
    print('Luvissolos: ',texto_Luvissolos)

elif pergunta == "7":
    h3_Neossolos = div_especifica.find('h3', string='Neossolos')
    p_Neossolos = h3_Neossolos.find_next_sibling('p')
    texto_Neossolos = p_Neossolos.text.strip()
    print('Neossolos: ',texto_Neossolos)

elif pergunta == "8":
    h3_Nitossolos = div_especifica.find('h3', string='Nitossolos')
    p_Nitossolos = h3_Nitossolos.find_next_sibling('p')
    texto_Nitossolos = p_Nitossolos.text.strip()
    p_Nitossolos = p_Nitossolos.find_next_sibling('p')
    texto_Nitossolos_2 = p_Nitossolos.text.strip()
    print('Nitossolos: ',texto_Nitossolos, texto_Nitossolos_2)

elif pergunta == "9":
    h3_Organossolos = div_especifica.find('h3', string='Organossolos')
    p_Organossolos = h3_Organossolos.find_next_sibling('p')
    texto_Organossolos = p_Organossolos.text.strip()
    p_Organossolos = p_Organossolos.find_next_sibling('p')
    texto_Organossolos_2 = p_Organossolos.text.strip()
    print('Organossolos: ',texto_Organossolos, texto_Organossolos_2)

elif pergunta == "10":
    h3_Planossolo = div_especifica.find('h3', string='Planossolo')
    p_Planossolo = h3_Planossolo.find_next_sibling('p')
    texto_Planossolo = p_Planossolo.text.strip()
    print('Planossolo: ',texto_Planossolo)

elif pergunta == "11":
    h3_Plintossolos = div_especifica.find('h3', string='Plintossolos')
    p_Plintossolos = h3_Plintossolos.find_next_sibling('p')
    texto_Plintossolos = p_Plintossolos.text.strip()
    p_Plintossolos = p_Plintossolos.find_next_sibling('p')
    texto_Plintossolos_2 = p_Plintossolos.text.strip()
    p_Plintossolos = p_Plintossolos.find_next_sibling('p')
    texto_Plintossolos_3 = p_Plintossolos.text.strip()
    print('Plintossolos: ',texto_Plintossolos, texto_Plintossolos_2, texto_Plintossolos_3)

elif pergunta == "12":
    h3_Vertissolos = div_especifica.find('h3', string='Vertissolos')
    p_Vertissolos = h3_Vertissolos.find_next_sibling('p')
    texto_Vertissolos = p_Vertissolos.text.strip()
    p_Vertissolos = p_Vertissolos.find_next_sibling('p')
    texto_Vertissolos_2 = p_Vertissolos.text.strip()
    print('Vertissolos: ',texto_Vertissolos, texto_Vertissolos_2)
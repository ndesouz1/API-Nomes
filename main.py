#https://servicodados.ibge.gov.br/api/docs/censos/nomes?versao=2
# Coletados pela primeira vez no Censo 2010, informa a frequência dos nomes por década de nascimento
#$ python3 main.py
import requests 
import json

def main():

    print("################################")
    print("####Popularidade dos Nomes######")
    print("################################")
    print()

    nome_input = input('Digite o nome a ser pesquisado: ')
    
    if len(nome_input) < 3:
        print("Quantidade de dígitos inválida!")
        exit()

    request = requests.get('https://servicodados.ibge.gov.br/api/v2/censos/nomes/{}'.format(nome_input))

    print(request.json())

    nome_data = request.json()

    if 'erro' not in nome_data:
        print('==> Nome Encontrado <==')

    else:
        print("{}: Nome invalido.".format(nome_input))    

    print("---------------------------------------")
    
    option = int(input('Deseja realizar uma nova consulta ?\n1. Sim\n2. Não\n'))
    if option == 1:
        main()
    else:
        print('Saindo da consulta...')   

if __name__ == "__main__":
    main()     

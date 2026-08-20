import requests

resposta = requests.get("https://portal.drugovich.com.br/api/funcionarioErp/adelso.godoi")


arquivo = open("tests.txt", "w")
arquivo.write(resposta.text)
arquivo.close()

print(resposta.text)



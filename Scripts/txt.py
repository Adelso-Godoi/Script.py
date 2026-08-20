print("Aprendendo a escrever em um arquivo .txt")

hosts = []


def solicita():

    hostname = input("Digite seu hostname: ")
    if hostname in hosts:
        print("Host já cadastrado")
        return

    hosts.append(hostname)


while True:

    print("""
1 - Adicionar Host
2 - Sair
""")

    op = int(input("Digite a sua opção: "))

    if op == 1:

        while True:
            solicita()

            valida = input("Deseja inserir um novo host? (S/N): ").upper()

            if valida == "N":

                arquivo = open("arquivo.txt", "a") # parametro "w" cria um arquivo e sobrescreve, parametro "a" apenas acrescenta linhas a mais sem sobrescrever.

                for valores in hosts:
                    arquivo.write(valores + "\n")

                arquivo.close()

                print("Hosts salvos no arquivo!")

                break

    elif op == 2:
        print("Saindo...")
        break
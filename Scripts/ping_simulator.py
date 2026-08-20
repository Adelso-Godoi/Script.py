print("+++++++++++++++++++")
print("PING SIMULATOR"  "  +++")
print("+++++++++++++++++++")


hosts = [] # Lista hosts

def solicita():

    hostname = input("Digite seu hostname: ")
    if hostname in hosts:
            print("Host já cadastrado")
            return
    hosts.append(hostname) #incluindo valor da variavel em lista ( list )



def listar_serv():
      print("Os servidores da lista são: ")
      for hostname in hosts:
           print(hostname)
           

def testar_s():
     nom = input("Digite o servidor para teste: ")
     if nom not in hosts:
          print("Servidor não encontrado!")
     else:
          print("Testando conexão ...")
          print("Servidor ONLINE!")

      
def remover_host():
    hostname = input("Digite o hostname para remover: ")

    if hostname in hosts:
        hosts.remove(hostname) #Remover o valor da variável hostname na lista hosts
        print("Host removido!")
    else:
        print("Servidor não encontrado")



while True:

    print("""
1 - Adicionar Host
2 - Listar Hosts
3 - Testar servidor
4 - Remover servidor
5 - Sair
""")

    op = int(input("Digite a sua opção: "))

    if op == 1:

        while True:
            solicita()
            valida = input("Deseja inserir um novo host? (S/N): ").upper()

            if valida == "N":
                break

    elif op == 2:
         listar_serv()
    

    elif op == 3:
         testar_s()

    elif op == 4:
         remover_host()    

    elif op == 5:
         print("saindo")
         break
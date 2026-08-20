

hosts = []



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
           
           



while True:

    print("""
1 - Adicionar Host
2 - Listar Hosts
3 - Sair
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
         print("saindo")
         break
    


    
      
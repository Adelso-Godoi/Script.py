print("==========================")
print("Validador de Hosts")
print("==========================")

hosts = {} #Dicionário hosts


def solicita():

    hostname = input("Digite seu hostname: ")
    if hostname in hosts:
            print("Host já cadastrado")
            return
    ip = input("Digite o IP: ")
    status = input("Digite o status: ")

    hosts[hostname] = {
        "ip": ip,
        "status": status
    }

 
def lista_dic():
    print(f"{hosts}")

    
    for hostname, dados in hosts.items():
         if dados["status"] != "ON" or "ONLINE" or "Online" or "On":
            
            print("Servidores Offline: ")

            print(hostname)

      
def remover_host():
    hostname = input("Digite o hostname para remover: ")

    if hostname in hosts:
        del hosts[hostname]
        print("Host removido!")
    else:
        print("Host não encontrado")

def alter_status():

    hostname = input("Digite o hostname para alterar o status: ")
    if hostname not in hosts:
        print("Hostname existe! ")
        return
    elif hostname in hosts:
        print(f'{hostname} { hosts[hostname]["status"]}')
        novo_status = input("Digite o novo status: ")
        
        hosts[hostname]["status"] = novo_status
        
        print("Status alterado com sucesso!")
    else:
        print("Opção inválida")

while True:

    print("""
1 - Adicionar Host
2 - Listar Hosts
3 - Remover Host
4 - Alterar Status
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

        print("Segue a lista dos dados")
        lista_dic()

    elif op == 3:
        remover_host()

    elif op == 4:
        alter_status()
  

    elif op == 5:

        print("Saindo...")
        break
   
    else:

        print("Opção inválida")
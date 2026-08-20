


hostname = input("Digite o nome do server: " )
ip = int(input("Digite o IP: "))

valid = input(" O servidor está online? (S/N) ")

if valid == "S":
    print(f"Servidor{hostname} {ip} está ONLINE")

else:
    print(f"Servidor{hostname} {ip} está Offline")
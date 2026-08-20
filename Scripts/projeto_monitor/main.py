
import subprocess

def consult_serv(serv):
    result = subprocess.run(["systemctl", "is-active",
        serv],
        capture_output=True,
        text=True,
        
    )
    return result
print("Monitor de serviço Linux")

servico = input("Digite o nome do serviço: ")

resul = consult_serv(servico)
resultado = resul.stdout.strip()
if resultado == "active":
    print("Serviço ativo")
else:
    print("Serviço parado")

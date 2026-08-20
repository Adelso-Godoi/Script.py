print("")

import subprocess

def total_disco(total, usado):
    sobra = total - usado
    return sobra

def verificar_status(livre):
    if livre <= 100:
        return "O servidor está crítico!"
    else:
        return "OK"
    
disc = int(input("Digite o valor total do disco: "))
use = int(input("Digite o valor usado do disco: "))

result = total_disco(disc, use)
status = verificar_status(result)

print(f"O espaço livre de disco {result}GB")
print(f"status: {status}")

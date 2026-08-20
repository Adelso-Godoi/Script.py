
import subprocess

def restart_servico():
    result = subprocess.run(
        ["zmproxyctl", "restart"],
        capture_output=True,
        text=True,
        
    )
    return result


def verif_memory():
    result1 = subprocess.run(
        ["free", "-m"],
        capture_output=True,
        text=True,
        
    )
    return result1

def write_text():
    arquivo = open("arquivo.txt", "a")
    arquivo.write("Seviço reiniciado com sucesso! " )
    arquivo.close()


    print("")

def dispara_tel(): #Avaliar possibilidade
    print("")

resultado = verif_memory()
linhas = resultado.stdout.splitlines()
for linha in linhas:
    if "Mem" in linha:
        memo = linha.split()
        total = int(memo[1])
        usado = int(memo[2])
        disponivel = int(memo[6])
        if disponivel <= (total * 0.10):
         write_text()
        else:
            arq = open("arquivo.txt", "a")
            arq.write("Memoria OK")
            arq.close()

        

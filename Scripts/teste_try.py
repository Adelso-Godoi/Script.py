print("Teste do try")

import subprocess

try:

    result = subprocess.run(
        ["systemctl", "status", "ssh"],
        capture_output=True,
        text=True,
        check=True
    )

    print("Comando executado com sucesso! ")
    linhas = result.stdout.splitlines() #splitlines() cria uma lista
    for linha in linhas[:5]: # percore a variavel "linha" criada pelo for na lista linhas, e o "[:5]:" exibe as primeiras 5 linhas
        print(linha)

except:
    print("Erro ao executar o comando.")

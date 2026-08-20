print("Inspetor de processos!")

import subprocess



try:
    result = subprocess.run(["ps", "aux"], capture_output=True, text=True, check=True)
    linhas = result.stdout.splitlines()
    
    # Criamos uma variável para controlar se achamos algo
    encontrou_python = False

    for linha in linhas:
        # Corrigido: sem os colchetes e com .lower()
        if "python" in linha.lower():
            print(f"Processo python encontrado: {linha}")
            encontrou_python = True # Mudamos o status para Verdadeiro

    # Só agora, DEPOIS que o for olhou todas as linhas, fazemos o teste final
    if not encontrou_python:
        print("Nenhum processo python encontrado no sistema.")

except subprocess.CalledProcessError as e:
    print(f"Erro encontrado, código: {e.returncode}")
except FileNotFoundError:
    print("Comando não existe")
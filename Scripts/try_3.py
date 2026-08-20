print("Verificador de conectividade")

import subprocess

try:
    result = subprocess.run(
        ["ping", "-c", "3", "google.com"],
        capture_output=True,
        text=True,
        check=True
    )

    print("Servidor Online!")
    
    # Pegamos todas as linhas em uma lista
    linhas = result.stdout.splitlines()
    
    # Mostramos apenas a última linha da lista usando [-1]
    print(linhas[-1])

except subprocess.CalledProcessError as e: 
    # Agora usamos o 'e' corretamente para capturar os dados do erro
    print(f"Erro ao executar o comando. Código de saída: {e.returncode}")
    print(f"Mensagem de erro do sistema: {e.stderr}")
except FileNotFoundError:
    print("O comando 'ping' não foi encontrado no seu sistema!")
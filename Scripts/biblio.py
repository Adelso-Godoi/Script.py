print("Importando biblioteca subprocess")

import subprocess

result = subprocess.run(  # Pegunta o hostname, captura em modo de texto
    ["hostname"],
    capture_output=True,
    text=True
)

resultado = result.returncode

if resultado == 0:
    print("Comando executado com sucesso!")
    print(f"O hostname dessa máquina é:  {result.stdout.strip()}")
# print(f"O hostname dessa máquina é: {result.returncode}") # strip() remove espaços e quebras de linha do inicio ao fim da string.


#print("Importando biblioteca subprocess")

#import subprocess

#result = subprocess.run(  # Pegunta o hostname, captura em modo de texto
 #   ["ls", "/diretorio_que_nao_existe"],
  #  capture_output=True,
   # text=True
#)

#print(f"O hostname dessa máquina é: {result.returncode}") # Returncode retorna o código da execução.
#print(result.stderr)
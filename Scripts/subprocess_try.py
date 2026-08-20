import subprocess

try:

    result = subprocess.run(
        ["hostnaame"],
        capture_output=True,
        text=True,
        check=True
    )

    print(result.stdout)

except:
    print("Erro ao executar o comando.")
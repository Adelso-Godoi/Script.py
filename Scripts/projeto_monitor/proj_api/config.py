import paramiko

def restart():

    ssh = None

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(
            "172.16.206.245",
            username="infra",
            password="senha",
            timeout=10
        )

        stdin, stdout, stderr = ssh.exec_command(
            "su - zimbra -c 'zmproxyctl restart'"
        )

        resultado = stdout.read().decode()
        erro = stderr.read().decode()

        if erro:
            return {
                "status": "falha",
                "mensagem": erro
            }

        return {
            "status": "sucesso",
            "mensagem": resultado
        }

    except Exception as e:
        return {
            "status": "erro",
            "mensagem": str(e)
        }

    finally:
        if ssh:
            ssh.close()
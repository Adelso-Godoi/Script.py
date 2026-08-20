import paramiko

def restart():

    ssh = None

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(
            "100.160.000.000",
            username="root",
            password="123456",
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

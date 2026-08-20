import subprocess

def consult_serv(serv):
    result = subprocess.run(["systemctl", "is-active",
        serv],
        capture_output=True,
        text=True,
        check=True
    )
    return result




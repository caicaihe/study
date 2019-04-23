#远程监测OOM
import paramiko
import logging

#config
IP = {'192.168.129.40':'caicloud2019-qa4','192.168.129.43':'caicloud2019-qa2'}
PORT = 22
USER = 'root'
OOMCOM = 'kubectl describe pod --all-namespaces |grep -C 100 \'OOMKilled\' -i'

#loging
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("day2/OOM.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


for key in IP:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 跳过了远程连接中选择‘是’的环节,
    ssh.connect(key, 22, USER, IP[key])
    stdin, stdout, stderr = ssh.exec_command(OOMCOM)
    respones = stdout.read()
    if  respones == b'':
        mess = "OOM status health"
    else:
        mess = respones
    print(mess)
    logger.info(mess)
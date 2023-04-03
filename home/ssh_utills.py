from paramiko import SSHClient, AutoAddPolicy
from rich import print, pretty, inspect
import os
import sys
from datetime import datetime
pretty.install()


class sshUtils:
    def __init__(self, host, user, password):
        self.client = SSHClient()
        self.host = host
        self.user = user
        self.password = password

        # LOAD HOST KEYS
        if sys.platform.startswith("linux"):
            self.client.load_host_keys('~/.ssh/known_hosts')
        elif sys.platform == "darwin":
            self.client.load_host_keys('~/.ssh/known_hosts')
        elif sys.platform == "win32":
            self.client.load_host_keys(
                f"{os.path.expanduser( '~' )}/.ssh/known_hosts")

        self.client.load_system_host_keys()
        # Known_host policy
        self.client.set_missing_host_key_policy(AutoAddPolicy())

        # client.connect('10.1.1.92', username='root', password='password1')
        self.client.connect(host, username=user, password=password)

    def execute(self, command, sudo=False):
        feed_password = False
        start_time = datetime.now()
        if sudo and self.user != "root":
            command = "sudo -S -p '' %s" % command
            feed_password = self.password is not None and len(
                self.password) > 0
        stdin, stdout, stderr = self.client.exec_command(command)
        if feed_password:
            stdin.write(self.password + "\n")
            stdin.flush()
        exec_time = datetime.now()-start_time
        return {'out': stdout.read().decode("utf8"),
                'err': stderr.read().decode("utf8"),
                'code': stdout.channel.recv_exit_status(),
                "execTime": exec_time.total_seconds() * 10**3
                }

    def closeSSH(self):
        # Close the client itself
        self.client.close()


util = sshUtils("raspberrypi.local", "tirthapi", "983221")
response = util.execute("sudo ls", sudo=True)
print(response["out"])
print(response["err"])
print(response["code"])
print(response["execTime"])

util.closeSSH()

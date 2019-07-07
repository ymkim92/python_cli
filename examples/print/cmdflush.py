#!/usr/bin/env python3

import cmd2
import paramiko
from subprocess import Popen, PIPE

host_address = 'localhost'
host_user = 'ykim'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class App(cmd2.Cmd):
    def do_local_command(self, arg):
        command = './print.sh'
        self.run_local_command(command)

    def do_ssh_command(self, arg):
        folder = '/home/ykim/Dropbox/dev/python/cmd2/examples/print/'
        command = 'print.sh'
        self.connect_ssh(host_address, host_user)
        self.run_ssh_command(folder+command)

    def run_local_command(self, command):
        output = ''
        self.poutput(command, color=bcolors.OKGREEN)
        p = Popen(command, stdout=PIPE, stderr=PIPE)
        if 0:
            for line in p.stdout:
                buf = line.decode()
                self.poutput(buf, end='')
                output += buf
        else:
            for char in iter(lambda: p.stdout.read(1), b''):
                self.poutput(char.decode(), end='')
                output += char.decode()

        return output

    def connect_ssh(self, address, user):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(address, username=user)

    def run_ssh_command(self, command):
        self.poutput(command, color=bcolors.OKGREEN)
        (_, stdout, stderr) = self.ssh.exec_command(command)
        output = self.print_ssh(stdout)
        self.print_ssh(stderr)
        return output

    def print_ssh(self, file):
        output = ''
        while not file.channel.exit_status_ready():
            buffer = file.read(1).decode()
            self.poutput(buffer, end='')
            output += buffer

        # process leftover
        buffer = file.read().decode()
        if buffer:
            self.poutput(buffer, end='')
            output += buffer

        return output


if __name__ == '__main__':
    App().cmdloop()
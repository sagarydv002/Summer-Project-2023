#!/usr/bin/python3
print("content-type: text/html")
print()

import cgi
import subprocess

form = cgi.FieldStorage()
cmd = form.getvalue("c")

def execute_command(command):
    try:
        output = subprocess.getoutput(command)
        return output
    except Exception as e:
        return str(e)

if "date" in cmd:
    output = execute_command("date")
    print(output)
elif "cal" in cmd:
    output = execute_command("cal")
    print(output)
elif "df" in cmd:
    output = execute_command("df -h")
    print(output)
elif "ifconfig" in cmd:
    output = execute_command("ifconfig")
    print(output)
elif "ls" in cmd:
    output = execute_command("ls -l")
    print(output)
elif "whoami" in cmd:
    output = execute_command("whoami")
    print(output)
elif "pwd" in cmd:
    output = execute_command("pwd")
    print(output)
elif "dd" in cmd:
    output = execute_command("dd")
    print(output)
elif "tail" in cmd:
    output = execute_command("tail new.py")
    print(output)
elif "env" in cmd:
    output = execute_command("env")
    print(output)
elif "netstat" in cmd:
    output = execute_command("netstat -tuln")
    print(output)
elif "head new.py" in cmd:
    output = execute_command("head new.py")
    print(output)
elif "grep" in cmd:
    output = execute_command("grep")
    print(output)
elif "docker ps -a" in cmd:
    output = execute_command("sudo docker ps -a")
    print(output)
elif "docker ps" in cmd:
    output = execute_command("sudo docker ps")
    print(output)
elif "docker images" in cmd:
    output = execute_command("sudo docker images")
    print(output)
elif "launch centos" in cmd:
    output = execute_command("sudo docker pull centos:7")
    print(output)
elif "launch rhel" in cmd:
    output = execute_command("sudo docker pull team15/rhel9")
    print(output)
elif "openss" in cmd:
    output = execute_command("openssl version")
    print(output)
elif "free" in cmd:
    output = execute_command("free -h")
    print(output)
elif "uptime" in cmd:
    output = execute_command("uptime")
    print(output)
elif "top" in cmd:
    output = execute_command("top -n 1")
    print(output)
elif "ps aux" in cmd:
    output = execute_command("ps aux")
    print(output)
elif "hostname" in cmd:
    output = execute_command("hostname")
    print(output)
elif "ping" in cmd:
    output = execute_command("ping -c 5 google.com")
    print(output)
elif "traceroute" in cmd:
    output = execute_command("traceroute google.com")
    print(output)
elif "who" in cmd:
    output = execute_command("who")
    print(output)
elif "uname" in cmd:
    output = execute_command("uname -a")
    print(output)
elif "lsblk" in cmd:
    output = execute_command("lsblk")
    print(output)
elif "df -i" in cmd:
    output = execute_command("df -i")
    print(output)
elif "ps aux | grep" in cmd:
    output = execute_command("ps aux | grep")
    print(output)
elif "history" in cmd:
    output = execute_command("history")
    print(output)
elif "ifconfig -a" in cmd:
    output = execute_command("ifconfig -a")
    print(output)
elif "uname -r" in cmd:
    output = execute_command("uname -r")
    print(output)
elif "lsusb" in cmd:
    output = execute_command("lsusb")
    print(output)
elif "lscpu" in cmd:
    output = execute_command("lscpu")
    print(output)
elif "lsmod" in cmd:
    output = execute_command("lsmod")
    print(output)
elif "chmod" in cmd:
    output = execute_command("chmod permissions filename")
    print(output)
elif "chown" in cmd:
    output = execute_command("chown user:group filename")
    print(output)
elif "df -h" in cmd:
    output = execute_command("df -h")
    print(output)
elif "du -h" in cmd:
    output = execute_command("du -h")
    print(output)
elif "grep" in cmd:
    output = execute_command("grep pattern filename.txt")
    print(output)
elif "sed" in cmd:
    output = execute_command("sed 's/old_pattern/new_pattern/' filename.txt")
    print(output)
elif "awk" in cmd:
    output = execute_command("awk '{print $1}' filename.txt")
    print(output)
elif "tail" in cmd:
    output = execute_command("tail -n 10 filename.txt")
    print(output)
elif "head" in cmd:
    output = execute_command("head -n 10 filename.txt")
    print(output)
elif "history" in cmd:
    output = execute_command("history")
    print(output)
elif "tar" in cmd:
    output = execute_command("tar -czvf archive.tar.gz files")
    print(output)
elif "unzip" in cmd:
    output = execute_command("unzip archive.zip")
    print(output)
elif "kill" in cmd:
    output = execute_command("kill process_id")
    print(output)
elif "crontab -l" in cmd:
    output = execute_command("crontab -l")
    print(output)
elif "crontab -e" in cmd:
    output = execute_command("crontab -e")
    print(output)
elif "find" in cmd:
    output = execute_command("find /path/to/search -name filename")
    print(output)
elif "ssh" in cmd:
    output = execute_command("ssh user@hostname")
    print(output)
elif "scp" in cmd:
    output = execute_command("scp source_file user@hostname:destination_path")
    print(output)
else:
    print("Command not found")
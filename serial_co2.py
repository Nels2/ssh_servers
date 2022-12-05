# Import needed modules
import os
import sys
import subprocess

# Create variables to store data
cpu_usage = os.popen('grep \'cpu \' /proc/stat | awk \'{usage=($2+$4)*100/($2+$4+$5)} END {print usage "%"}\'').read()
ram_usage = os.popen('free -m | awk \'NR==2{printf "%.2f%%", $3*100/$2 }\'').read()
docker_containers = os.popen('docker ps --format "{{.Names}}"').read()
disk_usage = os.popen('df -h | awk \'$NF=="/"{printf "%s", $5}\'').read()

# Create ssh connection to linux server and initiate remote serial connection
# Replace "user" and "server_ip" with respective information
ssh_connection = subprocess.Popen(['ssh', 'user@server_ip', 'sudo', 'screen', '/dev/tty1'],
                                shell=False,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

# Send data over serial connection
ssh_connection.stdin.write(cpu_usage)
ssh_connection.stdin.write(ram_usage)
ssh_connection.stdin.write(docker_containers)
ssh_connection.stdin.write(disk_usage)

ssh_connection.stdin.close()
ssh_connection.wait()

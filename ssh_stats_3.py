# connects to four different Linux servers via ssh and print an output of each server's CPU usage, RAM usage, docker containers running, and Disk usage to separate variables for each server. 
# Next, creates a file 'load.txt' that has all variables organized by server. 
# Then the script opens a sftp connection to a linux server and sends the file that was created to /vLabsMon/

# Import Modules
import paramiko
import os

# Create Variables for Servers
server1 = '192.168.1.1'
server2 = '192.168.1.2'
server3 = '192.168.1.3'
server4 = '192.168.1.4'

# Connect to Servers via SSH and Execute Commands
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(server1, username='admin',password='password')
stdin, stdout, stderr = ssh.exec_command("top -b -n 1 | grep -i \"cpu(s)\\|mem\\|docker\\|disk\"")

cpu_usage1, mem_usage1, docker_containers1, disk_usage1 = stdout.read().splitlines()

ssh.connect(server2, username='admin',password='password')
stdin, stdout, stderr = ssh.exec_command("top -b -n 1 | grep -i \"cpu(s)\\|mem\\|docker\\|disk\"")

cpu_usage2, mem_usage2, docker_containers2, disk_usage2 = stdout.read().splitlines()

ssh.connect(server3, username='admin',password='password')
stdin, stdout, stderr = ssh.exec_command("top -b -n 1 | grep -i \"cpu(s)\\|mem\\|docker\\|disk\"")

cpu_usage3, mem_usage3, docker_containers3, disk_usage3 = stdout.read().splitlines()

ssh.connect(server4, username='admin',password='password')
stdin, stdout, stderr = ssh.exec_command("top -b -n 1 | grep -i \"cpu(s)\\|mem\\|docker\\|disk\"")

cpu_usage4, mem_usage4, docker_containers4, disk_usage4 = stdout.read().splitlines()

# Create File
f= open("load.txt","w+")
f.write("Server 1 CPU Usage: %s\nServer 1 Memory Usage: %s\nServer 1 Docker Containers: %s\nServer 1 Disk Usage: %s\n\nServer 2 CPU Usage: %s\nServer 2 Memory Usage: %s\nServer 2 Docker Containers: %s\nServer 2 Disk Usage: %s\n\nServer 3 CPU Usage: %s\nServer 3 Memory Usage: %s\nServer 3 Docker Containers: %s\nServer 3 Disk Usage: %s\n\nServer 4 CPU Usage: %s\nServer 4 Memory Usage: %s\nServer 4 Docker Containers: %s\nServer 4 Disk Usage: %s" % (cpu_usage1, mem_usage1, docker_containers1, disk_usage1, cpu_usage2, mem_usage2, docker_containers2, disk_usage2, cpu_usage3, mem_usage3, docker_containers3, disk_usage3, cpu_usage4, mem_usage4, docker_containers4, disk_usage4))

f.close()

# SFTP File
sftp = ssh.open_sftp()
sftp.put('load.txt', '/vLabsMon/load.txt')
sftp.close()

# Close SSH Connection
ssh.close()

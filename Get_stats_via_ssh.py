import paramiko

# Declare servers
servers = ["server1", "server2", "server3", "server4"]

# Establish SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Loop through servers
for server in servers:
    ssh.connect(server, username="username", password="password")
    stdin, stdout, stderr = ssh.exec_command("cat /proc/meminfo")
    meminfo = stdout.read()
    # Write cpu, ram, docker and disk usage to file
    with open(f"{server}.txt", "w") as f:
        # CPU Usage
        cpu_usage = ssh.exec_command("top -bn1 | awk '/Cpu/ {print $2}'")
        f.write(f"CPU Usage: {cpu_usage[1].read()}")
        # RAM Usage
        f.write(f"RAM Usage: {meminfo.split('\n')[0].split()[1]}")
        # Docker Containers
        docker_containers = ssh.exec_command("docker container ls -aq")
        f.write(f"Docker Containers Running: {docker_containers[1].read()}")
        # Disk Usage
        disk_usage = ssh.exec_command("df -h")
        f.write(f"Disk Usage: {disk_usage[1].read()}")

# Close SSH connection
ssh.close()

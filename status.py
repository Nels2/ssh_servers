import paramiko

# Define list of servers
servers = ["server1", "server2", "server3", "server4"]

# Initialize SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 

# Loop through list of servers
for server in servers:
    # Connect to server
    ssh.connect(server, username="user", password="mypass")
    # Execute command to get CPU, RAM and Disk usage
    stdin, stdout, stderr = ssh.exec_command("df -h; free -h")
    # Get output of command
    output = stdout.readlines()
    # Print server name
    print(server, ":")
    # Print output of command
    for line in output:
        print(line.strip())
    print("\n")

# Close SSH connection
ssh.close()

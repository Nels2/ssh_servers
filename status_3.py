import paramiko

# Define connection details
SERVERS = [
    {'hostname': 'server1', 'username': 'admin', 'password': 'password'},
    {'hostname': 'server2', 'username': 'admin', 'password': 'password'},
    {'hostname': 'server3', 'username': 'admin', 'password': 'password'},
    {'hostname': 'server4', 'username': 'admin', 'password': 'password'}
]

# Define commands to run
COMMANDS = [
    'top -bn1 | grep "Cpu(s)"',
    'free -mh',
    'docker ps',
    'df -h'
]

# Connect to each server and run commands
for server in SERVERS:
    # Connect via SSH
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=server['hostname'], username=server['username'], password=server['password'])

    # Run commands
    for command in COMMANDS:
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print(f"{server['hostname']} Output: {stdout.read()}")

    # Close connection
    ssh_client.close()

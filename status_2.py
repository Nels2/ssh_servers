# Import the needed modules
import paramiko

# Create the variables for each server
server1 = "example.com"
server2 = "example2.com"
server3 = "example3.com"
server4 = "example4.com"

# Create the variables to store system information
server1_cpu = ""
server1_ram = ""
server1_disk = ""
server2_cpu = ""
server2_ram = ""
server2_disk = ""
server3_cpu = ""
server3_ram = ""
server3_disk = ""
server4_cpu = ""
server4_ram = ""
server4_disk = ""

# Create the SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the first server
client.connect(server1, username="username", password="password")

# Execute the command to get CPU, RAM, and Disk usage
stdin, stdout, stderr = client.exec_command("cat /proc/meminfo && cat /proc/cpuinfo && df -h")

# Read the output
out = stdout.read().splitlines()

# Parse the output
for line in out:
    if line.startswith("MemTotal:"):
        server1_ram = line.split()[1]
    elif line.startswith("model name"):
        server1_cpu = line.split(":")[1].strip()
    elif line.startswith("/dev/sda1"):
        server1_disk = line.split()[4]

# Close the connection
client.close()

# Connect to the second server
client.connect(server2, username="username", password="password")

# Execute the command to get CPU, RAM, and Disk usage
stdin, stdout, stderr = client.exec_command("cat /proc/meminfo && cat /proc/cpuinfo && df -h")

# Read the output
out = stdout.read().splitlines()

# Parse the output
for line in out:
    if line.startswith("MemTotal:"):
        server2_ram = line.split()[1]
    elif line.startswith("model name"):
        server2_cpu = line.split(":")[1].strip()
    elif line.startswith("/dev/sda1"):
        server2_disk = line.split()[4]

# Close the connection
client.close()

# Connect to the third server
client.connect(server3, username="username", password="password")

# Execute the command to get CPU, RAM, and Disk usage
stdin, stdout, stderr = client.exec_command("cat /proc/meminfo && cat /proc/cpuinfo && df -h")

# Read the output
out = stdout.read().splitlines()

# Parse the output
for line in out:
    if line.startswith("MemTotal:"):
        server3_ram = line.split()[1]
    elif line.startswith("model name"):
        server3_cpu = line.split(":")[1].strip()
    elif line.startswith("/dev/sda1"):
        server3_disk = line.split()[4]

# Close the connection
client.close()

# Connect to the fourth server
client.connect(server4, username="username", password="password")

# Execute the command to get CPU, RAM, and Disk usage
stdin, stdout, stderr = client.exec_command("cat /proc/meminfo && cat /proc/cpuinfo && df -h")

# Read the output
out = stdout.read().splitlines()

# Parse the output
for line in out:
    if line.startswith("MemTotal:"):
        server4_ram = line.split()[1]
    elif line.startswith("model name"):
        server4_cpu = line.split(":")[1].strip()
    elif line.startswith("/dev/sda1"):
        server4_disk = line.split()[4]

# Close the connection
client.close()

# Print the results
print("Server 1 CPU: %s, RAM: %s, Disk: %s" % (server1_cpu, server1_ram, server1_disk))
print("Server 2 CPU: %s, RAM: %s, Disk: %s" % (server2_cpu, server2_ram, server2_disk))
print("Server 3 CPU: %s, RAM: %s, Disk: %s" % (server3_cpu, server3_ram, server3_disk))
print("Server 4 CPU: %s, RAM: %s, Disk: %s" % (server4_cpu, server4_ram, server4_disk))

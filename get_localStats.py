import psutil
import os

# Get current CPU Usage
cpu_usage = psutil.cpu_percent()

# Get RAM usage
ram_usage = psutil.virtual_memory().percent

# Get list of running Docker containers
docker_containers = len(list(psutil.net_connections()))

# Get Disk Usage
disk_usage = psutil.disk_usage('/').percent

# Print the output in a neat table
print("CPU Usage:\t{0:.2f}%\nRAM Usage:\t{1:.2f}%\nDocker Containers:\t{2}\nDisk Usage:\t{3:.2f}%".format(cpu_usage, ram_usage, docker_containers, disk_usage))

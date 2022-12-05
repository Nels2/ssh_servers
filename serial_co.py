import serial
import psutil

#open serial connection
ser = serial.Serial('/dev/tty1')

#get cpu usage of current machine
cpu_usage = psutil.cpu_percent()

#get RAM usage of current machine
memory = psutil.virtual_memory()
ram_usage = memory.percent

#get Docker containers of current machine
docker_containers = psutil.docker_containers()

#get disk usage of current machine
disks = psutil.disk_usage('/')
disk_usage = disks.percent

#send data to serial connection
ser.write(f"CPU Usage: {cpu_usage}% RAM Usage: {ram_usage}% Docker Containers: {docker_containers} Disk Usage: {disk_usage}%")

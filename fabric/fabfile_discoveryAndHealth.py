from fabric.api import *
from fabric.context_managers import *

from pprint import pprint

env.hosts = ['ip']
env.user = 'user'
env.password = 'password'
env.port = 'port'


def get_system_health():
	discovery_commands = {
	"uptime": "uptime | awk '{print $3,$4}'",
	"hostname": "hostname",
#	"kernel_release": "uname -r",
#	"architecture": "uname -m",
#	"internal_ip": "hostname -I",
	"internal_ip": "ifconfig",
#	"external_ip": "curl -s ipecho.net/plain;echo",
	}
	health_commands = {
	"used_memory": "free | awk '{print $3}' | grep -v free | head -n1",
	"free_memory": "free | awk '{print $4}' | grep -v shared | head -n1",
#	"cpu_usr_percentage": "top | asterisk | awk '{print $1}'",
#	"number_of_process": "ps -A --no-headers | wc -l",
	"logged_users": "who",
#	"top_load_average": "top -n 1 -b | grep 'load average:' | awk '{print $10 $11 $12}'",
#	"disk_usage_external": "df -h | egrep 'Filesystem|/dev/sda*'",
	"disk_usage": "df -h | egrep 'Filesystem|/dev/root'",
#	"time from last reboot": "uptime"
	}
	tasks = [discovery_commands, health_commands]
	for task in tasks:
		#print(task)
		for operation, command in task.items():
			print("==========={0}===========".format(operation))
			output = run(command)

		
		


def detect_host_type():
	output = run("uname -s")
	if output.failed:
		print("something wrong happen, please check the logs")
	elif output.succeeded:
		print("command executed successfully")

def list_all_files_in_directory():
	directory = prompt("please enter full path to the directory the list",
	default = "/root")
	sudo ("cd {0} ; ls -htlr".format(directory))


def main_task():
	detect_host_type()
	list_all_files_in_directory()
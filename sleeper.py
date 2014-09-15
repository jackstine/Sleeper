import os
import sys
import subprocess
from time import *


def main():
	print ("Input the amount of time in minutes that you want")
	set_time=input()
	beginning=time()
	while (True):
		print(time()-(beginning+(60*float(set_time))))
		sleep(5)
		if (time()>(beginning+(60*float(set_time)))):
			break

	status, output = subprocess.getstatusoutput("shutdown -P now")
	return status


if __name__ == '__main__':
	if os.getuid():
		print("This program needs to be run with root privileges,")
		print("please use `sudo python3 ./{0}` to execute it".format(*sys.argv))
		sys.exit(100)
	else:
		sys.exit(main())

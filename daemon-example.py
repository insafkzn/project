from daemon import Daemon 
from check_new_commits import check_new_commits
import time
import sys, pathlib
import gi
import subprocess
import os
gi.require_version('Notify', '0.7')
from gi.repository import Notify
import logging


# Notify.init("MyDaemon")
# Notify.Notification.new("Test notification!").show()

#deamon = Daemon('/home/garfiev/daemon-example.pid')
#deamon.daemonize()
#deamon.run()
#deamon.start()
#deamon.stop()
# cwd = os.getcwd()
cwd = pathlib.Path(__file__).parent.resolve()


logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode='w')

otherFolder = str(cwd) + 'Pull' # for DevopsPyPull/


# str(cwd) directory where we are located
dirGit = str(cwd)

class MyDaemon(Daemon):
	def run(self):
		Notify.init("MyDaemon")
		time.sleep(3)
		while True:
			check_new_commits(dirGit)
			time.sleep(30)

daemon = MyDaemon('/tmp/daemon-example.pid')
if sys.argv[1] == 'start': daemon.start()
elif sys.argv[1] == 'stop': daemon.stop()
elif sys.argv[1] == 'restart': daemon.restart()

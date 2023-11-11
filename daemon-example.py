from daemon import Daemon 
import time
import sys
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

Notify.init("MyDaemon")
Notify.Notification.new("Test notification!").show()

#deamon = Daemon('/home/garfiev/daemon-example.pid')
#deamon.daemonize()
#deamon.run()
#deamon.start()
#deamon.stop()

class MyDaemon(Daemon):
    def run(self):
   	    while True:
   		    time.sleep(1)
			   
daemon = MyDaemon('/home/garfiev/daemon-example.pid')
if sys.argv[1] == 'start': daemon.start()
elif sys.argv[1] == 'stop': daemon.stop()
elif sys.argv[1] == 'restart': daemon.restart()

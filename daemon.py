# daemon.py
import sys
import os
import atexit
import signal

class Daemon:
	def __init__(self, pidfile): self.pidfile = pidfile

	def daemonize(self):
		#"""Deamonize class. UNIX double fork mechanism."""
		try:
			pid = os.fork()
			if pid > 0:
				# exit first parent
				sys.exit(0)
		except OSError as err:
			sys.stderr.write('fork #1 failed: {0}\n'.format(err))
			sys.exit(1)
			
		# decouple from parent environment
		os.chdir('/')
		os.setsid()
		os.umask(0)

   	 # do second fork
		try:
			pid = os.fork()
			if pid > 0:
				# exit from second parent
				sys.exit(0)
		except OSError as err:
			sys.stderr.write('fork #2 failed: {0}\n'.format(err))
			sys.exit(1)

		# redirect standard file descriptors
		sys.stdout.flush()
		sys.stderr.flush()
		si = open(os.devnull, 'r')
		so = open(os.devnull, 'a+')
		se = open(os.devnull, 'a+')

		os.dup2(si.fileno(), sys.stdin.fileno())
		os.dup2(so.fileno(), sys.stdout.fileno())
		os.dup2(se.fileno(), sys.stderr.fileno())

		
			

		# write pidfile
		# atexit.register(self.delpid)

		pid = str(os.getpid())
		with open(self.pidfile,'w+') as f:
			f.write(pid + '\n')  
  
	
	# def delpid(self):
	# 	os.remove(self.pidfile) 
	
	def start(self):
		# a)
		if self.pidfile and os.path.isfile(self.pidfile):
			with open(self.pidfile, 'r') as f:
				pid = int(f.read().strip())
				if pid:
					print("Daemon is already running with PID:", pid)
					sys.exit(1)
			self.pidfile.close()
		deamon = Daemon('/home/garfiev/daemon-example.pid')
		# b)
		deamon.daemonize()
		# c)
		deamon.run()
		

	def stop(self):
		# a)
		if self.pidfile and os.path.isfile(self.pidfile):
			with open(self.pidfile, 'r') as f:
				pid = int(f.read().strip())
				# b)
				os.kill(pid, signal.SIGTERM)
		else:
			print('The daemon is not running')
		if os.path.exists(self.pidfile):
			os.remove(self.pidfile)
		
	
	def restart(self):
	#"""Restart the daemon."""
		self.stop()
		self.start()
	
	def run(self):
		while True:
			pass
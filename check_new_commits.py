import subprocess, pathlib
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
import logging

cwd = pathlib.Path(__file__).parent.resolve()


logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode='w')

def check_new_commits(dirGit):
	subprocess.run(['git', '--git-dir=' + dirGit + '/.git', 'fetch'])
	# Notify.Notification.new("Has new commits!").show()
	# logging.info('--git-dir=' + str(cwd) + '/.git')
	# result = subprocess.run(['git', '--git-dir=' + dirGit + '/.git', 'log', '--graph',"--pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset'", '--abbrev-commit', '--date=relative', 'master..origin/master'], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	result = subprocess.run(['git', '--git-dir=' + dirGit + '/.git', 'log', '--graph',"--pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset'", '--abbrev-commit', '--date=relative', 'origin/master'], text=True, capture_output=True)
	# result = subprocess.run(['git', '--git-dir=' + str(cwd) + '/.git', 'log', 'master..origin/master'], text=True, capture_output=True)
	logging.info('--git-dir=' + str(cwd) + '/.git')
	if result.stdout:
		# logging.info('--git-dir=' + str(cwd) + '/.git')
		Notify.Notification.new('Есть новые коммиты в ' + dirGit, result.stdout).show()
	pass

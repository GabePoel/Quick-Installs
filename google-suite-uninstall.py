import os
home = os.path.expanduser('~')
launcher = os.path.join(home, '.local', 'share', 'applications')
apps = os.path.join(home, '.local', 'share', 'electron-suite')
os.system('rm ' + str(launcher) + '/google-*')
os.system('rm ' + str(apps) + '/Google* -r')
os.system('rm ' + str(apps) + '/Gmail* -r')
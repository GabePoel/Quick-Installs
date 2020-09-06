import os
home = os.path.expanduser('~')
launcher = os.path.join(home, '.local', 'share', 'applications')
apps = os.path.join(home, '.local', 'share', 'electron-suite')
os.system('rm ' + str(launcher) + '/microsoft-*')
os.system('rm ' + str(apps) + '/Microsoft* -r')
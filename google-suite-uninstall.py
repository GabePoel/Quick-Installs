import os
home = os.path.expanduser('~')
launcher = os.path.join(home, '.local', 'share', 'applications')
os.system('rm ' + str(launcher) + '/google-*')
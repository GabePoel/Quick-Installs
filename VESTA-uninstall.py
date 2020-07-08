import os
home = os.path.expanduser('~')
directory = os.path.join(home, '.local', 'share', 'VESTA')
os.system('rm ' + str(directory) + ' -r')
launcher = os.path.join(home, '.local', 'share', 'applications', 'vesta.desktop')
os.system('rm ' + str(launcher))
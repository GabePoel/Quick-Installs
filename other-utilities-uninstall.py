import os
home = os.path.expanduser('~')
launcher = os.path.join(home, '.local', 'share', 'applications')
apps = os.path.join(home, '.local', 'share', 'electron-suite')
os.system('rm ' + str(launcher) + '/other-*')
os.system('rm ' + str(apps) + '/Todoist* -r')
os.system('rm ' + str(apps) + '/Audible* -r')
os.system('rm ' + str(apps) + '/Messenger* -r')
os.system('rm ' + str(apps) + '/Materials* -r')
os.system('rm ' + str(apps) + '/Oura* -r')
os.system('rm ' + str(apps) + '/Headspace* -r')
os.system('rm ' + str(apps) + '/Seconcephalon* -r')
os.system('rm ' + str(apps) + '/IQAir* -r')
os.system('rm ' + str(apps) + '/Mendeley* -r')
os.system('rm ' + str(apps) + '/Kindle* -r')
os.system('rm ' + str(apps) + '/Snapdrop* -r')
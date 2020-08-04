#!/usr/bin/python3

from os import path
from os import system
import sys
import os
import util

home = util.home
config = util.config
here = os.getcwd()
util.check_dir(config)
util.check_dir(path.join(config, 'fonts'))
util.check_dir(path.join(home, '.local', 'share', 'fonts'))

apt_list = util.import_list(path.join(here, 'man', 'apt'))
flat_list = util.import_list(path.join(here, 'man', 'flat'))
pop_list = util.import_list(path.join(here, 'man', 'pop'))
pip_list = util.import_list(path.join(here, 'man', 'pip'))
rem_list = util.import_list(path.join(here, 'man', 'rem'))
git_list = util.import_list(path.join(here, 'man', 'git'))

util.git_install(git_list)
system('sh ' + path.join(config, 'Some-Pretty-Boring-Shell-Scripts', 'make-all-executable'))
kp = path.join(config, 'Korla-Plus')
system('cd ' + kp + ' && python3 ' + path.join(kp, 'install.py') + ' link')
ls = path.join(config, 'Lapidarium-Shell')
system('cd ' + ls + ' && python3 ' + path.join(ls, 'install.py') + ' link')

util.apt_install(apt_list)
util.flatpak_install(flat_list)
util.apt_install(pop_list)
util.pip_install(pip_list)
util.apt_remove(rem_list)
system('migrate-down')
system('restart-gnome-shell')

# try:
#     system('npm install -g gitbook-summary')
# except:
#     pass
# system('python3 google-suite-install.py')
# system('python3 microsoft-office-install.py')
# system('python3 other-utilities-install.py')

try:
    if str(sys.argv()[1]) == 'start':
        system('python3 vesta-install.py')
        system('cd ~/Documents')
        system('mkdir temp-install')
        system('git clone https://github.com/rafaelmardojai/firefox-gnome-theme/ && cd firefox-gnome-theme')
        system('sh ./scripts/install.sh')
        system('cd ~/Documents/temp-install')
        system('git clone https://github.com/sahibjotsaggu/San-Francisco-Pro-Fonts.git')
        system('cd San-Francisco-Pro-Fonts')
        system('cp SF* ~/.local/share/fonts')
        system('git clone https://github.com/ZulwiyozaPutra/SF-Mono-Font')
        system('cd ~/Documents/temp-install/SF-Mono-Font')
        system('cp SF* ~/.local/share/fonts')
        system('cd ~/Documents')
        system('git clone https://github.com/GabePoel/Some-Pretty-Boring-Shell-Scripts.git')
        system('git clone https://github.com/GabePoel/hBlock.git && cd hBlock && sudo sh install.sh && cd .. && sudo rm hBlock -r')
        system('git clone https://github.com/GabePoel/Korla-Plus.git')
        system('cd Korla-Plus')
        system('python3 install.py link')
        util.set_template('Blank Document', '')
        util.set_template('Python Scripts', '#!/usr/bin/python3\n')
        util.set_template('Shell Script', '#!/bin/bash\n')
        try:
            system('sudo apt install matlab-support')
        except:
            pass
except:
    # system('clear')
    print('Basic setup complete.')

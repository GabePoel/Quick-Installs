#!/usr/bin/python3

from os import path
from os import system
import os
import util

home = util.home
here = os.getcwd()
util.check_dir(path.join(home, '.local', 'share', 'fonts'))

apt_list = util.import_list(path.join(here, 'man', 'apt'))
flat_list = util.import_list(path.join(here, 'man', 'flat'))
pop_list = util.import_list(path.join(here, 'man', 'pop'))
pip_list = util.import_list(path.join(here, 'man', 'pip'))

util.apt_install(apt_list)
util.flatpak_install(flat_list)
util.apt_install(pop_list)
util.pip_install(pip_list)

system('python3 google-suite-install.py')
system('python3 microsoft-office-install.py')
system('python3 other-utilities-install.py')
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

# util.web_install()
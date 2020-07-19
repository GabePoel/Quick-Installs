from os import path
from os import system
import os
import wget

home = path.expanduser('~')

def make_launcher(file_name, app_name, executable, comment, icon, categories=[], actions=[]):
    launcher_path = path.join(home, '.local', 'share', 'applications', file_name)
    launcher = open(launcher_path, 'w')
    launcher_string = (
        "[Desktop Entry]\n" +
        "Name=" + app_name + "\n" + 
        "Exec=" + executable + "\n" + 
        "Comment=" + comment + "\n" + 
        "Icon=" + icon + "\n"
        "Type=Application\n"
        "Categories=" + category_string(categories) + "\n"
    )
    if len(actions) > 0:
        launcher_string += "Actions="
        for action in actions:
            launcher_string += action[0] + ';'
        launcher_string += '\n'
        for action in actions:
            launcher_string += '\n\n[Desktop Action ' + action[0] + ']\nName=' + action[1] + '\n'
            launcher_string += 'Exec=' + action[2]
    launcher.write(launcher_string)

def category_string(categories):
    s = ''
    for c in categories:
        s += c + '; '
    return s

def ppa_install(ppa, app_list=None):
    system("sudo add-apt-repository " + str(ppa))
    system("sudo apt-get update")
    if not app_list is None:
        apt_install(app_list)

def apt_install(app_list):
    system("sudo apt-get update")
    install_string = "sudo apt-get install "
    if type(app_list) is list:
        for app in app_list:
            install_string += str(app) + " "
    else:
        install_string += app_list
    system(install_string)

def pip_install(app_list):
    for app in app_list:
        system("pip3 install " + str(app))

def pacman_install(app_list):
    if type(app_list) is list:
        for app in app_list:
            system("sudo pacman -Syu " + str(app))
    else:
        system("sudo pacman -Syu " + str(app_list))

def flatpak_install(app_list):
    try:
        apt_install("flatpak")
        ppa_install("ppa:alexlarsson/flatpak", "flatpak")
        system("flatpak remode-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
    except:
        system("sudo pacman -S flatpak")
    for app in app_list:
        system("flatpak install flathub " + str(app))
        system("flatpak --user override " + str(app) + " --filesystem=/home/$USER/.icons/:ro")

def import_list(fp):
    f = open(fp, 'r')
    l = f.read().split("\n")
    f.close()
    return l


def check_dir(fp):
    if not path.exists(fp):
        os.makedirs(fp)

def web_install(address):
    check_dir(path.join(home, 'Documents', 'temp-install'))
    fp = path.join(home, 'Documents', 'temp-install', 'inst.deb')
    wget.download(address, fp)
    system('sudo apt install ' + str(fp))
    system('rm ' + str(fp))
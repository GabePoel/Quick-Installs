from os import path
from os import system
import os

home = path.expanduser('~')
config = path.join(home, 'Documents', 'Configuration')

def make_launcher(file_name, app_name, executable, comment, icon, categories=[], actions=[], notifications=True):
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
    if notifications:
        launcher_string += 'X-GNOME-UsesNotifications=true\n'
    else:
        launcher_string += 'X-GNOME-UsesNotifications=false\n'
    if len(actions) > 0:
        launcher_string += "Actions="
        for action in actions:
            launcher_string += action[0] + ';'
        launcher_string += '\n'
        for action in actions:
            launcher_string += '\n\n[Desktop Action ' + action[0] + ']\nName=' + action[1] + '\n'
            launcher_string += 'Exec=' + action[2]
            if len(action) > 3:
                launcher_string += '\nIcon=' + action[3]
    launcher.write(launcher_string)

def category_string(categories):
    s = ''
    for c in categories:
        s += c + '; '
    return s

def ppa_install(ppa_list, app_list=None):
    for ppa in ppa_list:
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
    
def apt_remove(app_list):
    for app in app_list:
        system("sudo apt remove " + str(app))

def pip_install(app_list):
    for app in app_list:
        system("pip3 install " + str(app) + " --user")

def dnf_install(app_list):
    for app in app_list:
        system("sudo dnf install " + str(app) + " -y")

def pacman_install(app_list):
    if type(app_list) is list:
        for app in app_list:
            system("sudo pacman -Syu " + str(app))
    else:
        system("sudo pacman -Syu " + str(app_list))

def flatpak_install(app_list):
    # try:
    #     apt_install("flatpak")
    #     ppa_install("ppa:alexlarsson/flatpak", "flatpak")
    #     system("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
    # except:
    #     system("sudo pacman -S flatpak")
    for app in app_list:
        system("flatpak install flathub " + str(app) + ' -y')
        system("flatpak --user override " + str(app) + " --filesystem=/home/$USER/.icons/:ro")

def import_list(fp):
    f = open(fp, 'r')
    l = f.read().split("\n")
    f.close()
    return l


def check_dir(fp):
    if not path.exists(fp):
        os.makedirs(fp)
    return fp

def web_install(address_list, extension='.rpm'):
    os.system('pip3 install wget --user')
    import wget
    for address in address_list:
        check_dir(path.join(home, 'Documents', 'temp-install'))
        fp = path.join(home, 'Documents', 'temp-install', 'inst' + extension)
        wget.download(address, fp)
        if extension == '.deb':
            system('sudo apt install ' + str(fp))
        elif extension == '.rpm':
            system('sudo rpm install ' + str(fp))
        system('rm ' + str(fp))

def set_template(name, text):
    fp = path.join(home, 'Templates', name)
    f = open(fp, 'w')
    f.write(text)
    f.close()

def git_install(clone_address, sub_dir=None):
    if not sub_dir is None:
        loc = path.join(config, sub_dir)
    else:
        loc = config
    if type(clone_address) == list:
        for address in clone_address:
            git_install(address)
    else:
        dir_name = clone_address[:-4].split('/')[-1]
        fp = path.join(loc, dir_name)
        if path.exists(fp):
            system('cd ' + fp + ' && ' + 'git pull')
        else:
            system('cd ' + loc + ' && ' + 'git clone ' + clone_address)
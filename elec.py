import gi
import os
import util
from os import system
from os import path
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

util.check_dir('~/.local/share/electron-suite')

def generate(address, name, icon, dark=True):
    util.check_dir('~/.local/share/electron-suite')
    here = os.getcwd()
    reduced_name = ''
    for n in name.split(' '):
        reduced_name += n
    target_name = path.join(here, reduced_name + '-linux-x64')
    fp = get_icon(icon)
    if fp is None:
        # dialog = Gtk.FileChooserDialog(action=Gtk.FileChooserAction.OPEN)
        # dialog.add_buttons(
        #     Gtk.STOCK_CANCEL,
        #     Gtk.ResponseType.CANCEL,
        #     Gtk.STOCK_OPEN,
        #     Gtk.ResponseType.OK,
        # )
        # dialog.run()
        # fp = dialog.get_filename()
        print(icon)
    system('inkscape -o ' + str(path.join(here, 'icon.png')) + ' -w 128 -h 128 ' + str(fp))
    if dark:
        system('nativefier ' + address + ' --name "' + name + '" --inject ~/Documents/Quick-Installs/resources/nativefier-dark.js --icon ' + path.join(here, 'icon.png') + ' --internal-urls ".*?"')
    else:
        system('nativefier ' + address + ' --name "' + name + '" --icon ' + path.join(here, 'icon.png') + ' --internal-urls ".*?"')
    package = path.join(target_name, 'resources', 'app', 'package.json')
    f = open(package, 'r')
    s = f.readlines()[0]
    i_start = s.find('"name":') + 7
    s_remaining = s[i_start:]
    i_end = s_remaining.find(',') + i_start
    s_name = s[i_start + 1:i_end - 1]
    s = s.replace(s_name, name)
    f.close()
    f = open(package, 'w')
    f.write(s)
    f.close()
    system('cd ' + target_name + ' && chmod +x ./' + reduced_name)
    system('rm ' + path.join(here, 'icon.png'))
    system('mv ' + target_name + ' ~/.local/share/electron-suite/ -f')
    system('rm ' + target_name + ' -r')
    ex_cont = "#!/bin/bash\n$HOME/.local/share/electron-suite/" + reduced_name + '-linux-x64' + '/' + reduced_name
    ex_name = name.replace(' ', '-', 999).lower()
    scripts = path.join(util.home, '.local', 'bin')
    ex_name = path.join(scripts, ex_name)
    ex = open(ex_name, 'w+')
    ex.write(ex_cont)
    ex.close()
    system('chmod +x ' + ex_name)
    print(ex_name)
    
def get_icon(icon_name):
    icon_theme = Gtk.IconTheme.get_default()
    icon = icon_theme.lookup_icon(icon_name, 48, 0)
    if icon:
        return icon.get_filename()
    else:
        return None
        
def electron_launcher(launcher_name, app_name, address, icon, description, categories=['Network', 'Office', 'Utility'], dark=True):
    util.check_dir('~/.local/share/electron-suite')
    generate(address, app_name, icon, dark)
    reduced_name = ''
    for n in app_name.split(' '):
        reduced_name += n
    target_name = reduced_name + '-linux-x64/' + reduced_name
    util.make_launcher(launcher_name, app_name, util.home + '/.local/share/electron-suite/' + target_name, description, icon, categories=categories, actions=[])

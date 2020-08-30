import gi
import os
from os import system
from os import path
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

util.checkdir('~/.local/share/electron-suite')

def generate(address, name, icon, dark=True):
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
        system('nativefier ' + address + ' --name "' + name + ' --icon ' + path.join(here, 'icon.png') + ' --internal-urls ".*?"')
    system('cd ' + target_name + ' && chmod +x ./' + reduced_name)
    system('rm ' + path.join(here, 'icon.png'))
    system('mv ' + target_name + ' ~/.local/share/electron-suite/ -f')
    system('rm ' + target_name + ' -r')
    
def get_icon(icon_name):
    icon_theme = Gtk.IconTheme.get_default()
    icon = icon_theme.lookup_icon(icon_name, 48, 0)
    if icon:
        return icon.get_filename()
    else:
        return None

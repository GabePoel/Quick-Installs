import gi
import os
import util
import shutil
from os import system
from os import path
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

suite = path.join(util.home, '.local', 'share', 'electron-suite')

util.check_dir(suite)

def generate(address, name, icon, dark=True, all_urls=True, flags=''):
    if len(flags) > 0:
        flags = ' ' + flags
    if all_urls:
        flags += ' --internal-urls ".*?"'
    flags += ' --background-color "#404040"'
    util.check_dir(suite)
    here = os.getcwd()
    reduced_name = ''
    for n in name.split(' '):
        reduced_name += n
    target_name = path.join(here, reduced_name + '-linux-x64')
    fp = get_icon(icon)
    if fp is None:
        fp = get_icon('application-default-icon')
        # dialog = Gtk.FileChooserDialog(action=Gtk.FileChooserAction.OPEN)
        # dialog.add_buttons(
        #     Gtk.STOCK_CANCEL,
        #     Gtk.ResponseType.CANCEL,
        #     Gtk.STOCK_OPEN,
        #     Gtk.ResponseType.OK,
        # )
        # dialog.run()
        # fp = dialog.get_filename()
    system('inkscape -z ' + str(fp) + ' -w 1024 -h 1024 -e ' + str(path.join(here, 'icon.png')))
    if dark:
        system('nativefier ' + address + ' --name "' + name + '" --inject ~/Documents/Quick-Installs/resources/nativefier-dark.js --icon ' + path.join(here, 'icon.png') + flags)
    else:
        system('nativefier ' + address + ' --name "' + name + '" --icon ' + path.join(here, 'icon.png') + flags)
    os.remove(path.join(here, 'icon.png'))
    os.rename(target_name, reduced_name)
    target_name = path.join(here, reduced_name)
    package = path.join(target_name, 'resources', 'app', 'package.json')
    f = open(package, 'r')
    s = f.readlines()[0]
    i_start = s.find('"name":') + 7
    s_remaining = s[i_start:]
    i_end = s_remaining.find(',') + i_start
    s_name = s[i_start + 1:i_end - 1]
    s = s.replace(s_name, name)
    f.close()
    f = open(package, 'w+')
    f.write(s)
    f.close()
    system('cd ' + target_name + ' && chmod +x ./' + reduced_name)
    if path.exists(path.join(suite, reduced_name)):
        shutil.rmtree(path.join(suite, reduced_name))
    shutil.move(target_name, path.join(suite, reduced_name), )
    ex_cont = "#!/bin/bash\n$HOME/.local/share/electron-suite/" + reduced_name + '/' + reduced_name
    ex_name = name.replace(' ', '-', 999).lower()
    scripts = path.join(util.home, '.local', 'bin')
    ex_name = path.join(scripts, ex_name)
    ex = open(ex_name, 'w+')
    ex.write(ex_cont)
    ex.close()
    system('chmod +x ' + ex_name)
    
def get_icon(icon_name):
    icon_theme = Gtk.IconTheme.get_default()
    icon = icon_theme.lookup_icon(icon_name, 48, 0)
    if icon:
        return icon.get_filename()
    else:
        return None
        
def electron_launcher(launcher_name, app_name, address, icon, description, categories=['Network', 'Office', 'Utility'], dark=True, all_urls=True, flags='', style=None, force_style=False, actions=[], notifications=True):
    util.check_dir(suite)
    generate(address, app_name, icon, dark=dark, all_urls=all_urls, flags=flags)
    reduced_name = ''
    for n in app_name.split(' '):
        reduced_name += n
    target_name = reduced_name + '/' + reduced_name
    util.make_launcher(launcher_name, app_name, util.home + '/.local/share/electron-suite/' + target_name, description, icon, categories=categories, actions=actions, notifications=notifications)
    if dark:
        if style is None:
            style = 'default'
        print('updating style')
        css_path = path.join(os.getcwd(), 'resources', style + '.css')
        css_file = open(css_path)
        css_lines = css_file.readlines()
        js_path = util.home + '/.local/share/electron-suite/' + reduced_name + '/resources/app/inject/inject.js'
        js_file = open(js_path)
        js_lines = js_file.readlines()
        if force_style:
            css_lines = [line[:-2] + ' !important;\n' if len(line) > 1 and line[-2] == ';' and not '!important' in line else line for line in css_lines]
        css_lines = ["\t'" + line[:-1] + "',\n" for line in css_lines]
        css_lines[-1] = css_lines[-1][:-1]
        js_lines = [js_lines[0]] + css_lines + js_lines[1:]
        css_file.close()
        js_file.close()
        js_file = open(js_path, 'w')
        js_string = ''.join(js_lines)
        js_file.write(js_string)
        js_file.close()
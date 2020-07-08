import os

home = os.path.expanduser('~')

def make_launcher(file_name, app_name, executable, comment, icon, categories=[]):
    launcher_path = os.path.join(home, '.local', 'share', 'applications', file_name)
    launcher = open(launcher_path, 'w')
    launcher.write(
        "[Desktop Entry]\n" +
        "Name=" + app_name + "\n" + 
        "Exec=" + executable + "\n" + 
        "Comment=" + comment + "\n" + 
        "Icon=" + icon + "\n"
        "Type=Application\n"
        "Categories=" + category_string(categories) + "\n"
    )

def category_string(categories):
    s = ''
    for c in categories:
        s += c + '; '
    return s
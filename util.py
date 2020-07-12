import os

home = os.path.expanduser('~')

def make_launcher(file_name, app_name, executable, comment, icon, categories=[], actions=[]):
    launcher_path = os.path.join(home, '.local', 'share', 'applications', file_name)
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
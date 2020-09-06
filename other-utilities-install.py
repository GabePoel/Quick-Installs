# These won't be too useful unless you have things configured exactly as I do

import util
import elec
import os

elec.electron_launcher('other-todoist.desktop', 'Todoist', 'todoist.com', 'todoist', 'To do list.', dark=False)
elec.electron_launcher('other-audible.desktop', 'Audible', 'audible.com', 'audible', "Amazon's audiobook service.", categories=['Audio'], dark=False)
elec.electron_launcher('other-messenger.desktop', 'Messenger', 'messenger.com', 'messengerfordesktop', "Facebook instant messaging.", categories=['InstantMessaging'])
elec.electron_launcher('other-materials-project.desktop', 'Materials Project', 'materialsproject.org', 'materials-project', 'Computational materials prediction database.', categories=['Science'])
elec.electron_launcher('other-oura.desktop', 'Oura', 'cloud.ouraring.com', 'oura', 'Sleep tracking and health.', categories=['Health'], dark=False)
elec.electron_launcher('other-headspace.desktop', 'Headspace', 'my.headspace.com', 'headspace', 'Guided meditations.', categories=['Health'], dark=False)
elec.electron_launcher('other-seconcephalon.desktop', 'Seconcephalon', 'seconcephalon.net', 'seconcephalon', 'Second brain.', categories=['Utilities', 'Health'])

home = os.path.expanduser('~')
documents = os.path.join(home, 'Documents')
scripts = os.path.join(documents, 'Some-Pretty-Boring-Shell-Scripts')
box_actions = [
    ['mount', 'Mount', 'sh ' + os.path.join(scripts, 'mount-box')],
    ['unmount', 'Unmount', 'sh ' + os.path.join(scripts, 'unmount-box')],
    ['sync', 'Sync', 'sh ' + os.path.join(scripts, 'sync-box')]
]
util.make_launcher('other-box.desktop', 'Box', 'sh ' + os.path.join(scripts, 'mount-box'), 'Cloud file storage.', 'dropbox', categories=['Network', 'Utility', 'Office'], actions=box_actions)
headspace_actions = [
    ['discover', 'Discover', 'xdg-open https://my.headspace.com/discover/packs'],
    ['stats', 'Stats', 'xdg-open https://my.headspace.com/profile/stats'],
    ['journey', 'Journey', 'xdg-open https://my.headspace.com/profile/journey']
]
# util.make_launcher('other-headspace.desktop', 'Headspace', 'xdg-open https://my.headspace.com', 'Guided meditations.', 'headspace', categories=['Health'], actions=headspace_actions)
util.make_launcher('other-github.desktop', 'GitHub', 'xdg-open https://github.com', 'Online git repository service.', 'github', categories=['Office', 'Network', 'Utility'])
util.make_launcher('other-wolfram-alpha.desktop', 'Wolfram Alpha', 'xdg-open https://wolframalpha.com', 'Online calculator.', 'wolfram-alpha', categories=['Science', 'Education'])
# util.make_launcher('other-lastpass.desktop', 'LastPass', 'xdg-open https://lastpass.com/?ac=1', 'Password manager.', 'lastpass', categories=['Network', 'Utility'])
util.make_launcher('other-jupyter.desktop', 'Jupyter', 'jupyter notebook', 'Interactive programming and data analysis.', 'jupyter-notebook', categories=['Science'])

# These won't be too useful unless you have things configured exactly as I do

import util
import os

util.make_launcher('other-audible.desktop', 'Audible', 'xdg-open https://audible.com', "Amazon's audiobook service.", 'audible', categories=['Audio'])
util.make_launcher('other-messenger.desktop', 'Messenger', 'xdg-open https://messenger.com', "Facebook instant messaging.", 'google-sheets', categories=['Office'])
util.make_launcher('other-materials-project', 'Materials Project', 'xdg-open https://materialsproject.org', 'Computational materials prediction database.', 'kalzium', categories=['Science'])

home = os.path.expanduser('~')
documents = os.path.join(home, 'Documents')
scripts = os.path.join(documents, 'Some-Pretty-Boring-Shell-Scripts')
box_actions = [
    ['mount', 'Mount', 'sh ' + os.path.join(scripts, 'mount-box')],
    ['unmount', 'Unmount', 'sh ' + os.path.join(scripts, 'unmount-box')],
    ['sync', 'Sync', 'sh ' + os.path.join(scripts, 'sync-box')]
]
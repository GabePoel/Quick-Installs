# These won't be too useful unless you have things configured exactly as I do

import util
import os

util.make_launcher('other-audible.desktop', 'Audible', 'xdg-open https://audible.com', "Amazon's audiobook service.", 'audible', categories=['Audio'])
util.make_launcher('other-messenger.desktop', 'Messenger', 'xdg-open https://messenger.com', "Facebook instant messaging.", 'messengerfordesktop', categories=['InstantMessaging'])
util.make_launcher('other-materials-project.desktop', 'Materials Project', 'xdg-open https://materialsproject.org', 'Computational materials prediction database.', 'kalzium', categories=['Science'])

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
util.make_launcher('other-headspace.desktop', 'Headspace', 'xdg-open https://my.headspace.com', 'Guided meditations.', 'headspace', categories=['Health'], actions=headspace_actions)
util.make_launcher('github.desktop', 'GitHub', 'xdg-open https://github.com', 'Online git repository service.', 'github', categories=['Office', 'Network', 'Utility'])

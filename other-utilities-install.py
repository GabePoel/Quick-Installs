# These won't be too useful unless you have things configured exactly as I do

import util
import elec
import os

elec.uninstall('Messenger', 'messenger', True)

todoist_actions = [
    ['add', 'Quick Add', 'com.github.alainm23.planner.quick-add', 'todo-indicator'],
    ['beta', 'Beta', 'todoist-beta', 'todoist']
]
elec.generate('https://beta.todoist.com', 'Todoist Beta', 'todoist', dark=False, flags='--tray --single-instance --app-version "0.3"')
elec.electron_launcher('audible.desktop', 'Audible', 'https://audible.com', 'audible', 'Audiobooks by Amazon.', categories=['Media'], all_urls=True, dark=False, flags='--tray --single-instance --app-version "0.3"', notifications=True, styles='audible')
elec.electron_launcher('kindle.desktop', 'Kindle', 'https://read.amazon.com', 'application-x-mobi8-ebook', 'Ebooks by Amazon.', categories=['Media'], all_urls=True, dark=False, flags='--tray --single-instance --app-version "0.2"', notifications=True)
elec.electron_launcher('todoist.desktop', 'Todoist', 'https://todoist.com', 'todoist', 'Organize, plan, and collaborate on tasks and projects.', categories=['Productivity', 'Office', 'Utility'], all_urls=True, dark=False, flags='--tray --single-instance --app-version "0.3"', notifications=True, actions=todoist_actions)
elec.electron_launcher('messenger.desktop', 'Messenger', 'https://messenger.com', 'messengerfordesktop', 'Chat with your Facebook friends.', categories=['Social'], dark=False, flags='--tray --single-instance --app-version "0.2" --inject "resources/default.css"', notifications=True, force_style=False, styles=['messenger'])
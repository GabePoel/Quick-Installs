# These won't be too useful unless you have things configured exactly as I do

import util
import elec
import os

elec.uninstall('Todoist')
elec.electron_launcher('audible.desktop', 'Audible', 'https://audible.com', 'application-x-mobi8-ebook', 'Audiobooks by Amazon.', categories=['Media'], all_urls=True, dark=False, flags='--tray --single-instance --app-version "0.3"', notifications=True, styles='audible')
elec.electron_launcher('todoist.desktop', 'Todoist', 'https://todoist.com', 'todoist', 'Organize, plan, and collaborate on tasks and projects.', categories=['Productivity', 'Office', 'Utility'], all_urls=True, dark=False, flags='--tray --single-instance --app-version "0.2"', notifications=True)
elec.electron_launcher('messenger.desktop', 'Messenger', 'https://messenger.com', 'messengerfordesktop', 'Chat with your Facebook friends.', categories=['Social'], dark=False, flags='--tray --single-instance --app-version "0.2"', notifications=True, force_style=True)

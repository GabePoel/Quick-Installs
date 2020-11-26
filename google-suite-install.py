import elec

elec.uninstall('Gmail', 'google-mail', True)
elec.uninstall('Google Calendar', 'google-calendar', True)

# elec.electron_launcher('google-mail.desktop', 'Gmail', 'https://mail.google.com', 'gmail', "Email that's intuitive, efficient, and useful.", categories=['Network', 'Email', 'Office', 'InstantMessaging'], all_urls=False, dark=False, flags="--counter --internal-urls '.*?\.google\.*?|.*?auth\.berkeley\.*?' --tray --single-instance --app-version '0.6'", styles=['gmail', 'gmail2', 'bauth', 'gauth'], force_style=True, notifications=True)
# elec.electron_launcher('google-calendar.desktop', 'Google Calendar', 'https://calendar.google.com', 'google-calendar', "A time-management and scheduling calendar service developed by Google.", categories=['Network', 'Office'], all_urls=False, dark=True, flags="--internal-urls '.*?\.google\.*?|.*?auth\.berkeley\.*?' --tray --single-instance --app-version '0.6'", styles=['calendar'], force_style=True, notifications=True)
elec.electron_launcher('google-messages.desktop', 'Messages', 'https://messages.google.com/web', 'internet-chat', "Simple, helpful messaging by Google.", categories=['Network', 'InstantMessaging'], all_urls=True, dark=False, flags="--counter --tray --single-instance --app-version '0.6'", notifications=True)
elec.electron_launcher('google-keep.desktop', 'Google Keep', 'https://keep.google.com/u/0/', 'google-keep', 'Capture notes, share them with others, and access them from anywhere.', categories=['Office', 'Utilities'], all_urls=True, dark=False, flags="--counter --tray --single-instance --app-version '0.1'", notifications=True)

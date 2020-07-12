import util

drive_actions = [
    ['priority', 'Priority', 'xdg-open https://drive.google.com/drive/priority'],
    ['my-drive', 'My Drive', 'xdg-open https://drive.google.com/drive/my-drive'],
    ['shared-drives', 'Shared Drives', 'xdg-open https://drive.google.com/drive/shared-drives'],
    ['shared', 'Shared With Me', 'xdg-open https://drive.google.com/drive/shared-with-me'],
    ['recent', 'Recent', 'xdg-open https://drive.google.com/drive/recent'],
    ['starred', 'Starred', 'xdg-open https://drive.google.com/drive/starred'],
    ['quota', 'Storage', 'xdg-open https://drive.google.com/drive/quota']
]
mail_actions = [
    ['inbox', 'Inbox', 'xdg-open https://mail.google.com/mail/#inbox'],
    ['starred', 'Starred', 'xdg-open https://mail.google.com/mail/#starred'],
    ['snoozed', 'Snoozed', 'xdg-open https://mail.google.com/mail/#snoozed'],
    ['important', 'Important', 'xdg-open https://mail.google.com/mail/#imp'],
    ['sent', 'Sent', 'xdg-open https://mail.google.com/mail/#sent'],
    ['drafts', 'Drafts', 'xdg-open https://mail.google.com/mail/#drafts'],
    ['social', 'Social', 'xdg-open https://mail.google.com/mail/#category/social'],
    ['updates', 'Updates', 'xdg-open https://mail.google.com/mail/#category/updates'],
    ['forums', 'Forums', 'xdg-open https://mail.google.com/mail/#category/forums'],
    ['promotions', 'Promotions', 'xdg-open https://mail.google.com/mail/#category/promotions']
]
photos_actions = [
    ['photos', 'Photos', 'xdg-open https://photos.google.com'],
    ['sharing', 'Sharing', 'xdg-open https://photos.google.com/sharing'],
    ['for-you', 'For You', 'xdg-open https://photos.google.com/foryou'],
    ['print-store', 'Print Store', 'xdg-open https://photos.google.com/printstore'],
    ['albums', 'Albums', 'xdg-open https://photos.google.com/albums'],
    ['utilities', 'Utilities', 'xdg-open https://photos.google.com/managelibrary'],
    ['archive', 'Archive', 'xdg-open https://photos.google.com/archive'],
    ['trash', 'Trash', 'xdg-open https://photos.google.com/trash'],
]
calendar_actions = [
    ['new', 'New Event', 'xdg-open https://calendar.google.com/calendar/r/eventedit']
]
docs_actions = [
    ['new', 'New Document', 'xdg-open https://docs.google.com/create']
]
sheets_actions = [
    ['new', 'New Sheet', 'xdg-open https://sheets.google.com/create']
]
forms_actions = [
    ['new', 'New Form', 'xdg-open https://forms.google.com/create']
]
slides_actions = [
    ['new', 'New Presentation', 'xdg-open https://slides.google.com/create']
]
drawings_actions = [
    ['new', 'New Drawing', 'xdg-open https://drawings.google.com/create']
]
earth_actions = [
    ['launch', 'Launch Earth', 'xdg-open https://earth.google.com/web']
]

util.make_launcher('google-docs.desktop', 'Google Docs', 'xdg-open https://docs.google.com', "Google's document writer.", 'google-docs', categories=['Office'], actions=docs_actions)
util.make_launcher('google-sheets.desktop', 'Google Sheets', 'xdg-open https://sheets.google.com', "Google's spreadsheet editor.", 'google-sheets', categories=['Office'], actions=sheets_actions)
util.make_launcher('google-forms.desktop', 'Google Forms', 'xdg-open https://forms.google.com', "Google's form maker.", 'google-forms', categories=['Office'], actions=forms_actions)
util.make_launcher('google-slides.desktop', 'Google Slides', 'xdg-open https://slides.google.com', "Google's slideshow maker.", 'google-slides', categories=['Office'], actions=slides_actions)
util.make_launcher('google-drawings.desktop', 'Google Drawings', 'xdg-open https://drawings.google.com', "Google's art maker.", 'chrome-google-drawings', categories=['Office', 'Media', 'Graphics'], actions=drawings_actions)
util.make_launcher('google-calendar.desktop', 'Google Calendar', 'xdg-open https://calendar.google.com', "Google's calendar.", 'google-calendar', categories=['Network', 'Office'], actions=calendar_actions)
util.make_launcher('google-drive.desktop', 'Google Drive', 'xdg-open https://drive.google.com', "Online drive.", 'google-drive', categories=['Network', 'Utility', 'Office'], actions=drive_actions)
util.make_launcher('google-mail.desktop', 'Gmail', 'xdg-open https://mail.google.com', "Google's email service.", 'gmail', categories=['Network', 'Email', 'Office', 'InstantMessaging'], actions=mail_actions)
util.make_launcher('google-photos.desktop', 'Google Photos', 'xdg-open https://photos.google.com', "Google's photo library.", 'google-photos', categories=['Graphics', 'Media'], actions=photos_actions)
util.make_launcher('google-messages.desktop', 'Messages', 'xdg-open https://messages.google.com', "Google's SMS service.", 'google-messages', categories=['Network', 'Office', 'InstantMessaging'])
util.make_launcher('google-hangouts.desktop', 'Google Hangouts', 'xdg-open https://hangouts.google.com', "Google's instant message service.", 'google-hangouts', categories=['Network', 'Office', 'InstantMessaging'])
util.make_launcher('google-maps.desktop', 'Google Maps', 'xdg-open https://maps.google.com', "Google's map service.", 'google-maps', categories=['Utility'])
util.make_launcher('google-earth.desktop', 'Google Earth', 'xdg-open https://earth.google.com', "Around the world with Google.", 'google-earth', categories=['Utility'], actions=earth_actions)
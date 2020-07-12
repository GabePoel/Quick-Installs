import util

util.make_launcher('microsoft-word.desktop', 'Microsoft Word', 'xdg-open https://office.com/launch/word', "Microsoft's document writer.", 'ms-word', categories=['Office'])
util.make_launcher('microsoft-excel.desktop', 'Microsoft Excel', 'xdg-open https://office.com/launch/excel', "Microsoft's spreadsheet editor.", 'ms-excel', categories=['Office'])
util.make_launcher('microsoft-powerpoint.desktop', 'Microsoft PowerPoint', 'xdg-open https://office.com/launch/powerpoint', "Microsoft's presentation maker.", 'ms-powerpoint', categories=['Office'])
util.make_launcher('microsoft-onenote.desktop', 'Microsoft OneNote', 'xdg-open https://onenote.com', "Microsoft's note taker.", 'ms-onenote', categories=['Office'])
util.make_launcher('microsoft-onedrive.desktop', 'Microsoft OneDrive', 'xdg-open https://onedrive.live.com', "Microsoft's cloud drive.", 'ms-onedrive', categories=['Office'])
util.make_launcher('microsoft-outlook.desktop', 'Microsoft Outlook', 'xdg-open https://outlook.live.com', "Microsoft's email portal.", 'ms-outlook', categories=['Office'])
util.make_launcher('microsoft-office.desktop', 'Microsoft Office', 'xdg-open https://office.com', "Microsoft's complete office suite.", 'ms-office', categories=['Office'])

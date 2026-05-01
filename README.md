# Mewo Manager
### The first password manager to require a password to access your passwords!
This is a password manager I made cuz why not? 
### Building process
This has only been tested on linux, so if it doesn't work, make an issue on it and ima try to fix is.<br>
Building for your current operating system (has only been tested on linux for linux):<br>
<code>python -m PyInstaller --onefile --noconsole --add-data="jetbrainsmononerd.ttf:." mewomanager.py</code><br>
<br>
Building on windows:<br>
<code>python -m PyInstaller --onefile --noconsole --add-data "jetbrainsmononerd.ttf;." mewomanager.py</code><br>
Building for windows on linux/mac requires a windows vm, or wine. I recommend wine cuz its easier to setup but
tbh i just used chatgpt to help cuz i was lazy.

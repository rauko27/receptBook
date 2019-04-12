#!C:\PycharmProjects\receptBook\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'tornadoweb==0.0.15','console_scripts','tornadoweb_init'
__requires__ = 'tornadoweb==0.0.15'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('tornadoweb==0.0.15', 'console_scripts', 'tornadoweb_init')()
    )


#!/usr/bin/env python3


import sys
import os

thumbnail = sys.argv[1]


if (os.path.getsize(thumbnail) == 0):
    print('Tiedosto on tyhjä')

else:
    print('Tiedostossa on jotain tavaraa')
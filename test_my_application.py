
#!/usr/bin/env python3

import requests
import sys
import os
import json

thumbnail = sys.argv[1]


if (os.path.getsize(thumbnail) == 0):
    print('Tiedosto on tyhjä')

else:
    print('Tiedostossa on jotain tavaraa')
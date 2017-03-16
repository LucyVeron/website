activate_this = 'home/majortom6/public_html/cgi_bin'
execfile(activate_this, dict(__file__=activate_this))

#!/usr/bin/python
import sys

sys.path.insert(0, 'home/majortom6/public_html/cgi_bin');
from server import app as application

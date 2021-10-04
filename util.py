

import aqt
try:
    # below or euqal 2.1.17
    from anki import version
except:
    # above 2.1.17
    from anki.buildinfo import version
#
# Utilities
#
def point_ver():
    'look up anki version ie 46'
    
    return int(version.split('.')[-1])

def setting(key):
    defaults = {
         'syncaddr':'http://127.0.0.1:27701/',
    }

    try:
        return aqt.mw.addonManager.getConfig(__name__).get(key, defaults[key])
    except:
        raise Exception('setting {} not found'.format(key))

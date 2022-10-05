from . import util
point_ver=util.point_ver()
sync_addr=util.setting('syncaddr')
if not sync_addr.endswith('/'):
    sync_addr+='/'
    
if point_ver<28:
    import anki.sync, anki.hooks, aqt

    addr = sync_addr # put your server address here
    anki.sync.SYNC_BASE = "%s" + addr
    def resetHostNum():
        aqt.mw.pm.profile['hostNum'] = None
    anki.hooks.addHook("profileLoaded", resetHostNum)
elif point_ver>=28:
    import os

    addr = sync_addr # put your server address here
    os.environ["SYNC_ENDPOINT"] = addr + "sync/"
    os.environ["SYNC_ENDPOINT_MEDIA"] = addr + "msync/"
    # set max upload limit
    # 5G
    os.environ["MAX_UPLOAD_MEGS_UNCOMP"] =str(1024*5)
    # 3 G
    os.environ["MAX_UPLOAD_MEGS_COMP"] =str(1024*3)

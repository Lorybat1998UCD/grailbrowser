import os

# XXX Unix specific stuff

def getgraildir():
    return getenv("GRAILDIR") or os.path.join(gethome(), ".grail")

def gethome():
    try:
	home = getenv("HOME")
	if not home:
	    import pwd
	    user = getenv("USER") or getenv("LOGNAME")
	    if not user:
		pwent = pwd.getpwuid(os.getuid())
	    else:
		pwent = pwd.getpwnam(user)
	    home = pwent[6]
	return home
    except (KeyError, ImportError):
	return os.curdir

def getenv(s):
    if os.environ.has_key(s): return os.environ[s]
    return None
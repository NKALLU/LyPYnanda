#!/usr/bin/python
# system information

import subprocess

#getting kernel info

uname = "uname"
uname_arg = "-a"
print ("Gathering system infor with %s command:\n") % uname
subprocess.call([uname, uname_arg])

#getting disk space

diskspace= "df"
diskspace_arg= "-h"
print ("Gathering system infor with %s command:\n") % diskspace
subprocess.call([diskspace,diskspace_arg])



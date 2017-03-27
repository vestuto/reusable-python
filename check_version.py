from __future__ import print_function
import sys

ver_tup = sys.version_info
ver_str = sys.version
exe_path = sys.executable

if "Continuum Analytics" in ver_str:
	anaconda_found = True
else:
	anaconda_found = False

msg_0 = "Python version check:"
msg_1 = "    Version: {}.{}.{}"
msg_2 = "    Path: {}"
msg_3 = "    Description: {}"
msg_4 = "    Anaconda found: {}"
msg_5 = "        If Anaconda was not found, \n        please review the instructions in tutorial_setup.md"

print("\n\n")
print(msg_0)
print(msg_1.format(*ver_tup))
print(msg_2.format(exe_path))
print(msg_3.format(ver_str.replace("\n","\n    ")))
print(msg_4.format(anaconda_found))
if not anaconda_found:
    print(msg_5)
print("\n\n")
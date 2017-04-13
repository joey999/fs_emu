import subprocess

root = '/home/joey/fs_emu/'
mountdir = '/home/joey/mountdir/'

proc = subprocess.Popen(['python3.5', '/home/joey/fs_emu/fs_driver.py', '%s' % root, '%s' % mountdir])

input('/>>')
# основной код

subprocess.Popen.terminate(proc)
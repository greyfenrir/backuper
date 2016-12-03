#!/usr/bin/python
from sys import argv
from subprocess import call

priority = ['commander', 'general', 'colonel']

# all paths must be set from home dir
files = {   priority[0]:
                ['tmp/2/target_d'],
            priority[1]:
                [''],
            priority[2]:
                ['']}

def get_arch_name():
    return 'archive'

def show_usage():
    print('Usage: arc -b|-r')
    exit()

def backup(i):
    end = i + '.tar'
    print('Backup:')
    cmd = "tar --create --ignore-failed-read --listed-incremental %s --file %s -C ~ %s"
    call(cmd % ('arc.inc', get_arch_name()+end, files['commander'][0]), shell=True)
    print('done.')
    exit()

def restore(i):
    print('Restore:')
    cmd = "tar --extract --listed-incremental /dev/null --file %s%s"
    call(cmd % (get_arch_name(), i+'.tar'), shell=True)
    print('done.')
    exit()

# >>>>>>>>>>>>> start <<<<<<<<<<<<<<<<<
if len(argv) > 1 :
    if argv[1] == '-b':
        backup(argv[2])
    elif argv[1] == '-r':
        restore(argv[2])

show_usage()

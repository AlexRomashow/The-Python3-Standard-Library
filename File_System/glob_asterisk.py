import glob

for name in sorted(glob.glob('*.py')):
    print(name)

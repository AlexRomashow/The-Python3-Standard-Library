import enum

BugStatus = enum.Enum(value='BugStatus', 
    names=('fix_released fix_commited in_progress wont_fix invalid inpomplete new'),)
print('Member: {}'.format(BugStatus.new))

print('\nAll members:')
for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))

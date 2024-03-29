import mailbox
import os

print('Before:')
mbox = mailbox.Maildir('Example')
mbox.lock()
try:
    for message_id, message in mbox.iteritems():
        print('{:6} "{}"'.format(message.get_subdir(),
                                message['subject']))
        message.set_subdir('cur')
        # Обновление сообщения
        mbox[message_id] = message
finally:
    mbox.flush()
    mbox.close()

print('\nAfter:')
mbox = mailbox.Maildir('Example')
for message in mbox:
    print('{:6} "{}"'.format(message.get_subdir(),
                        message['subject']))
print()
for dirname, subdirs, files in os.walk('Example'):
    print(dirname)
    print('Directories:', subdirs)
for name in files:
    fullname = os.path.join(dirname, name)
    print(fullname)

import mailbox

mbox = mailbox.mbox('example.mbox')
for message in mbox:
    print(message['subject'])

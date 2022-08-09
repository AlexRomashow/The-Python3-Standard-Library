import smtplib

server = smtplib.SMTP('mail')
server.set_debuglevel(True) # отображать информацию
                            # о соединении c сервером
try:
    dhellmann_result = server.verify('dhellmann')
    notthere_result = server.verify('notthere')
finally:
    server.quit()

print('dhellmann:', dhellmann_result)
print('notthere :', notthere_result)

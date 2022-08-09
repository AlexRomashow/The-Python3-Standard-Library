import smtpd
import anyncore

server = smtpd.PureProxy(('127.0.0.1', 1025), ('mail', 25))
asyncore.loop()

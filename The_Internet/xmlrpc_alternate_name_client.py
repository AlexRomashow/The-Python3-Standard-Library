import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:9000')
print('dir():', proxy.dir('/tmp'))
try:
    print('\nlist_contents():', proxy.list_contents ('/tmp'))
except xmlrpc.client.Fault as err:
    print('\nERROR:', err)

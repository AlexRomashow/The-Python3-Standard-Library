import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:9000')
print('BEFORE      :', 'EXAMPLE' in proxy.dir.list('/tmp'))
print('CREATE      :', proxy.dir.create('/tmp/EXAMPLE'))
print('SHOULDEXIST :', 'EXAMPLE' inproxy.dir.list('/tmp'))
print('REMOVE      :', proxy.dir.remove('/tmp/EXAMPLE'))
print('AFTER       :', 'EXAMPLE' in proxy.dir.list('/tmp'))

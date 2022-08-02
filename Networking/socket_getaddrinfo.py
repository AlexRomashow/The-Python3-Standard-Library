import socket

def get_constants(prefix):
    """Создать словарь, сопоставляющий константы
    модуля socket c их именами.
    """
    return {
        getattr(socket, n): n
        for n in dir(socket)
        if n.startswith(prefix)
    }

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

for response in socket.getaddrinfo('www.python.org', 'http'):

    # Распаковка кортежа ответа
    family, socktype, proto, canonname, sockaddr = response

    print('Family:        ', families[family])
    print('Type:          ', types[socktype])
    print('Protocol:      ', protocols[proto])
    print('Canonical name:', canonname)
    print('Socket address:', sockaddr)
    print()






import socket

def get_constants(prefix):
    """
    Create discitonary mapping socket module constants to their names.
    """
    return dict((getattr(socket, n), n)
                for n in dir(socket)
                if n.startswith(prefix)
                )


protocols = get_constants('IPPROTO_')
print protocols

for name in ['icmp', 'udp', 'tcp']:
    proto_num = socket.getprotobyname(name)
    const_name = protocols[proto_num]
    print '%4s -> %2d (socket.%-12s = %2d)' % \
            (name, proto_num, const_name, getattr(socket, const_name))

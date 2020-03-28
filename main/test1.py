import socket

if __name__ == '__main__':
    # print(socket.gethostbyname('f7ds.liberation.fr'))
    # print(socket.gethostbyname('www.liberation.fr'))
    add = socket.getfqdn('eule1.pmu.fr')
    add1 = socket.getfqdn('www.liberation.fr')
    add2 = socket.gethostbyaddr(socket.gethostbyname('f7ds.liberation.fr'))
    print("add: ", add)
    print("add1: ", add1)
    print("add2: ", add2)

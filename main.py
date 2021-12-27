clients = 'Zaier,Agustina,Kiara,'


def create_client(client_name):
    global clients
    clients += client_name
    
    _add_comma()

def list_clients():
    global clients
    print(clients)

def _add_comma():
    global clients
    clients += ','


if __name__ == '__main__':

    print(clients)
    create_client('Ruru')
    list_clients()

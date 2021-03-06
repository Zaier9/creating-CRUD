import csv
import os


CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']

clients = []


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)



def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    
    else:
        print("Client already is in the client's list")


def list_clients():
    print('uid | name | company | email | position ')
    print('*' * 50)

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))


def updated_client(client_name, updated_client):
    global clients

    if len(clients) - 1 >= client_name:
        clients[client_name] = updated_client
    else:
        print("Client is not in client's list")


def delete_client(client_name):
    global clients
    for idx, client in enumerate(clients):
        if idx == client_name:
            del clients[idx]
            break


def search_client(client_name):

    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _get_client_name(message='What is the client {}? --> '):
    field = None

    while not field:
        field = input(message.format(client_name))

    return field


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }
    return client


def _print_welcome():
    print('WELCOME TO PLATZI VANTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')

if __name__ == '__main__':

    _initialize_clients_from_storage()
    _print_welcome()
    
    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position')
        }
        create_client(client)
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        update_name = input("What is your client name? --> ")

        updated_client(client_name, update_name)
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print("The client is in the client's list")
        else:
            print("The client: {} is not in client's list".format(client_name))
    else:
        print('Invalid command')

    _save_clients_to_storage()

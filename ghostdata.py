from src.core import GhostData
from src.input import get_input

def main():
    options = get_input()
    file_name = options.o

    ghost = GhostData()

    if options.domain:
        domain = options.domain
        html = ghost.get_data_using_domain(domain)
        usernames, passwords = ghost.parse_data(html)
        if len(usernames) != 0 and len(passwords) != 0:
            ghost.export_data(usernames, passwords, file_name)
    if options.username:
        username = options.username
        html = ghost.get_data_using_username(username)
        usernames, passwords = ghost.parse_data(html)
        if len(usernames) != 0 and len(passwords) != 0:
            ghost.export_data(usernames, passwords, file_name)
    if options.password:
        password = options.password
        html = ghost.get_data_using_password(password)
        usernames, passwords = ghost.parse_data(html)
        if len(usernames) != 0 and len(passwords) != 0:
            ghost.export_data(usernames, passwords, file_name)
main()


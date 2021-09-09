import requests
import re

class GhostData:
    def __init__(self):
        self.domain = 'http://pwndb2am4tzkvold.onion/'
        self.data = {
            'luser': '',
            'domain': '',
            'luseropr': '0',
            'domainopr': '0',
            'submitform': 'em'
        }

        self.password_form = {
            'password': '',
            'submitform': 'pw'
        }

        self.session = requests.session()
        self.session.proxies = {
        'http': 'socks5h://localhost:9050',
        'https':'socks5h://localhost:9050'
        }
        
    
    def get_data_using_domain(self, domain):
        self.email_domain = domain
        self.data['domain'] = self.email_domain
        html = self.session.post(self.domain, data=self.data).text
        return html
        
    def get_data_using_password(self, password):
        self.password = password
        self.password_form['password'] = self.password
        html = self.session.post(self.domain, data=self.password_form).text
        return html

    def get_data_using_username(self, username):
        self.data['luser'] = username
        html = self.session.post(self.domain, data=self.data).text
        return html

    def parse_data(self, html):
        raw_usernames = re.findall(r'\[luser\] =>.+', html)
        raw_passwords = re.findall(r'\[password\] =>.+', html)
        domains = re.findall(r'\[domain\] =>.+', html)
        

        domains = [i.split()[2] for i in domains]
        filtered_usernames = [raw_usernames[i].split()[2] + '@' + domains[i] for i in range(len(raw_usernames))]
        filtered_passwords = [i.split()[2] for i in raw_passwords]
        filtered_usernames.pop(0)
        filtered_passwords.pop(0)

        return filtered_usernames, filtered_passwords
        
    def export_data(self, usernames, passwords, output_f):
        with open(output_f + '.txt', 'w') as f:
            for i in range(len(usernames)):
                f.write(usernames[i]+':'+passwords[i]+'\n')

    


# ghost = GhostData()
# html = ghost.get_data_using_username('thithi.c.aguiar')
# usernames, passwords = ghost.parse_data(html)
# if len(usernames) != 0:
#     ghost.export_data(usernames, passwords, 'test264')
# else:
#     print('Couldn\'t find any results.')
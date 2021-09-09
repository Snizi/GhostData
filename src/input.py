import argparse


def get_input():

    parser = argparse.ArgumentParser(description="Search for credentials in the Dark Web")
    parser.add_argument('-o', help="file name to output the data")
    parser.add_argument('--domain', help="keyword to search for credentials using a domain")
    parser.add_argument('--username', help="keyword to search for credentials using the username")
    parser.add_argument('--password', help="keyword to search for credentials using a password")

    return parser.parse_args()
    

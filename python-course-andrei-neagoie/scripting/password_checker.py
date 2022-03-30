import sys
import hashlib
import requests


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}. Check the api and try again")
    return res


def get_password_leak_count(hashes, hash_to_check):
    # Hashes is the list, of hashes that starts with
    # the first_5_chars that we provided
    # Hash_to_check is actually tail
    hashes = (line.split(':') for line in hashes.text.splitlines())
    # we have converted it into a tuple, that has split by ":",
    # first is hash, and second is count in string
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # start from zero, to the fifth character, start from fifth char, to the end,
    first_5_chars, tail = sha1_password[:5], sha1_password[5:]
    response = request_api_data(first_5_chars)
    return get_password_leak_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"{password} was found {count} times... you should probably change your password")
        else:
            print(f"{password} was NOT found. Carry on!")


if __name__ == '__main__':
    # pass the arguments except first one, that is the name of this file
    sys.exit(main(sys.argv[1:]))

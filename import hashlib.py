import hashlib
import itertools
import string

target_hash = hashlib.md5("abc".encode()).hexdigest()
print("Target Hash:", target_hash)

chars = string.ascii_lowercase  # a–z

def crack_hash():
    for length in range(1, 4):  
        for attempt in itertools.product(chars, repeat=length):
            passwd = "".join(attempt)
            attempt_hash = hashlib.md5(passwd.encode()).hexdigest()

            if attempt_hash == target_hash:
                return passwd

found = crack_hash()
print("Password Found:", found)

import base64
import hashlib
import random

def generate_passkey():
    # Generate a random number between 1 and 1000, then hash it using MD5
    random_number = str(random.randint(1, 1000))
    return hashlib.md5(random_number.encode()).hexdigest()

# Encodes email: first Base64, then ASCII Hex
def encode_email(email):
    base64_encoded = base64.b64encode(email.encode()).decode()  # to base64 string
    ascii_hex_encoded = base64_encoded.encode().hex()           # convert to ASCII hex
    return ascii_hex_encoded

# Decodes from ASCII Hex -> Base64 -> original email
def decode_email(encoded_email):
    base64_string = bytes.fromhex(encoded_email).decode()
    email = base64.b64decode(base64_string).decode()
    return email

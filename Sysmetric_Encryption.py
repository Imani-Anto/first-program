# Symmetric Encryption Implementation using Fernet (AES)
from cryptography.fernet import Fernet

# Step 1: Define the message
message = "Symmetric Encryption using Python"
print("The original message:", message)

# Step 2: Generate a secret key
# In symmetric encryption, the same key is used for both processes
key = Fernet.generate_key()
secret_key = Fernet(key)

# Step 3: Encrypt the data
cipher_text = secret_key.encrypt(message.encode())
print("The encrypted (Ciphertext):", cipher_text)

# Step 4: Decrypt the data
decrypted_text = secret_key.decrypt(cipher_text).decode()
print("Decrypted (Plaintext):", decrypted_text)
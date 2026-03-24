import hashlib

# 1. The user's chosen password
password = "ULKstudent@2026"

# 2. Convert the string to bytes and apply SHA-256 hashing
# SHA-256 is a standard hashing algorithm used globally
password_bytes = password.encode()
hash_object = hashlib.sha256(password_bytes)
password_hash = hash_object.hexdigest()

print(f"Original Password:", password)
print(f"Stored Hash (SHA-256):", password_hash)

# 3. Demonstration of verification
attempt = "ULKstudent@2026"
attempt_hash = hashlib.sha256(attempt.encode()).hexdigest()

if attempt_hash == password_hash:
    print("Login Successful: Hashes match!")
else:
    print("Login Failed: Hashes do not match.")
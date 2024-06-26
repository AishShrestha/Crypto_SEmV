import hashlib

md5hasher = hashlib.md5(b'alish')
alice_hash = md5hasher.hexdigest()
print("Hash of text , alice is : \n",alice_hash)

md5hasher = hashlib.md5(b'ALISH')
alice_hash1 = md5hasher.hexdigest()
print("Hash of text , alice is : \n",alice_hash1)

md5hasher = hashlib.md5(b'bob')
bob_hash = md5hasher.hexdigest()
print("Hash of text , alice is : \n",bob_hash)
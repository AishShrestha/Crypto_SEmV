# WAP to craete MD5 hash

import hashlib

# md5hasher = hashlib.md5()
# hash5 = md5hasher.hexdigest()
# print("Md5 hash is : ", hash5)


print("SHA-1 has word alice is :\n,",hashlib.sha1(b'alice').hexdigest())
print("SHA-256 has word alice is :\n,",hashlib.sha256(b'alice').hexdigest())
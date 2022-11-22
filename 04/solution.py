import hashlib

data = "yzbqklnj"


nonce = 0
while 1:
    md5_hash = hashlib.md5((data + str(nonce)).encode('utf-8')).hexdigest()
    if md5_hash.startswith('00000'):
        print("Part 1:", nonce)
        break
    nonce += 1


while 1:
    md5_hash = hashlib.md5((data + str(nonce)).encode('utf-8')).hexdigest()
    if md5_hash.startswith('000000'):
        print("Part 2:", nonce)
        break
    nonce += 1

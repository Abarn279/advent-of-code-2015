from hashlib import md5

inp = 'yzbqklnj'

i = 0
while True:
    hsh = md5(str.encode(f"{inp}{str(i)}")).hexdigest()
    if hsh.startswith("000000"):
        print(i)
        break
    i += 1
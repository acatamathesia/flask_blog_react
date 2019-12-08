import hashlib

def md5_pass(password):
    m = hashlib.md5()
    m.update(password.encode("utf-8"))
    return m.hexdigest()

if __name__ == "__main__":
    print(md5_pass("123456"))
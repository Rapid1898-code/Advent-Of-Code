import hashlib

str = "abcdef609043"
result = hashlib.md5 (str.encode ())
test = result.hexdigest ()
print(test)
print(test[0]== "0")

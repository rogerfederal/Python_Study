import base64

result = base64.b64encode(b'username:password')
result2 = base64.b64decode('passcode')
print(result)
print(result2)
#Hash something

import hashlib 

mystring = 'python is fun!'
print('Your string is:',mystring)

myhash =hashlib.sha256(mystring.encode())

print('your sha256 hash is:', myhash.hexdigest())
print('The length of your hash is:', len(myhash.hexdigest()))
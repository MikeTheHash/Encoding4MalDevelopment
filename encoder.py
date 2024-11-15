from lib_encoding import encode
from lib_encoding import decode

print("Encode: 1\nDecode: 2")
var = input("Select >>> ")
if(var == "1"):
    ivar = input("text >>> ")
    print(encode(ivar))
else:
    ivar1 = input("text >>> ")
    print(decode(ivar1))

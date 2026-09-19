var = "3/4"
print (var)
var = "j"
print (var)
var = "\u0031\u0030"
print (var)
#encode and decode
string = "Hello"
tobytes = string.encode('utf-8')
print (tobytes)
string = tobytes.decode('utf-8')
print (string)
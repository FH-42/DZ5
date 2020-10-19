#def low(text):
 #   return text.lower()
#input = low(input())
#print(input)
 #def up(text):
 #    return text.upper()
#input = up(input())
#print(input)
def low(text):
    return text.lower()
def up(text):
    return text.upper()
a = ["Hello World"]
b = ["Hello World", "London is the capital of Great Britain"]
lowerr = list(map(low, a))
uperr = list(map(up, b))
print (lowerr, uperr)
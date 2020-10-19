def shouter(a):
    L = []

    for c in range(1, a + 1):

            if (c % fizz == 0) and (c % buzz == 0):
                L.append('FB')#print ("FB")
            elif c % fizz == 0:
                L.append('F')#print("F")#
            elif c % buzz == 0:
                L.append('B')#print ("B")#
            else:
                L.append(c)#print(c)#
    G = (': ' .join(map(str, L)))
    print(G)
#print(shouter(a))
fizz = int(input("Enter first number"))
buzz = int(input("Enter second number"))
a = int(input("Enter the third one"))
shouter(a)



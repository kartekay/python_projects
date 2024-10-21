x=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(string, move):
    encodedtxt=""
    for i in string:
       encodedtxt+=x[x.index(i)+int(move)]
    return encodedtxt
def decode(string,move):
    decoded=""
    for i in string:
        decoded+=x[x.index(i)-int(move)]
    return decoded
while True:
 a= str(input("Enter your text here :"))
 b= int(input("Enter number of caesar cypher here : "))
 c= input("Any for encode 1 for decode : ")
 if c==1:
    print(decode(a,b))
 else:
    print(encode(a,b))

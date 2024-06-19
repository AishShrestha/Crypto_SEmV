#Reverse Cipher
msg = input("Input your message: ")
n= len(msg)
reverseMsg = ''
i=n-1
while(i>=0):
    reverseMsg = reverseMsg +msg[i]
    i = i-1
print("Reverse cipher of message is : ", reverseMsg)
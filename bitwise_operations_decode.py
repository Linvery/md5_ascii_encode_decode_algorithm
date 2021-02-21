import base64
ciphertext = ['96','65','93','123','91','97','22','93','70','102','94','132','46','112','64','97','88','80','82','137','90','109','99','112']

# ^是按位异或逻辑运算符 如：print(5^6)=3，print(5^3)=6

def decode(ciphertext):
    s=''
    ciphertext.reverse()
    for i in range(len(ciphertext)):
        ciphertext[i]=int(ciphertext[i])
        if i % 2 == 0:
            flag=chr((ciphertext[i]-10)^i)
        else:
            flag=chr((ciphertext[i]+10)^i)
        s+=flag    
    print(s)

decode(ciphertext)

 
#-*-coding:utf-8-*-
import base64
import hashlib

def encrypt(data,key):
    key=hashlib.md5(key.encode('utf-8')).hexdigest()

    data_len=len(data)

    x=0
    char1=''
    # char1 代表len(data)有多长，就取多少位key[x]
    for i in range(data_len):
        if x==len(key):
            x=0
        char1 += key[x]
        x+=1

    # data+char1 ascii相加后，在转换为字符串，最后进行base64运算
    str_text=''
    for i in range(data_len):
        str_text+=chr((ord(data[i]) + ord(char1[i])) % 128)
    return base64.b64encode(str_text.encode('utf-8'))

if __name__=='__main__':
    # data代表明文，key代表密钥
    data='test'
    key='ISCC'
    en_data=encrypt(data,key)
    print(en_data.decode('utf-8'))
#-*-coding:utf-8-*-
import base64
import hashlib

def decode_enans(en_data,key):
    str_text=base64.b64decode(en_data).decode('utf-8')
    key=hashlib.md5(key.encode('utf-8')).hexdigest()
    str_text_len=len(str_text)

    # base64前的en_data的长度 应等于 char1
    # 即str_text_len(加密后base64前的密文长度)=char1(截取密钥长度)=data_len(明文的长度)
    char1=''
    x=0
    for i in range(str_text_len):
        if x==len(key):
            x=0
        char1+=key[x]
        x=x+1

    # 相较于加密，从数学算式a+b=c，变成了a=c-b
    data=''
    for i in range(str_text_len):
        data += chr((ord(str_text[i]) - ord(char1[i])+128) % 128)
    return data

if __name__=='__main__':
    en_data='xxxxxxxxxxxxxxxxxxxxxxxxxx'
    key='ISCC'
    print(decode_enans(en_data,key))    
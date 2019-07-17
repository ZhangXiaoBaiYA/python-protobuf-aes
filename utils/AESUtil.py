# -*- coding:UTF-8 -*-
from Crypto.Cipher import AES
import base64

class AESCipher:
    def __init__(self,key,iv):
        self.key = key[0:16] #只截取16位作为KEY
        self.iv = iv[0:16] #16位字符，用于填充确是内容，可固定，也可随机生成

    def __pad(self,text):
        """
        填充方式，加密内容必须为16字节的倍数，若不是则使用self.iv进行数据填充
        """
        text_length = len(text)
        #计算需要填充字节数
        need_to_pad = AES.block_size - (text_length % AES.block_size)
        if need_to_pad == 0:
            need_to_pad = AES.block_size
        #需填充字节
        pad = chr(need_to_pad)
        return text + pad * need_to_pad

    def encrypt(self,raw):
        """
        这里进行加密
        """
        raw = self.__pad(raw)
        #生成加密器
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        #返回base64 unicode
        return base64.b64encode(cipher.encrypt(raw))

    def __unpad(self,text):
        """
        去除填充
        """
        pad = ord(text[-1])
        return text[:-pad]

    def decrypt(self,enc):
        """
        解密
        """
        #base64 进行解码
        enc = base64.b64decode(enc)
        #生成解码器
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        #返回去除填充的字符串
        return self.__unpad(cipher.decrypt(enc))

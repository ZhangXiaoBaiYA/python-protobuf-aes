# -*- coding:UTF-8 -*-

from tutorial import User_pb2
from utils.AESUtil import AESCipher
from utils.HttpUtil import HttpUtil

#生成实例对象
login_req = User_pb2.LoginRequest()

#设置参数
login_req.username = "Lili"
login_req.password = "12345678"
login_req.platform = "test-platform"
login_req.type = User_pb2.Type.PHONE

print(login_req)

#生成实例
aes_cipher = AESCipher("cHB2U512A7cb7856","SE1fch8DQlugcKdV")
#数据加密
#将login_req 实例对象，转换为string
login_req_to_string=login_req.SerializeToString()
print("加密前")
print(login_req_to_string)
encrypt_str = aes_cipher.encrypt(login_req_to_string)
print(encrypt_str)


#解密
#decrypt_str = aes_cipher.decrypt(encrypt_str)
#print("加密后")
#print(decrypt_str)

#请求服务
http_util = HttpUtil("http://localhost:8092/","tradingchain_otc")

response = http_util.request("/user/validate-password",encrypt_str)

if response.status_code != 200 :
    print("请求异常")
else:
    #对返回内容进行解密(解密成proto对象)
    resp_proto = User_pb2.Response()
    #对返回内容进行解密
    decrypted = aes_cipher.decrypt(response.text)
    #解析成proto对象格式
    resp_proto.ParseFromString(decrypted)
    print(resp_proto)
    print(resp_proto.code)
    print(resp_proto.msg)


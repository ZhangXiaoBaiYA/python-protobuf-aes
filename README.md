# python-protobuf-aes
使用python和protobuf，对数据进行加密解密，请求服务。如何使用，请看test.py 测试文件
```python版本 2.7```

[示例说明](https://www.jianshu.com/p/f1e1fd104a05)


python3.6版本
```
#当使用python3.6运行时，会报以下错误。 因为在python3.6中 SerializeToString使用后得到的是二进制串数据类型
#这时，我们可以这样修改
TypeError: can't concat str to bytes
#在protobuf调用SerializeToString后，追加decode("utf-8")，转为字符串
req.SerializeToString().decode('utf-8')

# 遇到此问题
TypeError: ord() expected string of length 1, but int found
# 在加密解密类中，修改__unpad方法ord(chr(text[-1]))
```

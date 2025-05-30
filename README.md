# qqbot-ClockInAddon
Python实现的基于napcat的qq机器人 打卡签到插件（整活版）
### 使用方法
首先配置napcat（官网链接：https://napneko.github.io/guide/napcat ）

在网络配置中添加一个HTTP服务器并启用

token为`isuncy`

![alt text](doc/image-1.png)

![alt text](doc/image.png)

在settings.json中添加要监听的群组或个人的qq号

运行
```cmd
python main.py
```

即可使用。

可修改`main.py`与`imageHandler.py`来更改关键词和图片

效果图：
![效果图](/doc/f8929c716bbac4bb316159d653410bf.jpg)
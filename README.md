# MQTT Server

## 简介
这是一个基于Python的MQTT服务器后台，用于接收传感器数据和图像，并将其存储在SQLite数据库中。图像存储在固定文件夹中，数据库中保存图像路径索引。该项目还提供了一个Flask API，用于访问存储的数据。

## 文件结构
- `app.py`: 主Flask应用
- `mqtt_client.py`: MQTT客户端和消息处理
- `database.py`: 数据库初始化和操作
- `config.py`: 配置文件（如MQTT代理地址、端口等）
- `requirements.txt`: Python依赖包列表
- `README.md`: 项目说明文档
- `images/`: 存储接收到的图像

## 安装
```bash
pip install -r requirements.txt
```
### 参考csdn博客"Windows环境下安装配置Mosquitto服务及入门操作介绍"
# 运行方法：运行app.py初始化数据库和文件夹
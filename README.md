# Flask Hello World 示例

这是一个基于 [HelloFlask教程](https://github.com/helloflask/flask-tutorial) 的简单Flask Web应用程序示例。

## 功能特点

- 简单的路由处理
- HTML响应返回
- 开发模式调试支持

## 路由说明

- `/` - 主页，显示欢迎信息
- `/hello` - Hello页面，显示问候信息

## 快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/15022298816/flask-hello-world-demo.git
cd flask-hello-world-demo
```

### 2. 创建虚拟环境
```bash
python -m venv .venv
```

### 3. 激活虚拟环境
Windows:
```bash
.venv\Scripts\activate
```

Linux/macOS:
```bash
source .venv/bin/activate
```

### 4. 安装依赖
```bash
pip install flask python-dotenv
```

### 5. 运行应用
```bash
flask run
```

或者以调试模式运行：
```bash
flask run --debug
```

应用将在 `http://127.0.0.1:5000` 启动。

## 项目结构

```
flask-hello-world-demo/
├── app.py          # 主应用文件
├── .env            # 环境变量配置
├── .flaskenv       # Flask环境配置
├── .gitignore      # Git忽略文件
└── README.md       # 项目说明文档
```

## 学习资源

- [Flask官方文档](https://flask.palletsprojects.com/)
- [HelloFlask教程](https://github.com/helloflask/flask-tutorial)
- [Flask入门教程](http://helloflask.com/book/3)

## 许可证

本项目仅供学习参考使用。
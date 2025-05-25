from flask import Flask, render_template_string

app = Flask(__name__)

# 字符画狗头（使用等宽字体显示）
DOGE_ASCII = r"""
　　　　▄　　　　▄
　　　　▒▒▒▒▒▒▒
　　▌▒▒▒▒▒▒▒▒▒▐
　▄▀▒▀▀▀▀▀▀▀▀▀▒▀▄
▌▒▒▐　　　·　　·　▌
▌▒▒▌　·　  🐾　 · 
▌▒▒▐　　　·　　 · 
▀▄▒▒▌　　　　　　▄▀
　　▀▄▄▄▄▄▄▄▄▄▀


--------By Evan 2025/2/6

"""

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>EvanRay.dev</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <style>
        body {
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: #f0f2f5;
            font-family: Arial, sans-serif;
        }

        .content {
            text-align: center;
            max-width: 600px;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        h1 {
            color: #2c3e50;
            margin-bottom: 30px;
        }

        .ascii-art {
            white-space: pre;
            font-family: 'Courier New', monospace;
            font-size: 12px;
            color: #34495e;
            margin: 20px 0;
        }

        @media (orientation: portrait) {
            body {
                background: #e8f4f8;
            }
            .content {
                width: 90%;
            }
        }

        @media (orientation: landscape) {
            body {
                background: #f9f9f9;
            }
        }
    </style>
</head>
<body>
    <div class="content">
        <h1>evanray.dev is coming...</h1>
        <div class="ascii-art">{{ doge_ascii }}</div>
    </div>
</body>
</html>
"""


@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, doge_ascii=DOGE_ASCII)


if __name__ == '__main__':
    # SSL 证书路径配置
    ssl_context = (
        r'C:\certs\evanray.dev_nginx\evanray.dev_bundle.crt',  # 证书文件路径
        r'C:\certs\evanray.dev_nginx\evanray.dev.key'  # 私钥文件路径
    )

    # 启动 HTTPS 服务
    app.run(
        host='::',  # 监听所有 IPv6/IPv4 地址
        port=10,  # HTTPS 标准端口
        ssl_context=ssl_context,
        debug=False
    )
 # 确保 host 为 '::'
    # app.run(host='0.0.0.0', port=80)grams\Python\Python313\python.exe "C:\Users\34038\Personal\WebService\parking page.py"
    #  * Serving Flask app 'parking page'
    #  * Debug mode: off
    # WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    #  * Running on all addresses (::)
# 动态接口的封装
from flask import Flask,jsonify,request,json
from flask_cors import *
data = {'huhy':{'age':24,'sex':'女'},
        'liuer':{'age':12,'sex':'男'}
        }
app = Flask(__name__)#创建一个服务，赋值给APP__name__代表当前的python文件。把当前的python文件当做一个服务启动
@app.route('/get_user',methods=['get'])#指定接口访问的路径，支持什么请求方式get，post
#@app.route('/post_user',methods=['post'])#指定接口访问的路径，支持什么请求方式get，post
def get_user():
    return json.dumps(data, ensure_ascii=False)
CORS(app, supports_credentials=True)#解决跨域问题
app.run(port=8012,debug=True)

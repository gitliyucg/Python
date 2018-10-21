import mysql.connector
from flask import Flask,jsonify,request
from flask_cors import *

mydb = mysql.connector.connect(
    host="localhost",
    port="3316",
    user="root",
    passwd="",
    database="test"
)
mycursor = mydb.cursor()

app = Flask(__name__)#创建一个服务，赋值给APP
@app.route('/post_user',methods=['post'])#指定接口访问的路径，支持什么请求方式get，post
def post_user():#-----这里的函数名称可以任意取
    id = request.json.get('id')
    sql = 'SELECT * FROM user WHERE id = ' + str(id)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()     # fetchall() 获取所有记录
    return jsonify(myresult)#把字典转成json串返回

@app.route('/get_user',methods=['get'])#指定接口访问的路径，支持什么请求方式get，post
def get_user():#-----这里的函数名称可以任意取
    sql = 'SELECT * FROM user'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()     # fetchall() 获取所有记录
    return jsonify(myresult)#把字典转成json串返回
    return json.dumps(data, ensure_ascii=False)

CORS(app, supports_credentials=True)#解决跨域问题
app.run(port=8012,debug=True)

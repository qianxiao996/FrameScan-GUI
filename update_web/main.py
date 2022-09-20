#从app模块中导入app应用
from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from flask import send_from_directory
app = Flask(__name__)
app.config.from_object('config')
# 创建数据库对象
db = SQLAlchemy(app)
from models import *
# 查询时显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True

from flask import render_template
from flask import request, Response,Flask

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    User1 = User.query.filter(User.username == username).first()
    if User1 and User1.password ==password:
        return True
    else:
        return False

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

#下载文件
@app.route('/file/fs/<string:filename>',methods=['GET'])
@requires_auth 
def file_download(filename):
    try:
        return send_from_directory("file/", filename, as_attachment=True)
    except Exception as e:
        return str(e)
        return "文件路径出错或文件不存在"
#update
@app.route('/update/<string:name>',methods=['GET'])
@requires_auth 
def update(name):
    data = Update.query.filter(Update.type==name).order_by(Update.id.desc()).limit(10)
    result = []
    # print(Book_book_data.items() )
    for i in data:
        sing_book={}
        sing_book['id'] = i.id
        sing_book['version'] = i.version
        sing_book['description'] = i.description
        sing_book['is_delete_all'] = i.is_delete_all
        sing_book['file_url'] = i.file_url
        sing_book['file_password'] = i.file_password
        sing_book['windows_file_url'] = i.windows_file_url
        sing_book['linux_file_url'] = i.linux_file_url
        sing_book['update_time'] = i.update_time
        result.append(sing_book)
    # print(result)
    return jsonify(result)
    
if __name__=='__main__':
    app.run(debug=True)
from main import db
from datetime import datetime
'''定义模型，建立关系'''


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    username = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(100))
    create_time = db.Column(db.DateTime,default=datetime.now)

class Update(db.Model):
    __tablename__ = 'update'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    version = db.Column(db.String(100))
    title = db.Column(db.String(500))
    description = db.Column(db.String(5000))
    type = db.Column(db.String(500))
    is_delete_all = db.Column(db.BOOLEAN,default=False)
    file_password = db.Column(db.String(500))
    file_url = db.Column(db.String(500))
    windows_file_url = db.Column(db.String(500))
    linux_file_url = db.Column(db.String(500))
    update_time = db.Column(db.DateTime,default=datetime.now)
    
# 1. 增：

# 增加：
# User1 = User(title='aaa',content='bbb')
# db.session.add(User1)
# 事务
# db.session.commit()

# 2. 查：

# 查
# select * from User where User.title='aaa';
# User1 = User.query.filter(User.title == 'aaa').first()
# print 'title:%s' % User1.title
# print 'content:%s' % User1.content

# 3. 改：

# 改：
# 1. 先把你要更改的数据查找出来
# User1 = User.query.filter(User.title == 'aaa').first()
# 2. 把这条数据，你需要修改的地方进行修改
# User1.title = 'new title'
# 3. 做事务的提交
# db.session.commit()

# 4. 删：

# 删
# 1. 把需要删除的数据查找出来
# User1 = User.query.filter(User.content == 'bbb').first()
# 2. 把这条数据删除掉
# db.session.delete(User1)
# 3. 做事务提交
# db.session.commit()
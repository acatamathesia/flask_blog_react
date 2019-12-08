
from models import models
from utils import md5_pass
'''
    这里进行业务逻辑的构建和描述
'''
# find_user_username 根据用户查询用户信息
def find_user_username(username):
    user = models.User.query.filter(models.User.username==username).first()
    return user.to_dict()

# update_user_info 修改用户基本信息
def update_user_info(user):
    sel_user = models.User.query.filter(models.User.id == user.id).first()
    sel_user.nickname = user.nickname
    sel_user.img = user.img
    models.db.session.commit()

# update_user_password 根据用户id更新用户密码
def update_user_password(id,npass,opass):
    sel_user = models.User.query.filter(models.User.id == id).first()
    if sel_user.password != md5_pass.md5_pass(opass):
        raise Exception('用户旧密码错误！')
    sel_user.password = md5_pass.md5_pass(npass)
    models.db.session.commit()

# register 注册用户
def register(user):
    o_user = models.User.query.filter(models.User.username == user.username).first()
    if o_user != None:
        raise Exception('用户已存在！')
    user.password = md5_pass.md5_pass(user.password)
    models.db.session.add(user)
    models.db.session.commit()
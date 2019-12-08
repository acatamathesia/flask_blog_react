# charset = utf-8
import json
from services import user_service
from flask import Response,request
from models import models
from models.result import ResultResp
'''
    这里用于写有关于请求操作的接口
'''
# register 用于注册用户基本信息
def register():
    try:
        params = request.json
        user_service.register(models.User(None, params['username'], params['password'], params['nickname'], ""))
        return ResultResp(20000, '注册成功！', None).to_resp()
    except Exception as e:
        print(e)
        return ResultResp(50001, '注册失败！', None).to_resp()

# find_user_info 根据用户名查询用户信息
def find_user_info(username):
    try:
        user_info = user_service.find_user_username(username)
        return ResultResp(20000, '查询成功！', user_info).to_resp()
    except Exception as e:
        print (e)
        return ResultResp(50001, '查询失败！', None).to_resp()

# update_info 根据用户id修改用户信息
def update_info(id):
    try:
        params = request.json
        user_service.update_user_info(models.User(id, params['username'], params['password'], params['nickname'], ""))
        return ResultResp(20000, '修改用户信息成功', None).to_resp()
    except Exception as e:
        print(e)
        return ResultResp(50001,'修改用户信息失败', None).to_resp()

def update_password(id):
    try:
        params = request.json
        user_service.update_user_password(id, params['new_password'], params['old_password'])
        return ResultResp(20000, '修改密码成功', None).to_resp()
    except Exception as e:
        print(e)
        return ResultResp(50001, '修改密码失败', None).to_resp()
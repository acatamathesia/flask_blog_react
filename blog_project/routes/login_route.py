from flask import request, session
from app_config import app
from utils import md5_pass
from services import user_service
from models.result import ResultResp

@app.before_request
def check_is_login():
    if request.path[1:4] == 'pri' and session['login_user'] == None:
        return ResultResp(40015, "未登录", None).to_resp()
    else:
        print(request.path)

def login():
    try:
        params = request.json
        u = user_service.find_user_username(params["username"])
        if u is None:
            return ResultResp(40001, "用户账户不存在", None).to_resp()
        if u['password'] != md5_pass.md5_pass(params["password"]):
            return ResultResp(40002, "用户密码不正确", None).to_resp()
        session['login_user'] = u
        return ResultResp(20000, "登录成功", {"username": u['username'], "nickname": u['nickname'], "img": u['img']}).to_resp()
    except Exception as e:
        print(e)
        return ResultResp(50001, "系统维护中", None).to_resp()

def logout():
    try:
        if session['login_user'] is not None:
            session['login_user'] = None
            return ResultResp(20000, "退出成功！", None).to_resp()
        return ResultResp(40001, "用户未登录", None).to_resp()
    except Exception as e:
        print(e)
        return ResultResp(20000, "退出失败！", None).to_resp()

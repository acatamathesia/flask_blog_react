from flask import request, session
from models.models import Commont
from models.result import ResultResp
from services import com_services

def commont_page(page_num):
    params = request.json
    try:
        commonts = com_services.commont_page_usr(page_num, params['user_id'])
    except Exception as e:
        print(e)
        commonts = com_services.commont_page_art(page_num, params['article_id'])
    return ResultResp(20000, '查询成功', commonts).to_resp()

def insert_commont():
    try:
        params = request.json
        com_services.insert_commont(Commont(None, params['article_id'],
                                            session['login_user']['id'],
                                            session['login_user']['nickname'],
                                            params['content'],
                                            None, None))
        return ResultResp(20000, '回复成功！', None).to_resp()
    except Exception as e:
        print(e)
        return ResultResp(50001, '系统维护中', None).to_resp()

def delete_commont(id):
    try:
        com_services.delete_commont(id)
        return ResultResp(20000, '删除成功', None).to_resp()
    except Exception as e:
        print(e)
        return ResultResp(50001, '删除失败', None).to_resp()

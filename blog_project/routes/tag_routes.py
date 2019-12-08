from flask import request
from models.result import ResultResp
from models.models import Tag
from services import tag_services

def insert_tag():
    try:
        params = request.json
        tag_services.insert_tag(Tag(None, params["name"], params["order"]))
        return ResultResp(20000, "添加成功", None).to_resp()
    except Exception as e:
        print(e)
        return ResultResp(50001, "添加失败", None).to_resp()

def find_tag_page(page_num):
    try:
        params = request.json
        tag_list = tag_services.find_tag_page(page_num,params["keywords"])
        return ResultResp(20000, "查询成功", tag_list).to_resp()
    except Exception as e:
        print(e)
        return ResultResp(50001, "查询失败", None).to_resp()

def delete_tag(id):
    try:
        tag_services.delete_tag(id)
        return ResultResp(20000, "删除成功", None).to_resp()
    except Exception as e:
        print(e)
        return ResultResp(50001, "删除失败", None).to_resp()

def update_tag(id):
    try:
        params = request.json
        tag_services.update_tag(Tag(id, params["name"], params["order"]))
        return ResultResp(20000, "修改成功", None).to_resp()
    except Exception as e:
        print(e)
        return ResultResp(50001, "修改失败", None).to_resp()

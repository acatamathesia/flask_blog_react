import time
from models.models import Commont, db
from utils import model_json, page

def commont_page_art(page_num,article_id):
    commonts = Commont.query.filter(Commont.is_deleted == '0',Commont.article_id == article_id).all()
    commonts = page.Page.auto_page(commonts, page_num)
    commonts = model_json.list_to_json(commonts)
    return commonts

def commont_page_usr(page_num,user_id):
    commonts = Commont.query.filter(Commont.is_deleted == '0',Commont.user_id == user_id).date_format().all()
    commonts = page.Page.auto_page(commonts, page_num)
    commonts = model_json.list_to_json(commonts)
    return commonts

def insert_commont(commont):
    if type(commont) is not Commont:
        raise Exception('类型异常')
    commont.created_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    commont.is_deleted = '0'
    db.session.add(commont)
    db.session.commit()

def delete_commont(id):
    commont = Commont.query.filter(Commont.id == id).first()
    commont.is_deleted = "1"
    db.session.commit()

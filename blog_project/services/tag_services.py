from models.models import Tag, db
from utils import page, model_json

def find_tag_page(page_number,keywords):
    tag_list = Tag.query.filter(Tag.name.like("%"+keywords+"%")).order_by(Tag.id).all()
    tag_list = page.Page.auto_page(tag_list,page_number)
    tag_list = model_json.list_to_json(tag_list)
    return tag_list

def find_tag_info(id):
    tag = Tag.query.filter(Tag.id == id).first()
    return tag.to_dict()

def update_tag(tag):
    if tag.id == None:
        raise Exception("要修改的id不能为空")
    old_tag = Tag.query.filter(Tag.id == tag.id).first()
    old_tag.name = tag.name
    old_tag.order = tag.order
    db.session.commit()

def delete_tag(id):
    tag = Tag.query.filter(Tag.id == id).first()
    if tag == None:
        raise Exception("无法删除不存在的数据")
    db.session.delete(tag)
    db.session.commit()

def insert_tag(tag):
    if type(tag) is not Tag:
        raise Exception("数据类型异常，需要Tag，实际"+type(tag))
    db.session.add(tag)
    db.session.commit()


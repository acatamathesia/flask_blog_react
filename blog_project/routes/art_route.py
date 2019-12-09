from flask import request, session
from models.models import Article, ArticleContent
from models.result import ResultResp
from services import art_services

def insert_article():
    try:
        params = request.json
        art_services.insert_article(Article(None, params['title'], session['login_user']['id'], session['login_user']['nickname'], None,
                                            None, '0', params['tagId'], None),
                                    ArticleContent(None,params['content']))
        return ResultResp(20000, '添加成功', None).to_resp()
    except Exception as e:
        print(e)
        return ResultResp(50001,'添加失败！', None).to_resp()

def update_article(id):
    try:
        params = request.json
        art_services.update_article(Article(id, params['title'], None, None, None,
                                            None, '0', params['tagId'], None),
                                    ArticleContent(None,params['content']))
        return ResultResp(20000, '修改成功', None).to_resp()
    except Exception as e:
        print(e)
        return ResultResp(50001, '修改失败！', None).to_resp()

def delete_article(id):
    try:
        art_services.delete_article(id)
        return ResultResp(20000, '删除成功', None).to_resp()
    except Exception as e:
        print(e)
        return ResultResp(50001, '删除失败！', None).to_resp()

def article_info(id):
    try:
        all_art = art_services.article_info(id)
        return ResultResp(20000, '查询成功', all_art).to_resp()
    except Exception as e:
        return ResultResp(50001,'查询失败！', None).to_resp()

def article_page(page_num):
    try:
        params = request.json
        articles = art_services.article_page(page_num, params['keywords'])
        return ResultResp(20000, '查询成功', articles).to_resp()
    except Exception as e:
        return ResultResp(50001, '查询失败！', None).to_resp()

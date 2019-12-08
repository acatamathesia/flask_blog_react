from models.models import db, Article, ArticleContent, Tag
from utils.page import Page
from utils import model_json

import time

# 分页条件查询文章信息
def article_page(page_num, keywords):
    articles = Article.query.filter(Article.title.like("%"+keywords+"%")).order_by(Article.id).all()
    articles = model_json.list_to_json(articles)
    articles = Page.auto_page(articles,page_num)
    return articles

# 根据文章id查询文章信息包括文章内容
def article_info(id):
    article = Article.query.filter(Article.id == id).first()
    articleContent = ArticleContent.query.filter(ArticleContent.article_id == id).first()
    if article.is_deleted == "1":
        return {'msg':'文章已被删除！'}
    return {
        'article': article.to_dict(),
        'content': articleContent.to_dict()
    }

# 根据文章id假删除文章内容
def delete_article(id):
    article = Article.query.filter(Article.id == id).first()
    article.is_deleted = "1"
    db.session.commit()

# 根据文章id修改文章部分信息
def update_article(article,content):
    old_article = Article.query.filter(Article.id == article.id).first()
    old_articlecontent = ArticleContent.query.filter(ArticleContent.article_id == article.id).first()
    old_article.title = article.title
    old_article.update_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    old_article.tag_id = article.tag_id
    tag = Tag.query.filter(Tag.id == article.tag_id).first()
    old_article.tag_name = tag.name
    old_articlecontent.content = content.content
    db.session.commit()

# 添加文章信息
def insert_article(article, content):
    if type(article) is not Article or type(content) is not ArticleContent:
        raise Exception("期望类型是<class:Article>以及<class:ArticleContent>,但是您的输入不符合！")
    article.created_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    article.update_time = article.created_time
    article.is_deleted = '0'
    tag = Tag.query.filter(Tag.id == article.tag_id).first()
    article.tag_name = tag.name
    db.session.add(article)
    db.session.flush() # 获取刚保存的文章的id
    content.article_id = article.id
    db.session.add(content)
    db.session.commit()

if __name__=="__main__":
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

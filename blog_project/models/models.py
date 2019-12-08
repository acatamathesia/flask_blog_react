# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

'''
    当前文件用于保存项目中的实体类 也就是模型关系映射
'''

class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    user = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(6))
    created_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime)
    is_deleted = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    tag_id = db.Column(db.Integer)
    tag_name = db.Column(db.String(10))

    def __init__(self, id, title, user, username, created_time, update_time, is_deleted, tag_id, tag_name):
        self.id = id
        self.title = title
        self.user = user
        self.username = username
        self.created_time = created_time
        self.update_time = update_time
        self.is_deleted = is_deleted
        self.tag_id = tag_id
        self.tag_name = tag_name

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'user': self.user,
            'username': self.username,
            'created_time': self.created_time,
            'update_time': self.update_time,
            'is_deleted': self.is_deleted,
            'tag_id': self.tag_id,
            'tag_name': self.tag_name
        }


class ArticleContent(db.Model):
    __tablename__ = 'article_content'

    article_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)

    def __init__(self, article_id, content):
        self.article_id = article_id
        self.content = content

    def to_dict(self):
        return {
            'article_id': self.article_id,
            'content': self.content
        }

class Commont(db.Model):
    __tablename__ = 'commont'

    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(6))
    content = db.Column(db.String(255))
    created_time = db.Column(db.DateTime, nullable=False)
    is_deleted = db.Column(db.String(1), server_default=db.FetchedValue())

    def __init__(self, id, article_id, user_id,username, content, created_time, is_deleted):
        self.id = id
        self.article_id = article_id
        self.user_id = user_id
        self.username = username
        self.content = content
        self.created_time = created_time
        self.is_deleted = is_deleted

    def to_dict(self):
        return {
            'id':self.id,
            'article_id':self.article_id,
            'user_id':self.user_id,
            'username':self.username,
            'content':self.content,
            'created_time':self.created_time,
            'is_deleted':self.is_deleted
        }


class Tag(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    order = db.Column(db.Integer, nullable=False)

    def __init__(self, id, name, order):
        self.id = id
        self.name = name
        self.order = order

    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'order':self.order
        }

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    nickname = db.Column(db.String(6), nullable=False)
    img = db.Column(db.String(32))

    def __init__(self, id, username, password, nickname, img):
        self.id = id
        self.username = username
        self.password = password
        self.nickname = nickname
        self.img = img

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'nickname': self.nickname,
            'img': self.img
        }


if __name__ == '__main__':
    obj = User("1","1","1","1")
    print(obj.password)


from flask import Flask
from models import models

app = Flask(__name__)

# 配置session信息
app.config["SECRET_KEY"] = "testperson"

# 配置链接数据库的路径
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost:3306/blog_database'
# 配置每次修改后自动commit到数据库中
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

models.db.init_app(app)

from app_config import app
from routes import user_route, tag_routes, art_route, login_route
'''
    问题： 在这里定义文件后，虽然注册了路由，但是没有生效，导致404
    解决： 在app文件中引入route就可以了，相当于默认调用该文件组册了url路径，否则就不会生效
'''

### 登录操作
app.add_url_rule('/pub/login/', view_func=login_route.login, endpoint='login', methods=['POST'])
app.add_url_rule('/pri/logout/', view_func=login_route.logout, endpoint='logout', methods=['GET', 'POST'])

### 用户请求接口路径
app.add_url_rule('/pub/user/', view_func=user_route.register, endpoint='user_register', methods=['PUT'])
app.add_url_rule('/pri/user/<username>', view_func=user_route.find_user_info, endpoint='user_find', methods=['GET'])
app.add_url_rule('/pri/user/<int:id>', view_func=user_route.update_info, endpoint='user_update', methods=['POST'])
app.add_url_rule('/pri/user_ps/<int:id>', view_func=user_route.update_password, endpoint='user_update_password', methods=['POST'])

### 标签请求接口
app.add_url_rule('/pri/tag/', view_func=tag_routes.insert_tag, endpoint="tag_insert", methods=["PUT"])
app.add_url_rule('/pri/tag/<int:page_num>', view_func=tag_routes.find_tag_page, endpoint="tag_page", methods=["GET"])
app.add_url_rule('/pri/tag/<int:id>', view_func=tag_routes.delete_tag, endpoint='tag_delete', methods=["DELETE"])
app.add_url_rule('/pri/tag/<int:id>', view_func=tag_routes.update_tag, endpoint='tag_update', methods=['POST'])


### 文章请求接口
app.add_url_rule('/pri/art/', view_func=art_route.insert_article, endpoint="art_insert", methods=["PUT"])
app.add_url_rule('/pub/art/<int:page_num>', view_func=art_route.article_page, endpoint="art_page", methods=["GET"])
app.add_url_rule('/pri/art_inf/<int:id>', view_func=art_route.article_info, endpoint="art_info", methods=["GET"])
app.add_url_rule('/pri/art/<int:id>', view_func=art_route.delete_article, endpoint='art_delete', methods=["DELETE"])
app.add_url_rule('/pri/art/<int:id>', view_func=art_route.update_article, endpoint='art_update', methods=['POST'])


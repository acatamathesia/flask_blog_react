from flask import Flask
from app_config import route, app


if __name__ == '__main__':
    print("=====================================" * 2)
    print(app.url_map)
    print("====================================="*2)
    app.run()

# -*- coding:utf-8 -*-

"""
File Name: `__init__`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/13 14:07
"""

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from my_flask.config.default import Config

app = Flask(__name__)

app.config.from_object(Config)
# 创建1个SQLAlichemy实例
db = SQLAlchemy(app)


from .views import db_action, DbAction

app.register_blueprint(db_action)

view = Api(app)
view.add_resource(DbAction, '/db')

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
# -*- coding:utf-8 -*-

"""
File Name: `models`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/12 11:42
"""

from my_flask import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32), nullable=False)
    address = db.Column(db.String(80))
    old_password = db.Column(db.String(32), default='0')
    create_time = db.Column(db.DateTime, default=db.func.now())
    update_time = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return '<User %r, id %r>' % (self.username, self.id)


class ProjectInfo(db.Model):
    __tablename__ = 'project_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=db.func.now())
    update_time = db.Column(db.DateTime, onupdate=db.func.now())
    project_name = db.Column(db.String(50), nullable=False, unique=True)
    simple_desc = db.Column(db.String(100))

    def __repr__(self):
        return '<ProjectInfo %r, id %r>' % (self.project_name, self.id)


class SystemInfo(db.Model):
    __tablename__ = 'system_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=db.func.now())
    update_time = db.Column(db.DateTime, onupdate=db.func.now())
    system_name = db.Column(db.String(50), nullable=False)
    test_user = db.Column(db.String(50))
    dev_user = db.Column(db.String(50))
    publish_app = db.Column(db.String(50))
    simple_desc = db.Column(db.String(100))
    project_id = db.Column(db.Integer, db.ForeignKey('project_info.id'))
    project = db.relationship('ProjectInfo', backref=db.backref('systems'))

    def __repr__(self):
        return '<SystemInfo %r, id %r>' % (self.system_name, self.id)

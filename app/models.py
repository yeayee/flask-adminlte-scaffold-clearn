# -*- coding: utf-8 -*-


import json
from werkzeug.security import check_password_hash
from flask_login import UserMixin

from conf.config import config
import os


cfg = config[os.getenv('FLASK_CONFIG') or 'default']

class Users(UserMixin):
    
    def __init__(self, openId):
        self.openId = openId
        
    def get_id(self):
        return self.openId
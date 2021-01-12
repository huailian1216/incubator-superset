import jwt
from flask import request, redirect, make_response
from flask_login import login_user
from superset.security import SupersetSecurityManager
from flask_appbuilder.security.views import AuthDBView, expose


class CustomAuthDBView(AuthDBView):
    @expose('/login/', methods=['GET', 'POST'])
    def login(self):
        r = super(CustomAuthDBView, self).login()
        try:
             request.cookies.get('session')
        except Exception as e:
            pass
        return r


class CustomSecurityManager(SupersetSecurityManager):
    authdbview = CustomAuthDBView

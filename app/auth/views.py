from flask import render_template, redirect, request, url_for, flash
from . import auth
from .forms import LoginForm
from flask_login import login_user, logout_user, login_required
from ..models import Users
from app import login_manager


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # print(form.rememberme.data)
    if form.validate_on_submit():
        # try:
        openId= 'admin@intumu.com'
        if form.username.data == openId:
            user_obj = Users(openId)
            login_user(user_obj, form.rememberme.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash('用户名或密码错误')
        # except:
        #     flash('用户名或密码错误')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已退出登录')
    return redirect(url_for('auth.login'))

@login_manager.user_loader
def load_user(openId):
    return Users(openId)
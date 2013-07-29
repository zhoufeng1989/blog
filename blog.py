# -*- coding:utf-8 -*-
import web
from model import register_form, login_form, post_form
from user import register_user, get_user_by_name
from session import update_session, create_cookie
from content import get_articals

render = web.template.render('templates/', base='layout')


class index(object):
    def GET(self):
        articals = get_articals(order='create_time')
        return render.index(articals)


class post(object):
    def GET(self):
        f = post_form()
        return render.add_post(f)

    def POST(self):
        f = post_form()
        if not f.validates():
            return render.login(f)
        else:
            post_data = web.input()
            if add_post(title=post_data.title, content=post_data.content):
                return render.add_finish('添加成功')
            else:
                return render.add_finish('添加失败')


class login(object):
    def GET(self):
        f = login_form()
        return render.login(f.email.render(), f.password, f.submit)

    def POST(self):
        f = login_form()
        if not f.validates():
            return render.login(f)
        else:
            post_data = web.input()
            user = get_user_by_name(post_data.username)
            update_session(user)
            create_cookie(user)
            return render.login_finish('登陆成功')


class register(object):
    def GET(self):
        f = register_form()
        return render.register(f)

    def POST(self):
        f = register_form()
        if not f.validates():
            return render.register(f)
        else:
            post_data = web.input()
            username = post_data['username']
            password = post_data['password']
            email = post_data['email']
            if register_user(username, password, email):
                return render.reg_finish('注册成功')
            else:
                return render.reg_finish('注册失败,请重试')

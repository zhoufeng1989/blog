# -*- coding:utf-8 -*-
from web import form
from user import check_register, check_login

vpass = form.regexp(r".{3,20}$", '3到20个字符')
vemail = form.regexp(r".*@.*", '必须是合法的邮箱')

register_form = form.Form(
    form.Textbox('username', description='用户名'),
    form.Textbox('email', vemail, description='邮箱'),
    form.Textbox('password', vpass, description='密码'),
    form.Textbox('password2', description='重复密码'),
    form.Button('submit', type='submit', description='注册'),
    validators=[
        form.Validator('密码不匹配',
                       lambda i: i.password == i.password2),
        form.Validator('用户名或邮箱已存在',
                       lambda i: check_register(i.username, i.email))
    ]
)

login_form = form.Form(
    form.Textbox('email', form.notnull),
    form.Textbox('password', form.notnull),
    form.Button('submit', type='submit', description='登陆'),
    validators=[
        form.Validator('用户名或密码错误',
                       lambda i: check_login(i.username, i.password))
    ]
)


post_form = form.Form(
    form.Textbox('title', form.notnull, description='标题'),
    form.Textarea('content', form.notnull, description='内容'),
    form.Button('submit', type='submit', description='发表'),
    form.Button('reset', type='reset', description='清空')
)

import web
from db import db
from util import gen_password


def check_register(username, email):
    sql = (
        r'select count(*) as count from users where username = $username '
        r'or email = $email')
    result = db.query(sql, vars={'username': username, 'email': email})
    return result[0]['count'] == 0


def register_user(username, password, email):
    password, salt = gen_password(password)
    return db.insert(
        'users', **{
            'username': username, 'password': password,
            'email': email, 'salt': salt,
            'create_time': web.SQLLiteral("unix_timestamp(NOW())")}
    )


def check_login(username, password):
    user = get_user_by_name(username)
    print user
    sql = (
        r'select count(*) as count from users where username = $username '
        r'and password = md5(concat($salt, md5($password)))')
    result = db.query(
        sql, vars={'username': username, 'password': password,
                   'salt': user['salt']})
    return result[0]['count'] != 0


def get_user_by_name(username):
    sql = (
        r'select * from users where username = $username ')
    result = db.query(sql, vars={'username': username})
    if result:
        return result[0]
    else:
        return {}

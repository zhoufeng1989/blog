import web
import base64


def update_session(user):
    web.config._session.user_id = user['id']
    web.config._session.username = user['username']
    web.config._session.email = user['email']
    web.config._session.login = True


def create_cookie(user):
    auth = base64.encodestring(user.password + '|' + str(user.id))
    web.setcookie('blog_id', auth, 3600 * 24 * 7)

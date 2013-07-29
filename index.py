import web
import os
session_dir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'sessions')
prefix = 'blog'
urls = (
    '/', prefix + '.index',
    '/login', prefix + '.login',
    '/register', prefix + '.register',
    '/post', prefix + '.post',
)
app = web.application(urls, globals())
if web.config.get('_session') is None:
    session = web.session.Session(
        app, web.session.DiskStore(session_dir),
        initializer={'user_id': None})
    web.config._session = session
else:
    session = web.config._session
if __name__ == '__main__':
    app.run()

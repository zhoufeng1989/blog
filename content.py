import web
import time
from datetime import datetime
from db import db


def get_articals(**kwargs):
    result = db.select('articals',
                       what='title, content, update_time, create_time',
                       **kwargs)
    return result


def modify_post(**kwargs):
    action = kwargs.get('action', 'create')
    if action == 'create':
        kwargs['author_id'] = web.config.get('_session').user_id
        kwargs['create_time'] = kwargs['update_time'] = time.mktime(
            datetime.utcnow().timetuple())
        return db.insert('articals', **kwargs)
    elif action == 'update':
        artical_id = kwargs.pop('artical_id')
        #kwargs['update_time'] = time.mktime(
        return db.update('articals', **kwargs)

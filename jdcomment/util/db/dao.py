#!/usr/bin/env python
#-*- coding:utf8 -*-
# @Author: lisnb
# @Date:   2016-04-29T17:06:03+08:00
# @Email:  lisnb.h@hotmail.com
# @Last modified by:   lisnb
# @Last modified time: 2016-06-29T16:05:08+08:00



import os
import time
import random
import logging
import chardet
import MySQLdb
import threading

from dbconn import MySQLConn, MongoDBConn
from core.exceptions import ImproperlyConfigured
from sqlfactory import SQLFactory


class Dao(object):
    """docstring for DBUtil"""

    def __init__(self, config):
        super(Dao, self).__init__()
        self._config = config
        self.logger = logging.getLogger(__name__)
        self._setup()
        self._exec_error_desc_tmpl = 'Error in Dao, see the detail: %s.'

    def _setup(self):
        desc_tmpl = (
            '"%s" in MySQL settings is necessary for Dao.'
            'Please make sure it is well configured.'
        )
        if 'mysql' not in self._config:
            desc = desc_tmpl%'mysql'
            self.logger.error(desc)
            raise ImproperlyConfigured(desc)
        mysql = self._config['mysql']
        if 'default' not in mysql:
            desc = desc_tmpl%'default'
            self.logger.error(desc)
            raise ImproperlyConfigured(desc)
        default = mysql['default']
        if 'tables' not in default:
            desc = desc_tmpl%'default.ables'
            self.logger.error(desc)
            raise ImproperlyConfigured(desc)
        if 'connection' not in default:
            desc = desc_tmpl%'connection'
            self.logger.error(desc)
            raise ImproperlyConfigured(desc)
        tables = default['tables']
        self.table_table = {}
        table_db = {}
        for key in ['checkdup', 'app', 'channel']:
            if key not in tables:
                desc = desc_tmpl%('default.table.%s'%key)
                self.logger.error(desc)
                raise ImproperlyConfigured(desc)
            else:
                self.table_table[key] = tables[key]
        self.mysqlconn = MySQLConn(default['connection'])
        self.sqls = SQLFactory(self.table_table)


        desc_tmpl = (
            '"%s" in Mongo settings is necessary for Dao if mongo.use is true.'
            'Please make sure it is well configured.'
        )

        if 'mongo' in self._config:
            mongo = self._config['mongo']
            if not mongo.get('use', True):
                self.logger.info('MongoDB will not be used')
            else:
                if 'default' not in mongo:
                    desc = desc_tmpl%'default'
                    self.logger.error(desc)
                    raise ImproperlyConfigured(desc)
                import pymongo
                self.mongoconn = MongoDBConn(mongo['default'])


    def try_encode(self, sql):
        try:
            if type(sql)==unicode:
                return sql.encode('utf-8')
            return sql
        except Exception, e:
            return sql

    def escape_encode(self, s):
        # print str(type(s))
        try:
            st = type(s)
            if st != unicode and st != str:
                return s
            ns = MySQLdb.escape_string(s.encode('utf-8') if st==unicode else s)
            return ns
        except Exception, e:
            return s

    def check_news_in_dup(self, news):
        if not news:
            return False, 'news is null'
        sql =self.sqls['check_news_in_dup']
        dbr, r = self.mysqlconn.query(sql, news)
        if not dbr:
            desc = self._exec_error_desc_tmpl%(
                'Error when try to check news in dup database, the wc_gid is: '
                '%(wc_gid)s'
            )%news
            self.logger.error(desc)
            return False, desc
        return r[0]['exist'] >= 1, None

    def insert_news_to_dup(self, news):
        if not news:
            return False, 'news is null'
        sql = self.sqls['insert_news_to_dup'] #self.tryencode(self.sql['insertnews']%kwargs)
        dbr, r = self.mysqlconn.execute(sql, news)
        if not dbr:
            desc = self._exec_error_desc_tmpl%(
                'Error when try to insert news to dup database, the title of news is: '
                '%s'
            )%news.get('wc_title')
            self. logger.error(desc)
            return False, desc
        return r==1, None


    def insert_app(self, app):
        if not app:
            return False, 'app is null'

        sql = self.sqls['insert_app']
        dbr, r = self.mysqlconn.execute(sql, app)
        if not dbr:
            desc = self._exec_error_desc_tmpl%(
                'Error when try to insert app to config database, the name of app is: '
                '%s'
            )%app.get('wc_name')
            return False, desc
        return r==1, None


    def insert_channel(self, channel):
        if not channel:
            return False, 'channel is null'
        sql = self.sqls['insert_channel']
        dbr, r = self.mysqlconn.execute(sql, channel)
        if not dbr:
            desc = self._exec_error_desc_tmpl%(
                'Error when try to insert channel to config database, the name of channel is: '
                '%s'
            )%channel.get('wc_name')
            return False, desc
        return r==1, None

    def status_newscount_by_app(self, args=None):

        sql = self.sqls['get_news_count_by']
        if args is not None:
            if args.get('wc_app'):
                sql += '`wc_app` = %(wc_app)s AND '
            if args.get('begindate'):
                sql += '`wc_updatetime` > %(begindate)s AND '
            if args.get('enddate'):
                sql += '`wc_updatetime` < %(enddate)s AND '

        sql+=' 1'
        sql += ' GROUP BY `wc_app`'
        dbr, r = self.mysqlconn.query(sql, args)
        if not dbr:
            desc = self._exec_error_desc_tmpl%(
                'Error when try to get status of news count by app'
            )
            return None, desc
        return r, None



    def delete_dup(self, args=None):
        sql = self.sqls['delete_from_dup_by']
        if args is not None:
            if args.get('before'):
                sql += '`wc_updatetime` > %(before)s AND '
            if args.get('wc_app'):
                sql += '`wc_app` = %(wc_app)s AND '
        sql += ' 1'

        dbr, r = self.mysqlconn.execute(sql, args)
        if not dbr:
            desc = self._exec_error_desc_tmpl%(
                'Error when try to delete news from dup database'
            )
            return False, desc
        return r, None



    def get_app(self, args=None):
        sql = self.sqls['get_app_by']
        if args is not None:
            if args.get('wc_ename'):
                sql+='`wc_ename`=%(wc_ename)s AND '
        sql+=' 1'
        dbr, r = self.mysqlconn.query(sql, args)
        if not dbr:
            desc = self._exec_error_desc_tmpl%(
                'Error when try to get app from config database'
            )
            return None, desc
        return r, None

    def delete_app(self, args=None):
        sql = self.sqls['delete_app']
        dbr, r = self.mysqlconn.execute(sql, args)
        if not dbr:
            desc = self._exec_error_desc_tmpl%(
                'Error when try to delete app from config database'
            )
            return False, desc
        return r==1, None


    def delete_channel(self, args = None):
        sql = self.sqls['delete_channel_by']
        if args is not None:
            if args.get('wc_app'):
                sql += '`wc_app`=%(wc_app)s AND'
        sql += ' 1'
        dbr, r = self.mysqlconn.execute(sql, args)
        if not dbr:
            desc = self._exec_error_desc_tmpl%(
                'Error when try to delete channels from config database'
            )
            return None, desc

        return r, None

    def get_channel(self, args = None):
        sql = self.sqls['get_all_channel_by']
        if args is not None:
            if args.get('wc_app'):
                sql += '`wc_app`=%(wc_app)s AND'
            if args.get('wc_ename'):
                sql += '`wc_ename`=%(wc_ename)s AND '
            if args.get('wc_collect'):
                sql += '`wc_collect`=%(wc_collect)s AND '
            if args.get('channel_name_kw'):
                sql += '`wc_name` like %(channel_name_kw)s AND '
        sql += ' 1'
        if args is not None:
            if args.get('limit'):
                sql += ' LIMIT %(limit)s'
        dbr, r = self.mysqlconn.query(sql, args)
        if not dbr:
            desc = self._exec_error_desc_tmpl%(
                'Error when try to get channels from config database'
            )
            return None, desc
        return r, None


    def set_channel_collect(self, args = None):
        sql = self.sqls['set_channel_collect']
        if args is not None:
            if args.get('wc_id') is None:
                return False, 'wc_id is null'
            if args.get('wc_collect') is None:
                args['wc_collect'] = False
        else:
            return False, 'args is null'
        dbr, r = self.mysqlconn.execute(sql, args)
        if not dbr:
            desc = self._exec_error_desc_tmpl%(
                'Error when try to set channel collect in config database'
            )
            return False, desc
        return r==1, None

    def insert_news_to_mongo(self, news):
        dbr, r = self.mongoconn.insert(news)
        if not dbr:
            desc = self._exec_error_desc_tmpl%'Error when try to insert news to mongodb.'
            return False, desc
        return True, r

    def insert_comments_to_mongo(self, comments):
        dbr, r = self.mongoconn.insert(comments)
        if not dbr:
            desc = self._exec_error_desc_tmpl%'Error when try to insert comments to mongodb.'
            return False, desc
        return True, r



if __name__ == '__main__':
    mysqlconfig = {
        'checkdup':{
            'host':'localhost',
            'user':'wde',
            'passwd':'lixipeng@wde',
            'db':'wde_wiesler_checkdup'
        },
        'task':{
            'host':'localhost',
            'user':'wde',
            'passwd':'lixipeng@wde',
            'db':'wde_wiesler'
        }
    }
    dbutil = DBUtil(mysqlconfig)
    app = {
    }

#!/usr/bin/env python
#-*- coding:utf8 -*-
# @Author: lisnb
# @Date:   2016-04-29T17:06:11+08:00
# @Email:  lisnb.h@hotmail.com
# @Last modified by:   lisnb
# @Last modified time: 2016-07-27T18:34:13+08:00



import time
import MySQLdb
import sys
import logging
import pymongo
import urllib
from MySQLdb.cursors import DictCursor
from util.exceptions import (
    MySQLExecuteError, MySQLConnectionError,ImproperlyConfigured,
    MongoDBConnectionError,MongoDBExecuteError
)
import traceback

class DBConn(object):
    """docstring for DBConn"""
    pass


class MySQLConn(DBConn):
    def __init__(self, config, charset = 'utf8'):
        super(MySQLConn, self).__init__()
        self.logger = logging.getLogger(__name__)
        self._config = config
        self.host = config['host']
        self.user = config['user']
        self.passwd = config['passwd']
        self.db = config['db']
        self.charset = charset
        self.port = config['port']
        self._connect()

    def __del__(self):
        #关闭与数据库的连接e
        if getattr(self, 'conn', None):
            self.conn.close()

    def _connect(self):
        """
            连接数据库
        """
        desc_tmpl = 'host: %(host)s, db: %(db)s, port: %(port)s, user: %(user)s'%self._config
        attempts = 0
        while True:
            try:
                attempts += 1
                self.logger.debug('%s, %s, %s, %s, %s'%(self.host, self.user, self.passwd, self.db, self.port))
                self.conn = MySQLdb.connect(
                    host = self.host,
                    user = self.user,
                    passwd = self.passwd,
                    db = self.db,
                    port = self.port,
                    cursorclass=DictCursor)
                self.conn.autocommit(True)
                self.query('set names utf8')
                desc = 'MySQL connection established, %s'%desc_tmpl
                self.logger.debug(desc)
                break
            except Exception, e:
                desc = (
                    'Can not establish connection with mysql server '
                    'after %s attempts, %s. Original exception: %s')%(attempts, desc_tmpl, e)
                self.logger.error(desc)
            if attempts > 2:
                desc = (
                    'Can not establish connection with mysql server '
                    'after %s attempts, %s')%(attempts, desc_tmpl)
                self.logger.error(desc)
                raise MySQLConnectionError(desc)
            time.sleep(5)

    def ping(self):
        """
            判断是否需要重连接数据库
        """
        # reconnect, attempts, delay = True, 3, 5
        try:
            self.conn.ping(True)
        except Exception, e:
            desc = (
                'Can not ping connection with mysql server.'
                'Original exception: %s')%e
                # 'host: %s, db: %s, port: %s, user: %s.'
                # 'reconnect: %s, attempts: %s, delay: %s'
            # )%(self.host, self.db, self.port, self.user, reconnect, attempts, delay)
            # self.connect()
            raise MySQLConnectionError(desc)

    def execute(self, sql, args=None):
        self.ping()
        try:
            with self.conn as cursor:
                r = cursor.execute(sql, args)
            return True, r
        except Exception, e:
            desc = 'Error in execute this sql: %s, original exception: %s'%(sql, e)
            # traceback.print_exc()
            self.logger.error(desc)
            return False, None

    def executes(self, sql, args = None):
        self.ping()
        try:
            sqls = sql.split(';')
            rs = []
            for sql in sqls:
                pure_sql = sql.strip()
                if pure_sql:
                    rs.append(self.execute(sql.strip(), args))
            return True, rs
        except Exception, r:
            desc = 'Error in execute this sql: %s, original exception: %s'%(sql, e)
            self.logger.error(desc)
            return False, None

    def query(self, sql, args=None):
        """
            查询操作
            args:
                sql:要执行的语句
            return:
                成功返回(True,查询结果列表)
                失败返回(False, 空列表)
        """
        #是否需要重连接数据库
        self.ping()
        try:
            with self.conn as cursor:
                cursor.execute(sql, args)
                results = cursor.fetchall()
            return True, results
        except Exception, e:
            desc = 'Error in query this sql: %s, original exception: %s'%(sql, e)
            self.logger.error(desc)
            return False, ()

    def insert(self, sql, args=None):
        """
            插入,更新操作
            args:
                sql:要执行的语句
            return:
                成功返回True,失败返回False
        """
        #是否需要重连接数据库
        er, row = self.execute(sql, args)
        return er and row[0]



class MongoDBConn(DBConn):
    """docstring for MongoDBConn"""
    def __init__(self, config):
        super(MongoDBConn, self).__init__()
        self._config = config

    def _setup(self):
        auth = self._config.get('auth', False)
        config = self._config.copy()
        if auth:
            if not config.get('mechanism', ''):
                config['mechanism'] = 'SCRAM-SHA-1'
            uri_base = 'mongodb://%(user)s:%(passwd)s@%(host)s/%(db)s?authMechanism=%(mechanism)s'
        else:
            uri_base = 'mongodb://%(host)s/%(db)s'
        try:
            uri = uri_base%config
        except Exception as e:
            desc = (
                'MongoDB is not configured improperly.'
                'Using this config: %s'
            )%self._config
            raise ImproperlyConfigured(desc)
        try:
            self.client = pymongo.MongoClient(uri)
        except Exception as e:
            desc = (
                'Can not establish connection with MongoDB Server.'
                'Using this config: %s'
            )%self._config
            raise MongoDBConnectionError(desc)


    def _insert_one(self, coll, doc, remove_id = True):
        if remove_id and '_id' in doc:
            del doc['_id']
        r = self.client[coll].insert_one(doc)
        return r['inserted_id']

    def _insert_many(self, coll, docs, remove_id = True):
        if remove_id:
            for doc in docs:
                del doc['_id']
        rs = self.client[coll].insert_many(docs)
        return r['inserted_ids']

    def insert(self, coll, doc, remove_id = True):
        try:
            if type(doc) is list:
                r =  self._insert_many(coll, doc, remove_id)
            else:
                r =  self._insert_one(coll, doc, remove_id)
            return True, r
        except Exception as e:
            return False, None


if __name__ == '__main__':
    db = ConnDB('localhost','yangfang','fangyang','NewsDB_test')
    print db.query('select 1')

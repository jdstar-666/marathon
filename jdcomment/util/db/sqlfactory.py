#!/usr/bin/env python
#-*- coding:utf8 -*-
# @Author: lisnb
# @Date:   2016-05-13T11:44:31+08:00
# @Email:  lisnb.h@hotmail.com
# @Last modified by:   lisnb
# @Last modified time: 2016-06-22T13:23:01+08:00

from core.exceptions import ArguementInvalid

class SQLFactory(object):
    """docstring for SQLFactory"""


    _sqls_tmpl = {
        'check_news_in_dup':'SELECT EXISTS( SELECT 1 FROM `%(checkdup)s` WHERE `wc_id` = %%(wc_gid)s) as exist',
        'delete_from_dup_by': 'DELETE FROM `%(checkdup)s` WHERE ',
        'insert_news_to_dup':(
            'INSERT INTO `%(checkdup)s`(`wc_id`, `wc_app`, `wc_title`) '
            'VALUES(%%(wc_gid)s, %%(wc_app)s, %%(wc_title)s)'
        ),
        'insert_app': (
            'INSERT INTO `%(app)s`(`wc_ename`, `wc_name`, `wc_alias`, `i_sid`, `i_sn`) '
            'VALUES(%%(wc_ename)s, %%(wc_name)s, %%(wc_alias)s, %%(i_sid)s, %%(i_sn)s) '
            'ON DUPLICATE KEY UPDATE wc_updatetime=CURRENT_TIMESTAMP'
        ),
        'delete_app': 'DELETE FROM `%(app)s` WHERE `wc_ename`=%%(wc_ename)s',
        'insert_channel':(
            'INSERT INTO `%(channel)s`(`wc_iid`, `wc_name`, `wc_ename`, `wc_gid`, '
            '`wc_collect`, `wc_app`, `i_bid`, `i_bn`) '
            'VALUES (%%(wc_iid)s, %%(wc_name)s, %%(wc_ename)s, %%(wc_gid)s, '
            '%%(wc_collect)s, %%(wc_app)s, %%(i_bid)s, %%(i_bn)s) '
            'ON DUPLICATE KEY UPDATE `wc_updatetime`=CURRENT_TIMESTAMP'
        ),
        'delete_channel_by': 'DELETE FROM `%(channel)s` WHERE ',
        'get_app_by':'SELECT * FROM `%(app)s` WHERE ',
        'get_all_app':'SELECT * FROM `%(app)s`',
        'get_channel':'SELECT * FROM `%(channel)s` WHERE wc_app=%%(wc_ename)s',
        'get_all_channel_by':'SELECT * FROM `%(channel)s` WHERE ',
        'set_channels_collect_yes':'UPDATE `%(channel)s` SET wc_collect=true WHERE `wc_id` in %%s',
        'set_channels_collect_no':'UPDATE `%(channel)s` SET wc_collect=false WHERE `wc_id` in %%s',
        'set_channel_collect_yes':'UPDATE `%(channel)s` SET wc_collect=true WHERE `wc_id` = %%(wc_id)s',
        'set_channel_collect_no':'UPDATE `%(channel)s` SET wc_collect=false WHERE `wc_id` = %%(wc_id)s',
        'set_channel_collect':'UPDATE `%(channel)s` SET `wc_collect`=%%(wc_collect)s WHERE `wc_id` = %%(wc_id)s',
        'get_channel_by': 'SELECT * FROM `%(channel)s`',
        'get_news_count_by':'SELECT SQL_NO_CACHE `wc_app`, count(*) from `%(checkdup)s` WHERE ',
    }

    def __init__(self, tables):
        super(SQLFactory, self).__init__()
        self._tables = tables
        self._setup()

    def _setup(self):
        self._sqls = {}
        for k, v in SQLFactory._sqls_tmpl.items():
            self._sqls[k] = v%self._tables
    def __getattr__(self, sql_name):
        return self.__getitem__(sql_name)

    def __getitem__(self, sql_name):
        if sql_name not in self._sqls:
            desc = (
                'There is no sql named "%s".'
            )%sql_name
            raise ArguementInvalid(desc)
        return self._sqls[sql_name]



class _SQLFactory(object):
    """docstring for Sqls"""
    def __init__(self):
        super(Sqls, self).__init__()

    _sqls = {
        'check_news_in_dup':'SELECT EXISTS( SELECT 1 FROM `%(checkdup)s` WHERE wc_gid = %%s)',
        'delete_all_from_dup_by': 'DELETE FROM `%(checkdup)s` WHERE ',
        'insert_news_to_dup':(
            'INSERT INTO `%(checkdup)s`(`wc_gid`, `wc_app`, `wc_title`) '
            'VALUES(%%(wc_gid)s, %%(wc_app)s, %%(wc_title)s)'
        ),
        'insert_app': (
            'INSERT INTO `%(app)s`(`wc_ename`, `wc_name`, `wc_alias`, `i_sid`, `i_sn`) '
            'VALUES(%%(wc_ename)s, %%(wc_name)s, %%(wc_alias)s, %%(i_sid)s, %%(i_sn)s) '
            'ON DUPLICATE KEY UPDATE wc_updatetime=CURRENT_TIMESTAMP'
        ),
        'insert_channel':(
            'INSERT INTO `%(channel)s`(`wc_id`, `wc_name`, `wc_ename`, `wc_gid`, '
            '`wc_collect`, `wc_app`, `i_bid`, `i_bn`) '
            'VALUES (%%(wc_id)s, %%(wc_name)s, %%(wc_ename)s, %%(gchannelid)s, '
            '%%(wc_collect)s, %%(wc_app)s, %%(i_bid)s, %%(i_bn)s) '
            'ON DUPLICATE KEY UPDATE `wc_updatetime`=CURRENT_TIMESTAMP'
        ),
        'get_app_by':'SELECT * FROM `%(app)s` WHERE ',
        'get_all_app':'SELECT * FROM `%(app)s`',
        'get_channel':'SELECT * FROM `%(channel)s` WHERE wc_app=%%(ename)s',
        'get_all_channel_by':'SELECT * FROM `%(channel)s` WHERE ',
        'set_channels_collect_yes':'UPDATE `%(channel)s` SET wc_collect=true WHERE `wc_id` in %%s',
        'set_channels_collect_no':'UPDATE `%(channel)s` SET wc_collect=false WHERE `wc_id` in %%s',
        'set_channel_collect_yes':'UPDATE `%(channel)s` SET wc_collect=true WHERE `wc_id` = ',
        'set_channel_collect_no':'UPDATE `%(channel)s` SET wc_collect=false WHERE `wc_id` = ',
        'get_channel_by': 'SELECT * FROM `%(channel)s`',
        'get_news_count_by':'SELECT SQL_NO_CACHE `wc_app`, count(*) from `%(checkdup)s` WHERE ',
    }

    _sql_cache = {}

    @staticmethod
    def get_sql(sql_name, tables, from_cache=True):
        if sql_name not in SQLFactory._sql_cache or not from_cache:
            if sql_name not in _sqls:
                desc = (
                    'There is no sql named "%s".'
                )%sql_name
                raise ArguementInvalid(desc)
            try:
                sql = SQLFactory._sqls%tables
            except Exception as e:
                raise e
            SQLFactory._sql_cache[sql_name] = sql
        return SQLFactory._sql_cache[sql_name]

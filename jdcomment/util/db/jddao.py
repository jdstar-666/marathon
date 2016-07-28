#!/usr/bin/env python
#-*- coding:utf8 -*-
# @Author: lisnb
# @Date:   2016-07-27T16:59:19+08:00
# @Email:  lisnb.h@hotmail.com
# @Last modified by:   lisnb
# @Last modified time: 2016-07-28T13:23:27+08:00

from dbconn import MySQLConn



class JDDao(object):
    def __init__(self, config):
        super(JDDao, self).__init__()
        self.config = config
        self.conn = MySQLConn(config)
        self.page_num = 10



    def login(self, args):
        if not args:
            return None, 'Args is null.'
        sql_base = 'SELECT * FROM `user` WHERE `ps`=%(ps)s and `user_name`=%(user_name)s limit 1'
        print sql_base, args
        dbr, res = self.conn.query(sql_base, args)
        if dbr:
            if res:
                return res[0], None
            else:
                return None, None

        # if not res:
        #     print errormsg
        #     return None, 'No user is found.'
        # return res[0], None
        return None, None

    def user_get_by_id(self, args):
        if not args:
            return None, 'Args is null.'
        sql_base = 'SELECT * FROM `usertable` WHERE `user_id`=%(user_id)s limit 1'
        dbr, res = self.conn.query(sql_base, args)
        # if res is None:
        #     return None, errormsg
        # if not res:
        #     return None, 'No user is found.'
        # return res[0], None
        if dbr:
            return res, None
        return None, None



    def get_items_by_orderid(self, args):
        if not args:
            return None, 'Args is null.'

        sql_itemids = 'SELECT `item_id` FROM `orderdetail` WHERE `order_id`=%(order_id)s'
        res, itemids = self.conn.query(sql_itemids, args)
        # print itemids
        items = []
        sub_args = {
            'item_id': None
        }
        # print type(itemids)
        # print 'itemidss', itemids
        for item in itemids:
            # sub_args['item_id'] = itemid['']
            item, errormsg = self.get_item_by_id(item)
            if item:
                items.append(item)
        # print items
        return items, None

    def get_item_by_id(self, args):
        if not args:
            return None, 'Args is null.'
        sql_item = 'SELECT * FROM `item` WHERE `item_id`=%(item_id)s'
        # print sql_item, args
        dbr, res = self.conn.query(sql_item, args)
        if dbr:
            # del res[0]['item_des']
            # del res[0]['item_title']
            return res[0], None
        return None, None

    def get_orders(self, args):
        if not args:
            return None, 'Args is null.'
        sql_orders = 'SELECT * FROM `orderdetail` WHERE `user_id`=%(user_id)s'# AND `datetime`>=%(dt_from)s AND `datetime`<=%(dt_to)s'
        if 'limit' in args:
            sql_orders += ' limit %(limit)s'
        elif 'page' in args:
            args['limit_from'], args['limit_to'] = self.page_num*args[page], self.page_num*(args[page]+1)-1
            sql_orders += ' limit %(limit_from)s, %(limit_to)s '
        # print sql_orders, args
        res, orders = self.conn.query(sql_orders, args)
        # print res, orders
        for order in orders:
            order_args = {
                'order_id': order['order_id']
            }
            order['items'], _ = self.get_items_by_orderid(order_args)
            # print order
        # print orders
        return orders, None

    def get_item_comments_by_id(self, args):
        if not args:
            return None, 'Args is null.'
        sql_comments = 'SELECT * FROM `evaluation` WHERE `item_id`=%(item_id)s '#AND `datetime`>=%(dt_from)s AND `datetime`<=%(dt_to)s'
        # print sql_comments, args
        if 'limit' in args:
            sql_comments += ' limit %(limit)s'
        elif 'page' in args:
            args['limit_from'], args['limit_to'] = self.page_num*args[page], self.page_num*(args[page]+1)-1
        res, comments = self.conn.query(sql_comments, args)
        return comments, None

    def post_comment(self, args):
        if not args:
            return None, 'Args is null.'
        # sql_comment = 'INSERT INTO `evaluation`(`item_id`, `evaluation_time`, `score`, `suite`, `attitude_merchant`, `delivery`, `attitude_agent`, `comment`, `evaluation_pic`) VALUES(%(item_id)s, %(evaluation_time)s, %(score)s, %(suite)s, %(attitude_merchant)s, %(delivery)s, %(attitude_agent)s, %(comment)s, %(evaluation_pic)s)'
        sql_comment = 'INSERT INTO `evaluation`(`item_id`, `evaluation_time`, `score`, `comment`, `evaluation_pic`) VALUES(%(item_id)s, %(evaluation_time)s, %(score)s, %(comment)s, %(evaluation_pic)s)'
        print sql_comment, args
        dbr, res = self.conn.execute(sql_comment, args)
        print dbr, res
        if not res or res !=1:
            return False, None
        return True, None



mysql_config = {
    'mysql': {
        'default': {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'jd',
            'passwd': 'jd666',
            'db': 'jdcomment'
        }
    }
}

dao = JDDao(mysql_config['mysql']['default'])

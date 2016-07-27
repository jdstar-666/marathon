#!/usr/bin/env python
#-*- coding:utf8 -*-
# @Author: lisnb
# @Date:   2016-04-27T11:05:16+08:00
# @Email:  lisnb.h@hotmail.com
# @Last modified by:   lisnb
# @Last modified time: 2016-06-18T22:20:18+08:00

class UnknownError(Exception):
    pass

class ImproperlyConfigured(Exception):
    """Wiesler is somehow improperly configured"""
    pass


class ImportFailed(ImportError):
    """Import module failed"""
    pass

class ImportAppConfigFailed(ImportFailed):
    """Can't import config of app when initialize an App instance"""
    pass

class AttributeNotFound(Exception):
    """Necessary attribute is not found"""
    pass

class NecessaryVariableIsEmpty(Exception):
    """A variable that is necessary is empty, None or empty list etc."""
    pass

class ArguementInvalid(Exception):
    """Attribute is somehow invalid"""
    pass

class DBError(Exception):
    pass

class MySQLError(DBError):
    """Something happens when using mysql"""
    pass

class MySQLConnectionError(MySQLError):
    """Can't establish connection with mysql server"""
    pass

class MySQLExecuteError(MySQLError):
    """Error when try to execute SQL statement"""
    pass

class MongoDBError(DBError):
    pass

class MongoDBConnectionError(MongoDBError):
    pass

class MongoDBExecuteError(MongoDBError):
    pass

class AppNotFound(ImportFailed):
    pass

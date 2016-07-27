/*
Navicat MySQL Data Transfer

Source Server         : localDB
Source Server Version : 50524
Source Host           : localhost:3306
Source Database       : liu666

Target Server Type    : MYSQL
Target Server Version : 50524
File Encoding         : 65001

Date: 2016-07-27 14:36:16
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for itemtable
-- ----------------------------
DROP TABLE IF EXISTS `itemtable`;
CREATE TABLE `itemtable` (
  `item_id` varchar(255) NOT NULL COMMENT '商品id',
  `item_title` varchar(255) DEFAULT NULL COMMENT '商品名称',
  `item_pic` varchar(255) DEFAULT NULL COMMENT '商品图片信息',
  `item_des` varchar(255) DEFAULT NULL COMMENT '商品描述',
  `item_price` double DEFAULT NULL COMMENT '商品描述',
  `ps` varchar(255) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='商品表';

-- ----------------------------
-- Table structure for orderanduser
-- ----------------------------
DROP TABLE IF EXISTS `orderanduser`;
CREATE TABLE `orderanduser` (
  `user_id` varchar(255) DEFAULT NULL COMMENT '用户id',
  `order_id` varchar(255) DEFAULT NULL COMMENT '订单id',
  KEY `user_key` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单商品关联表';

-- ----------------------------
-- Table structure for orderdetail
-- ----------------------------
DROP TABLE IF EXISTS `orderdetail`;
CREATE TABLE `orderdetail` (
  `order_id` varchar(255) DEFAULT NULL COMMENT '订单id',
  `user_id` varchar(255) DEFAULT NULL COMMENT '用户id',
  `item_id` varchar(255) DEFAULT NULL COMMENT '商品id',
  `order_time` datetime DEFAULT NULL COMMENT '订单产生时间',
  `comment` varchar(255) DEFAULT NULL COMMENT '商品评论',
  `ps` varchar(255) DEFAULT NULL COMMENT '备注'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单详情表';

-- ----------------------------
-- Table structure for usertable
-- ----------------------------
DROP TABLE IF EXISTS `usertable`;
CREATE TABLE `usertable` (
  `user_id` varchar(255) NOT NULL COMMENT '用户id',
  `user_name` varchar(255) DEFAULT NULL COMMENT '用户名称',
  `user_level` varchar(255) DEFAULT NULL COMMENT '用户等级',
  `ps` varchar(255) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户信息表';

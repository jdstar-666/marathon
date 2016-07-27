/**
* @Author: lisnb
* @Date:   2016-07-27T17:42:30+08:00
* @Email:  lisnb.h@hotmail.com
* @Last modified by:   lisnb
* @Last modified time: 2016-07-27T22:04:07+08:00
*/



/*
Navicat MySQL Data Transfer

Source Server         : localDB
Source Server Version : 50524
Source Host           : localhost:3306
Source Database       : liu666

Target Server Type    : MYSQL
Target Server Version : 50524
File Encoding         : 65001

Date: 2016-07-27 17:26:02
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for evaluation
-- ----------------------------
DROP TABLE IF EXISTS `evaluation`;
CREATE TABLE `evaluation` (
  `evaluation_id` varchar(255) NOT NULL COMMENT '评价id',
  `item_id` varchar(255) DEFAULT NULL COMMENT '商品id',--外键item表
  `evaluation_time` datetime DEFAULT NULL COMMENT '评价时间',
  `score` double DEFAULT NULL COMMENT '商品满意评分',
  `suite` varchar(255) DEFAULT NULL COMMENT '商品符合度',
  `attitude_merchant` varchar(255) DEFAULT NULL COMMENT '商家服务态度',
  `delivery` varchar(255) DEFAULT NULL COMMENT '物流评分',
  `attitude_agent` varchar(255) DEFAULT NULL COMMENT '配送员评分',
  `comment` varchar(255) DEFAULT NULL COMMENT '商品评价',
  `evaluation_pic` varchar(255) DEFAULT NULL COMMENT '评价图片路径',
  `evaluation_addition_flag` varchar(255) DEFAULT NULL COMMENT '追评',
  `valid_flag` int(11) DEFAULT NULL COMMENT '有效标志',
  PRIMARY KEY (`evaluation_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='评价表';

-- ----------------------------
-- Table structure for item
-- ----------------------------
DROP TABLE IF EXISTS `item`;
CREATE TABLE `item` (
  `item_id` varchar(255) NOT NULL COMMENT '商品id',
  `item_title` varchar(255) DEFAULT NULL COMMENT '商品名称',
  `item_pic` varchar(255) DEFAULT NULL COMMENT '商品图片信息',
  `item_des` varchar(255) DEFAULT NULL COMMENT '商品描述',
  `item_price` double DEFAULT NULL COMMENT '商品描述',
  `score` varchar(255) DEFAULT NULL COMMENT '商品综合评分',
  `suite` varchar(255) DEFAULT NULL COMMENT '商品符合度',
  `attitude_merchant` varchar(255) DEFAULT NULL COMMENT '商家服务态度',
  `transport` varchar(255) DEFAULT NULL COMMENT '物流评分',
  `attitude_agent` varchar(255) DEFAULT NULL COMMENT '配送员评分',
  `item_value_flag` int(11) DEFAULT NULL COMMENT '商品是否已经评价标志',
  `ps` varchar(255) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='商品表';

-- ----------------------------
-- Table structure for orderdetail
-- ----------------------------
DROP TABLE IF EXISTS `orderdetail`;
CREATE TABLE `orderdetail` (
  `order_id` varchar(255) DEFAULT NULL COMMENT '订单id',
  `user_id` varchar(255) DEFAULT NULL COMMENT '用户id',--外键user表
  `item_id` varchar(255) DEFAULT NULL COMMENT '商品id',--外键item表
  `evaluation_id` varchar(255) DEFAULT NULL COMMENT '评价id',--外键评价表
  `order_time` datetime DEFAULT NULL COMMENT '订单产生时间',
  `ps` varchar(255) DEFAULT NULL COMMENT '备注',
  `submit` int(11) DEFAULT NULL COMMENT '订单是否完成'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单详情表';

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `user_id` varchar(255) NOT NULL COMMENT '用户id',
  `user_name` varchar(255) DEFAULT NULL COMMENT '用户名称',
  `user_level` varchar(255) DEFAULT NULL COMMENT '用户等级',
  `user_type` varchar(255) DEFAULT NULL COMMENT '用户类型(用户信用等级，即权重)',
  `ps` varchar(255) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户信息表';

/**
* @Author: lisnb
* @Date:   2016-07-28T03:07:58+08:00
* @Email:  lisnb.h@hotmail.com
* @Last modified by:   lisnb
* @Last modified time: 2016-07-28T03:33:30+08:00
*/



use jdcomment;
/*
Navicat MySQL Data Transfer

Source Server         : localDB
Source Server Version : 50524
Source Host           : localhost:3306
Source Database       : liu666

Target Server Type    : MYSQL
Target Server Version : 50524
File Encoding         : 65001

Date: 2016-07-28 01:09:12
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for evaluation
-- ----------------------------
DROP TABLE IF EXISTS `evaluation`;
CREATE TABLE `evaluation` (
  `evaluation_id` varchar(255) NOT NULL COMMENT '评价id',
  `item_id` varchar(255) DEFAULT NULL COMMENT '商品id',
  `evaluation_time` varchar(255) DEFAULT NULL COMMENT '评价时间',
  `score` double DEFAULT NULL COMMENT '商品满意评分',
  `suite` varchar(255) DEFAULT NULL COMMENT '商品符合度',
  `comment` varchar(255) DEFAULT NULL COMMENT '商品评价',
  `evaluation_pic` varchar(255) DEFAULT NULL COMMENT '评价图片路径',
  `evaluation_addition_flag` varchar(255) DEFAULT NULL COMMENT '追评',
  `valid_flag` int(11) DEFAULT NULL COMMENT '有效标志',
  PRIMARY KEY (`evaluation_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='评价表';

-- ----------------------------
-- Records of evaluation
-- ----------------------------
INSERT INTO `evaluation` VALUES ('120001', '2754831', '2016-01-03 16:00', '4.6', '4.9', '手机刚拿到手 系统流畅 做工精致 很不错的国货手机', '1276524.png', '0', '1');
INSERT INTO `evaluation` VALUES ('120002', '1903226', '2016-01-03 16:00', '4.6', '4.7', '手机刚拿到手 系统流畅 做工精致 很不错的国货手机', '1276524.png', '0', '1');
INSERT INTO `evaluation` VALUES ('120003', '1276524', '2016-01-03 16:00', '4.7', '4.8', '手机刚拿到手 系统流畅 做工精致 很不错的国货手机', '1276524.png', '0', '1');
INSERT INTO `evaluation` VALUES ('120004', '3294814', '2016-01-03 16:00', '4.7', '4.8', '手机刚拿到手 系统流畅 做工精致 很不错的国货手机', '1276524.png', '0', '1');
INSERT INTO `evaluation` VALUES ('120005', '1903226', '2016-01-03 16:00', '4.7', '4.8', '手机刚拿到手 系统流畅 做工精致 很不错的国货手机', '1276524.png', '0', '1');
INSERT INTO `evaluation` VALUES ('120006', '2712431', '2016-01-03 16:00', '4.7', '4.8', '手机刚拿到手 系统流畅 做工精致 很不错的国货手机', '1276524.png', '0', '1');
INSERT INTO `evaluation` VALUES ('120007', '1276524', '2016-01-03 16:00', '4.7', '4.8', '手机刚拿到手 系统流畅 做工精致 很不错的国货手机', '1276524.png', '0', '1');
INSERT INTO `evaluation` VALUES ('120008', '1276524', '2016-01-03 16:00', '4.7', '4.8', '手机刚拿到手 系统流畅 做工精致 很不错的国货手机', '1276524.png', '0', '1');

-- ----------------------------
-- Table structure for item
-- ----------------------------
DROP TABLE IF EXISTS `item`;
CREATE TABLE `item` (
  `item_id` varchar(255) NOT NULL COMMENT '商品id',
  `item_title` varchar(255) DEFAULT NULL COMMENT '商品名称',
  `item_pic` text COMMENT '商品图片信息',
  `item_des` text COMMENT '商品描述',
  `item_price` double DEFAULT NULL COMMENT '商品描述',
  `score` varchar(5) DEFAULT NULL COMMENT '商品综合评分',
  `suite` varchar(5) DEFAULT NULL COMMENT '商品符合度',
  `attitude_merchant` varchar(5) DEFAULT NULL COMMENT '商家服务态度',
  `delivery` varchar(5) DEFAULT NULL COMMENT '物流评分',
  `attitude_agent` varchar(5) DEFAULT NULL COMMENT '配送员评分',
  `ps` varchar(255) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='商品表';

-- ----------------------------
-- Records of item
-- ----------------------------
INSERT INTO `item` VALUES ('1276524', '索尼（SONY）MDR-1A 高解析度 立体声耳机 银色', '1276524.png', '主体\n品牌	索尼 SONY\n型号	MDR-1A\n类型	耳麦\n佩戴方式	头戴式\n颜色	银色\n耳机规格\n频响范围	3 Hz - 100000 Hz\n阻抗	1 kHz 时24 Ω\n接口类型	L型\n灵敏度	105 dB/mW\n最大承载功率	1500 mW\n线长	1.2m\n重量	约225 g（不包括连接线）\n线型	双边等长线\n音频接口	3.5毫米音频接口\n耳机/耳麦是否带线控	是\n驱动单元类型/直径	40 mm，圆顶型（CCAW 音圈）\n耳麦规格\n频响范围	20 Hz – 20000 Hz\n特性\n特性	封闭式，动态\n', '1199', '4.7', '4.6', '4.7', '4.8', '4.9', null);
INSERT INTO `item` VALUES ('1903226', '索尼（SONY）NW-A25HN mp3无损音乐播放器 炭黑色 高清降噪 含入耳式耳机', '1903226.png', '主体\n品牌	索尼（SONY）\n型号	NW-A25HN\n颜色	炭黑色\n类型	MP4播放器\n翻新类型	全新\n存储\n存储类型	闪存式\n外接扩展卡	支持\n屏幕\n屏幕尺寸	2.2英寸\n类型	TFT彩屏\n菜单语言	简体中文、英文\n视频\n视频播放	支持\n视频格式	AVC(H.264/AVC) / MPEG-4 / Windows Media Video 9\n音频\n音效模式	DSEE HX / 醇音技术+ / 5种音效&清晰重低音 / 动态均衡器\n音频播放格式	MP3 / WMA / FLAC / Linear PCM / AAC / HE-AAC / Apple Lossless / AIFF\n功能\n录音	不支持\nFM功能	具备（耳机线作为天线使用）\nA-B复读	不支持\n外放功能	不支持\nOTG功能	不支持\n支持定时关机	不支持\nUSB充电	支持\n耳机接口	3.5mm\n接口\nUSB2.0	支持\n蓝牙	通讯系统：蓝牙规范3.0\nWIFI	不支持\n电池\n电池类型	锂电池\n理论音频回放时间	约49小时（高解析度音频）；约50小时（MP3音频格式，关闭蓝牙功能）\n理论视频回放时间	MPEG-4 384kbps： 关闭降噪功能：约 14 小时 开启降噪功能：约 13 小时\n规格\n尺寸	约 43.6 x 109 x 8.7　mm（不含突出部分） 约 44.4mm x 109.1mm x 9.1mm\n其它特性\n特性	与A15/A17系列中使用的无铅焊锡技术相比，可带来更好的音质。并降低噪声等级，以提高整个频段的声音解析度。S-Master HX可执行音频信号的全数字处理，从而支持高解析度音频的回放。', '1499', '4.8', '4.7', '4.9', '4.9', '4.8', null);
INSERT INTO `item` VALUES ('2712431', '乐视（Le）乐Max2（X820) 金色 移动联通电信4G 双卡双待', '2712431.png', '主体\n品牌\n乐视（Letv）\n型号\nX820\n颜色\n金色\n上市年份\n2016年\n上市月份\n4月\n输入方式\n触控\n智能机\n是\n操作系统\n安卓（Android）\n操作系统版本\nAndroid\nCPU品牌\nQualcomm 骁龙\nCPU型号\n高通骁龙820(MSM8996)\nCPU频率\n2.15GHz\nCPU核数\n四核\n运营商标志或内容\n无\n网络\n4G网络制式\n移动4G/联通4G/电信4G\n3G网络制式\n移动3G(TD-SCDMA)/联通3G(WCDMA)/电信3G(CDMA2000)\n2G网络制式\n移动2G/联通2G(GSM)/电信2G(CDMA)\n网络频率\nTDD-LTE ：B38/B39/B40/B41；FDD-LTE： B1/B2/B3/B4/B5/B7/B8/B12/B17/B20/B25/B26；TD-SCDMA ：B34/B39 ；WCDMA：B1/B2/B5/B8 ；GSM：B2/B3/B5/B8；CDMA：BC0/BC1\n双卡机类型\n双卡双待单通\n其它\n2张电信卡无法同时使用 双卡使用说明：任意一张SIM卡可选4G网络，另外一张为GSM网络\n存储\n机身内存\n32GB ROM\n运行内存\n4GB RAM\n储存卡类型\n不支持\n显示\n屏幕尺寸\n5.7英寸\n触摸屏\n电容屏，多点触控\n分辨率\n2560×1440（2K）\n屏幕材质\nTFT\n超大字体\n支持\n屏幕色彩\n1600万色\n感应器\nGPS模块\n支持\n重力感应\n支持\n光线感应\n支持\n距离感应\n支持\n电子罗盘\n支持\n陀螺仪\n支持\n摄像功能\n后置摄像头\n2100万像素\n前置摄像头\n800万像素\n闪光灯\n支持\n自动对焦\n支持\n娱乐功能\n收音机\n不支持\n音乐播放\n支持\n视频播放\n支持\n录音\n支持\n传输功能\nWi-Fi\n支持\nWIFI热点\n支持\n蓝牙\n支持\nNFC(近场通讯)\n不支持\nOTG\n支持\n其他\nSIM卡尺寸\nNano SIM卡 + Nano SIM卡\n电池类型\n其它\n电池容量（mAh）\n3100mAh\n电池更换\n不支持\n数据线\n专用接口\n耳机接口\n专用接口\n机身尺寸（mm）\n156.8*77.6*7.99\n机身重量（g）\n185g\n包装清单\n主机×1，电源适配器×1，耳机转接头×1，数据线×1，手机保护套，卡针×1，三包证×1，快速入门指南×1', '2099', '4.7', '4.5', '4.6', '4.9', '4.8', null);
INSERT INTO `item` VALUES ('2754831', '华为（HUAWEI）华为手环B3 (蓝牙耳机与智能手环结合+金属机身+触控屏幕+TPU腕带) 运动版 悦动白', '1276524.png', '主体\n品牌	华为\n型号	华为手环 B3\n颜色	悦动白\n操作系统	兼容Android 4.3+ 及 IOS 7.0+\n系统内存	128KB RAM\n适用范围	130-200mm手腕尺寸\n防水	IP57防尘防水\n翻新类型	全新\n显示屏\n屏幕尺寸	0.7\n屏幕分辨率	128*80\n屏幕材质	3D弧面处理大猩猩玻璃\n触摸屏	OLED触控显示屏\n通讯功能\n拨打电话	支持\n免持接听	支持\n来电提醒	支持\n娱乐功能\n拍照	可控制手机遥控拍照\n防丢失	支持\n计步器	支持\n其他功能	与手机同步显示来电信息\n连接方式\n蓝牙	BT4.2\n耳机接口	蓝牙\n其他参数\n电池容量	91mAh\n待机时长	6小时通话时间，3-4天工作时间，6天长待机\n产品尺寸	210.0mm×21.7mm×12.2mm\n产品重量	产品：< 95.8g 耳机：约10.8g', '999', '4.6', '4.7', '4.8', '4.8', '4.8', null);
INSERT INTO `item` VALUES ('2873176', '膜法世家 水光黑面膜贴尊享礼盒20片（水润光泽 保湿嫩肤）', '2873176.png', '主体\n类别	面贴膜\n品牌	膜法世家\n保质期	1095\n功效\n保湿补水	是\n亮肤	是\n适合肤质\n偏油及油性	是\n偏干及干性	是\n混合型	是', '99', '4.8', '4.8', '4.5', '4.9', '4.9', null);
INSERT INTO `item` VALUES ('3294814', '小蚁（YI）4K运动相机（黑色）智能摄像机 户外航拍潜水防抖相机 遥控相机', '1276524.png', '基本参数\n品牌	小蚁\n屏幕参数\n液晶屏尺寸	2.19吋高清触屏\n液晶屏比例	16：9黄金比例\n镜头参数\n滤镜直径	其它\n存储及连接参数\n存储介质	其他\n附件及电源参数\n电池	1400mAh,3.85V,5.39Wh\n电池续航时间	4K/30帧2小时续航\n外观参数\n尺寸	102(L)*102(W)*49mm(H) （含包装）\n重量	178.5g （含包装）', '1499', '4.8', '4.8', '4.9', '4.8', '4.9', null);

-- ----------------------------
-- Table structure for orderdetail
-- ----------------------------
DROP TABLE IF EXISTS `orderdetail`;
CREATE TABLE `orderdetail` (
  `order_id` varchar(55) DEFAULT NULL COMMENT '订单id',
  `user_id` varchar(55) DEFAULT NULL COMMENT '用户id',
  `item_id` varchar(55) DEFAULT NULL COMMENT '商品id',
  `evaluation_id` varchar(55) DEFAULT NULL COMMENT '评价id',
  `order_time` varchar(55) DEFAULT NULL COMMENT '订单产生时间',
  `submit` varchar(5) DEFAULT NULL COMMENT '订单是否完成',
  `attitude_merchant` varchar(5) DEFAULT NULL COMMENT '商家服务态度',
  `delivery` varchar(5) DEFAULT NULL COMMENT '物流评分',
  `attitude_agent` varchar(5) DEFAULT NULL COMMENT '配送员评分',
  `ps` varchar(255) DEFAULT NULL COMMENT '备注'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单详情表';

-- ----------------------------
-- Records of orderdetail
-- ----------------------------
INSERT INTO `orderdetail` VALUES ('200001', '1000001', '1276524', '120003', '2016-01-01 16:00', '1', '4', '4', '5', '4');
INSERT INTO `orderdetail` VALUES ('200002', '1000001', '1903226', '120002', '2016-01-03 16:00', '1', '4', '5', '4', null);
INSERT INTO `orderdetail` VALUES ('200003', '1000002', '3294814', '120004', '2016-01-03 16:00', '1', '4', '5', '5', null);
INSERT INTO `orderdetail` VALUES ('200004', '1000003', '1903226', '120005', '2016-01-03 16:00', '1', '5', '5', '5', null);
INSERT INTO `orderdetail` VALUES ('200002', '1000001', '2754831', '120001', '2016-01-03 16:00', '1', '5', '5', '4', null);
INSERT INTO `orderdetail` VALUES ('200002', '1000004', '2712431', '120006', '2016-01-03 16:00', '1', '5', '4', '5', null);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `user_id` varchar(255) NOT NULL COMMENT '用户id',
  `user_name` varchar(255) DEFAULT NULL COMMENT '用户名称',
  `user_level` varchar(255) DEFAULT NULL COMMENT '用户等级',
  `user_type` varchar(255) DEFAULT NULL COMMENT '用户类型(用户信用等级，即权重)',
  `ps` varchar(255) DEFAULT NULL COMMENT '用户密码',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户信息表';

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1000001', '张龙', '钻石会员', '1', null);
INSERT INTO `user` VALUES ('1000002', '赵虎', '银牌会员', '1', null);
INSERT INTO `user` VALUES ('1000003', '山珍', '金牌会员', '1', null);
INSERT INTO `user` VALUES ('1000004', '海威', '银牌会员', '1', null);
INSERT INTO `user` VALUES ('1000005', '春困', '钻石会员', '1', null);
INSERT INTO `user` VALUES ('1000006', '秋乏', '金牌会员', '1', null);

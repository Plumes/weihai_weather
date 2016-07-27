/*
Navicat MySQL Data Transfer

Source Server         : db
Source Server Version : 50631
Source Host           : 192.168.33.10:3306
Source Database       : weather

Target Server Type    : MYSQL
Target Server Version : 50631
File Encoding         : 65001

Date: 2016-07-27 16:32:23
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `weihai`
-- ----------------------------
DROP TABLE IF EXISTS `weihai`;
CREATE TABLE `weihai` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` int(11) unsigned zerofill NOT NULL COMMENT '数据时间',
  `sunrise` varchar(16) DEFAULT NULL COMMENT '日出时间',
  `sunset` varchar(16) DEFAULT NULL COMMENT '日落时间',
  `temperature` decimal(10,3) DEFAULT NULL COMMENT '气温',
  `dewpoint` decimal(10,3) DEFAULT NULL,
  `humidity` decimal(10,3) DEFAULT NULL,
  `wind_chill` decimal(10,3) DEFAULT NULL,
  `wind_speed` decimal(10,3) DEFAULT NULL,
  `wind_direction` varchar(8) DEFAULT NULL,
  `thw_index` decimal(10,3) DEFAULT NULL,
  `barometer` decimal(10,3) DEFAULT NULL,
  `heat_index` decimal(10,3) DEFAULT NULL,
  `daily_rainfall` decimal(10,3) DEFAULT NULL,
  `monthly_rainfall` decimal(10,3) DEFAULT NULL,
  `current_rainfall` decimal(10,3) DEFAULT NULL,
  `sunshine` decimal(10,3) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `time_unique` (`created`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of weihai
-- ----------------------------

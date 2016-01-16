/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50621
Source Host           : localhost:3306
Source Database       : api_validator

Target Server Type    : MYSQL
Target Server Version : 50621
File Encoding         : 65001

Date: 2015-05-07 16:34:06
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for api_detail
-- ----------------------------
DROP TABLE IF EXISTS `api_detail`;
CREATE TABLE `api_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_code` varchar(255) DEFAULT NULL COMMENT '所属工程',
  `module_code` varchar(255) DEFAULT NULL COMMENT '所属模块',
  `class_code` varchar(255) DEFAULT NULL COMMENT '所在类',
  `method_name` varchar(255) DEFAULT NULL COMMENT '接口名',
  `rest_method_name` varchar(255) DEFAULT NULL COMMENT 'rest接口',
  `visit_method_way` varchar(255) DEFAULT NULL COMMENT '访问方式',
  `paras_detail` varchar(255) DEFAULT NULL COMMENT '参数及说明',
  `invoke_example` text COMMENT '调用示例',
  `return_segments` varchar(255) DEFAULT NULL COMMENT '返回字段',
  `return_description` varchar(255) DEFAULT NULL COMMENT '返回说明',
  `work_status` varchar(20) DEFAULT NULL COMMENT '是否启用 0不启用，1启用',
  `return_format` varchar(255) DEFAULT NULL COMMENT '返回格式 	Xml,json',
  `return_example` text COMMENT '返回示例',
  `test_status` varchar(20) DEFAULT NULL COMMENT '是否测试 0不测，1测试',
  `owner` varchar(255) DEFAULT NULL COMMENT 'API负责人',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of api_detail
-- ----------------------------
INSERT INTO `api_detail` VALUES ('1', 'cop-api', 'zhtx', 'AccountController', '登录接口111', '/account/sms/sendCode', 'GET', '{\'mobile\':\'手机号码\'}', 'http://218…/login\r\nPost:\r\nXxx=xxx\r\nhttp://218…/login\r\nPost:\r\nXxx=xxx\r\nhttp://218…/login\r\nPost:\r\nXxx=xxx', '{}', '200', '0', 'XML', 'None', '0', 'Jackie');
INSERT INTO `api_detail` VALUES ('7', 'cop-api', 'zhtx', 'AccountController', 'test11', 'test', 'POST', 'test', 'test', 'test', '', '0', 'XML', 'test', '0', 'test');
INSERT INTO `api_detail` VALUES ('9', 'cop-api', 'zhtx', 'AccountController', 'test22', 'test', 'GET', 'test', 'test', 'test', '', '0', 'XML', 'test', '1', 'test');
INSERT INTO `api_detail` VALUES ('10', 'cop-api', 'zhtx', 'AccountController', 'test222', 'test', 'GET', 'test', 'test', 'test', '', '0', 'XML', 'test', '1', 'test');
INSERT INTO `api_detail` VALUES ('11', 'cop-api', 'zhtx', 'AccountController', 'test22', 'test', 'GET', 'test', 'test', 'test', '', '0', 'XML', 'test', '1', 'test');
INSERT INTO `api_detail` VALUES ('13', 'cop-api', 'zhtx', 'AccountController', 'test', 'test', 'GET', 'test', 'test', 'test', '', '0', 'XML', 'test', '1', 'test');
INSERT INTO `api_detail` VALUES ('14', 'cop-api', 'zhtx', 'AccountController', 'test', 'test', 'GET', 'test', 'test', 'test', '', '0', 'XML', 'test', '1', 'test');
INSERT INTO `api_detail` VALUES ('16', 'cop-api', 'zhtx', 'AccountController', 'test', 'test', 'GET', 'test', 'test', 'test', '', '0', 'XML', 'test', '1', 'test');
INSERT INTO `api_detail` VALUES ('17', 'cop-api', 'zhtx', 'AccountController', 'test1111', 'test', 'GET', 'test1111', 'test111', 'test11111', '', '0', 'JSON', 'test', '0', 'test');
INSERT INTO `api_detail` VALUES ('19', 'cop-api', 'zhtx', 'AccountController', 'test', 'test', 'GET', 'test', 'test', 'test', '', '0', 'XML', 'test', '1', 'test');
INSERT INTO `api_detail` VALUES ('21', 'cop-api', 'zhtx', 'AccountController', 'test', 'test', 'GET', 'test', 'test', 'test', '', '0', 'XML', 'test', '1', 'test');
INSERT INTO `api_detail` VALUES ('22', 'cop-api', 'zhtx', 'AccountController', 'test', '/api/rest/pad/blocks', 'GET', 'test', 'test', 'test', '', '0', 'XML', 'test', '1', 'test');

-- ----------------------------
-- Table structure for check_table
-- ----------------------------
DROP TABLE IF EXISTS `check_table`;
CREATE TABLE `check_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `api_id` int(11) NOT NULL COMMENT 'apiId',
  `enviroment_code` varchar(255) NOT NULL COMMENT '环境id',
  `parameters` varchar(255) DEFAULT NULL COMMENT '测试参数',
  `visit_way` varchar(255) DEFAULT NULL COMMENT '访问方式 post/get 枚举',
  `encrypt_status` varchar(255) DEFAULT NULL COMMENT '是否加密 00 否 01是',
  `encrypt_way` varchar(255) DEFAULT NULL COMMENT '加密方式 Des2,des,sha1,rsa 枚举',
  `encrypt_key` varchar(255) DEFAULT NULL COMMENT '加密的key',
  `match_strategy` varchar(255) DEFAULT NULL COMMENT '匹配策略',
  `match_content` varchar(255) DEFAULT NULL COMMENT '匹配内容',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of check_table
-- ----------------------------
INSERT INTO `check_table` VALUES ('1', '22', 'productive', '{\'username\':\'janwenjohn\'}', 'GET', '00', null, null, 'JSON', '{\'success\':True}');

-- ----------------------------
-- Table structure for class_detail
-- ----------------------------
DROP TABLE IF EXISTS `class_detail`;
CREATE TABLE `class_detail` (
  `name` varchar(255) NOT NULL COMMENT '类名',
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of class_detail
-- ----------------------------
INSERT INTO `class_detail` VALUES ('AccountController');
INSERT INTO `class_detail` VALUES ('AccountController11');
INSERT INTO `class_detail` VALUES ('AccountController111');

-- ----------------------------
-- Table structure for enviroment_detail
-- ----------------------------
DROP TABLE IF EXISTS `enviroment_detail`;
CREATE TABLE `enviroment_detail` (
  `name` varchar(255) DEFAULT NULL COMMENT '环境名',
  `code` varchar(255) NOT NULL COMMENT '环境代码',
  `address` varchar(40) DEFAULT NULL COMMENT '地址',
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of enviroment_detail
-- ----------------------------
INSERT INTO `enviroment_detail` VALUES ('444', '444', '444');
INSERT INTO `enviroment_detail` VALUES ('生产环境22', 'productive', '218.78.214.24');
INSERT INTO `enviroment_detail` VALUES ('测试环境', 'test', '218.78.214.32');
INSERT INTO `enviroment_detail` VALUES ('测试环境', 'test1', '218.78.214.32');
INSERT INTO `enviroment_detail` VALUES ('test11', 'test11', 'test');

-- ----------------------------
-- Table structure for module_detail
-- ----------------------------
DROP TABLE IF EXISTS `module_detail`;
CREATE TABLE `module_detail` (
  `code` varchar(255) NOT NULL COMMENT '模块代码',
  `name` varchar(255) DEFAULT NULL COMMENT '模块名',
  `project_code` varchar(255) DEFAULT NULL COMMENT '所属工程',
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of module_detail
-- ----------------------------
INSERT INTO `module_detail` VALUES ('zhtx', '账号体系11', 'cop-api');

-- ----------------------------
-- Table structure for project_detail
-- ----------------------------
DROP TABLE IF EXISTS `project_detail`;
CREATE TABLE `project_detail` (
  `name` varchar(255) DEFAULT NULL COMMENT '工程名',
  `code` varchar(255) NOT NULL DEFAULT '' COMMENT '工程代码',
  `context` varchar(255) DEFAULT NULL,
  `pro_env_code` varchar(255) DEFAULT NULL COMMENT '生产环境代码',
  `test_env_code` varchar(255) DEFAULT NULL COMMENT '测试环境代码',
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of project_detail
-- ----------------------------
INSERT INTO `project_detail` VALUES ('create', 'cop-api', 'context', '生产环境', '生产环境');
INSERT INTO `project_detail` VALUES ('create', 'cop-apid', 'ddd', '生产环境', '生产环境');

#-*-coding:utf-8-*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql.base import TEXT

Base = declarative_base()
  
# `name` varchar(255) DEFAULT NULL COMMENT '������',
#  `code` varchar(255) NOT NULL COMMENT '���̴���',
#  `context` varchar(255) DEFAULT NULL,
#  `pro_env_code` varchar(255) DEFAULT NULL COMMENT '�������',
#  `test_env_code` varchar(255) DEFAULT NULL COMMENT '���Ի�������',

class ProjectDetail(Base):    
    __tablename__ = 'project_detail'
    code = Column(String(255), primary_key=True)
    name = Column(String(255))
    context = Column(String(255))
    pro_env_code = Column(String(255))
    test_env_code = Column(String(255))
    
#  `name` varchar(255) DEFAULT NULL COMMENT '������',
#  `code` varchar(255) NOT NULL COMMENT '��������',
#  `address` varchar(40) DEFAULT NULL COMMENT '��ַ',    
    
class EnvironmentDetail(Base):    
    __tablename__ = 'enviroment_detail'
    code = Column(String(255), primary_key=True)
    name = Column(String(255))
    address = Column(String(255))
    
    
    
#CREATE TABLE `module_detail` (
#  `code` varchar(255) NOT NULL COMMENT 'ģ�����',
#  `name` varchar(255) DEFAULT NULL COMMENT 'ģ����',
#  `project_code` varchar(255) DEFAULT NULL COMMENT '��������',
#  PRIMARY KEY (`code`)
#) ENGINE=InnoDB DEFAULT CHARSET=utf8;    
    
class ModuleDetail(Base):    
    __tablename__ = 'module_detail'
    code = Column(String(255), primary_key=True)
    name = Column(String(255))
    project_code = Column(String(255))
    
     
#CREATE TABLE `class_detail` (
#  `name` varchar(255) NOT NULL COMMENT '����',
#  PRIMARY KEY (`name`)
#) ENGINE=InnoDB DEFAULT CHARSET=utf8;    
    
class ClassDetail(Base):    
    __tablename__ = 'class_detail'
    name = Column(String(255), primary_key=True)


#CREATE TABLE `api_detail` (
#  `id` int(11) NOT NULL,
#  `project_code` varchar(255) DEFAULT NULL COMMENT '��������',
#  `module_code` varchar(255) DEFAULT NULL COMMENT '����ģ��',
#  `class_code` varchar(255) DEFAULT NULL COMMENT '������',
#  `method_name` varchar(255) DEFAULT NULL COMMENT '�ӿ���',
#  `rest_method_name` varchar(255) DEFAULT NULL COMMENT 'rest�ӿ�',
#  `visit_method_way` varchar(255) DEFAULT NULL COMMENT '���ʷ�ʽ',
#  `paras_detail` varchar(255) DEFAULT NULL COMMENT '����˵��',
#  `invoke_example` text COMMENT '����ʾ��',
#  `return_segments` varchar(255) DEFAULT NULL,
#  `return_description` varchar(255) DEFAULT NULL COMMENT '����˵��',
#  `work_status` int(1) DEFAULT NULL COMMENT '�Ƿ����� 0�����ã�1����',
#  `return_format` varchar(255) DEFAULT NULL COMMENT '���ظ�ʽ     Xml,json',
#  `test_status` varchar(255) DEFAULT NULL COMMENT '�Ƿ���� 0���⣬1����',
#  `onwer` varchar(255) DEFAULT NULL COMMENT 'API������',
#  PRIMARY KEY (`id`)
#) ENGINE=InnoDB DEFAULT CHARSET=utf8;    
    
class APIDetail(Base):    
    __tablename__ = 'api_detail'
    id = Column(Integer, primary_key=True)
    project_code = Column(String(255))
    module_code = Column(String(255))
    class_code = Column(String(255))
    method_name = Column(String(255))
    rest_method_name = Column(String(255))
    visit_method_way = Column(String(255)) 
    paras_detail = Column(String(255))
    invoke_example = Column(TEXT)
    return_segments = Column(String(255))
    return_description = Column(String(255))
    work_status = Column(Integer)
    return_format = Column(String(255))
    return_example = Column(TEXT) 
    test_status = Column(Integer)
    owner = Column(String(255))
   
# check_table
#   `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
#   `api_id` int(11) NOT NULL COMMENT 'apiId',
#   `enviroment_id` int(11) NOT NULL COMMENT '环境id',
#   `parameters` varchar(255) DEFAULT NULL COMMENT '测试参数',
#   `visit_way` varchar(255) DEFAULT NULL COMMENT '访问方式 post/get 枚举',
#   `encrypt_status` varchar(255) DEFAULT NULL COMMENT '是否加密 00 否 01是',
#   `encrypt_way` varchar(255) DEFAULT NULL COMMENT '加密方式 Des2,des,sha1,rsa 枚举',
#   `encrypt_key` varchar(255) DEFAULT NULL COMMENT '加密的key',
#   `match_strategy` varchar(255) DEFAULT NULL COMMENT '匹配策略',
#   `match_content` varchar(255) DEFAULT NULL COMMENT '匹配内容',


class CheckTableBo(Base):    
    __tablename__ = 'check_table'
    id = Column(Integer, primary_key=True)
    api_id = Column(Integer)
    enviroment_code = Column(String(255))
    parameters = Column(String(255))
    visit_way = Column(String(255))
    encrypt_status = Column(String(255))
    encrypt_way = Column(String(255)) 
    encrypt_key = Column(String(255))
    match_strategy = Column(TEXT)
    match_content = Column(String(255))
   





    
    
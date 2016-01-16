
#-*-coding:utf-8-*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from bo.baseBo import ProjectDetail
from bo.baseBo import APIDetail
from bo.baseBo import EnvironmentDetail
from bo.baseBo import ModuleDetail
from bo.baseBo import ClassDetail
from bo.baseBo import CheckTableBo

    
Base = declarative_base()    

engine = create_engine('mysql://root:admin@localhost:3306/api_validator?charset=utf8', encoding='utf-8', echo=True)
Base.metadata.create_all(engine)
    
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()  

class APIDetailDao():
    #保存api
    def save(self, dic):
        api_detail = APIDetail(project_code = dic["projectName"], module_code = dic["moduleName"], class_code = dic["className"],
                               method_name = dic["methodName"], rest_method_name = dic["restMethodName"], visit_method_way = dic["requestWay"],
                               paras_detail = dic["paraDescription"], invoke_example = dic["invokeExample"], return_segments = dic["returnSegment"],
                               return_description = dic["returnDescription"], work_status = dic["workStatus"], return_format = dic["retrunFormat"],
                               return_example = dic["returnExample"], test_status = dic["testStatus"], owner = dic["responser"]);
        session.add(api_detail)
        try:                #--------session提交时， 要捕获异常，否则错误将一直存在知道session清除----------
            session.commit()
        except:
            session.rollback()
        
    #跟新api
    def update(self, id, dic):
        api_detail = APIDetail(id = id, project_code = dic["projectName"], module_code = dic["moduleName"], class_code = dic["className"],
                               method_name = dic["methodName"], rest_method_name = dic["restMethodName"], visit_method_way = dic["requestWay"],
                               paras_detail = dic["paraDescription"], invoke_example = dic["invokeExample"], return_segments = dic["returnSegment"],
                               return_description = dic["returnDescription"], work_status = dic["workStatus"], return_format = dic["retrunFormat"],
                               return_example = dic["returnExample"], test_status = dic["testStatus"], owner = dic["responser"]);
        session.merge(api_detail)
        session.commit()        
        #查询符合条件的api
    def query(self, conditionDic):
        query = session.query(APIDetail)
        if 'projectName' in conditionDic:
            query = query.filter(APIDetail.project_code == conditionDic['projectName'])
        if 'moduleName' in conditionDic:
            query = query.filter(APIDetail.module_code == conditionDic['moduleName'])
        if 'className' in conditionDic:
            query = query.filter(APIDetail.class_code == conditionDic['className']) 
        if 'methodName' in conditionDic:
            if conditionDic['methodName'] != "":
                query = query.filter(APIDetail.method_name.like('%' + conditionDic['methodName'] + '%')) 
        if 'restMethodName' in conditionDic:
            if conditionDic['restMethodName'] != "":
                query = query.filter(APIDetail.rest_method_name.like('%' + conditionDic['restMethodName'] + '%')) 
        if 'requestWay' in conditionDic:
            if conditionDic['requestWay'] != "":
                query = query.filter(APIDetail.visit_method_way == conditionDic['requestWay'])                         
        if 'retrunFormat' in conditionDic:
            if conditionDic['retrunFormat'] != "":
                query = query.filter(APIDetail.return_format == conditionDic['retrunFormat']) 
        return query.all()

    def queryPage(self, conditionDic, page): # 分页查询
        query = session.query(APIDetail)
        if 'projectName' in conditionDic:
            query = query.filter(APIDetail.project_code == conditionDic['projectName'])
        if 'moduleName' in conditionDic:
            query = query.filter(APIDetail.module_code == conditionDic['moduleName'])
        if 'className' in conditionDic:
            query = query.filter(APIDetail.class_code == conditionDic['className']) 
        if 'methodName' in conditionDic:
            if conditionDic['methodName'] != "":
                query = query.filter(APIDetail.method_name.like('%' + conditionDic['methodName'] + '%')) 
        if 'restMethodName' in conditionDic:
            if conditionDic['restMethodName'] != "":
                query = query.filter(APIDetail.rest_method_name.like('%' + conditionDic['restMethodName'] + '%')) 
        if 'requestWay' in conditionDic:
            if conditionDic['requestWay'] != "":
                query = query.filter(APIDetail.visit_method_way == conditionDic['requestWay'])                         
        if 'retrunFormat' in conditionDic:
            if conditionDic['retrunFormat'] != "":
                query = query.filter(APIDetail.return_format == conditionDic['retrunFormat']) 
        return query.order_by(APIDetail.id)[page.size * (page.number - 1), page.size * page.number - 1]  
          
    def deleteById(self, id):
        apiToDelete = session.query(APIDetail).get(id)
        session.delete(apiToDelete)
        session.commit()
        
    def getById(self, id):
        return session.query(APIDetail).get(id)

class ProjectDetailDao():
    def findList(self):
        return session.query(ProjectDetail).all()
    def getById(self, code):
        return session.query(ProjectDetail).get(code)
    
    #保存project
    def save(self, dic):
        projectDetail = ProjectDetail(name = dic["projectName"], context = dic["projectContext"],
                                      pro_env_code = dic["projectProEnvi"], test_env_code = dic["projectTestEnvi"],
                                      code = dic["projectCode"]);
        session.add(projectDetail)
        session.commit()
        
    #跟新project
    def update(self, id, dic):
        projectDetail = ProjectDetail(code = id, name = dic["projectName"], context = dic["projectContext"],
                                      pro_env_code = dic["projectProEnvi"], test_env_code = dic["projectTestEnvi"]);
        session.merge(projectDetail)
        session.commit() 
        
    def deleteById(self, code):
        projectToDelete = session.query(ProjectDetail).get(code)
        session.delete(projectToDelete)
        session.commit()           
               
class EnvironmentDetailDao():
    def findList(self):
        return session.query(EnvironmentDetail).all()
    
    def getById(self, code):
        return session.query(EnvironmentDetail).get(code)
    
    def save(self, dic):
        environmentDetail = EnvironmentDetail(name = dic["name"], code = dic["code"],
                                      address = dic["address"]);
        session.add(environmentDetail)
        try:  
            session.commit()
        except:
            session.rollback()
        
    def update(self, id, dic):
        environmentDetail = EnvironmentDetail(name = dic["name"], code = dic["code"],
                                      address = dic["address"]);
        session.merge(environmentDetail)
        session.commit() 
        
    def deleteById(self, code):
        environmentToDelete = session.query(EnvironmentDetail).get(code)
        session.delete(environmentToDelete)
        session.commit() 
        
            

class ModuleDetailDao():
    def findList(self):
        return session.query(ModuleDetail).all()
    
    def getById(self, code):
        return session.query(ModuleDetail).get(code)
    
    def save(self, dic):
        moduleDetail = ModuleDetail(name = dic["name"], code = dic["code"],
                                      project_code = dic["projectCode"]);
        session.add(moduleDetail)
        session.commit()
        
    def update(self, dic):
        moduleDetail = ModuleDetail(name = dic["name"], code = dic["code"],
                                      project_code = dic["projectCode"]);
        session.merge(moduleDetail)
        session.commit() 
        
    def deleteById(self, code):
        moduleDetailToDelete = session.query(ModuleDetail).get(code)
        session.delete(moduleDetailToDelete)
        session.commit()     
    
    
    
# class    
class ClassDetailDao():
    def findList(self):
        return session.query(ClassDetail, ClassDetail.name).all()          

    def deleteById(self, name):
        classToDelete = session.query(ClassDetail).get(name)
        session.delete(classToDelete)
        session.commit()   
    #保存Class
    def save(self, dic):
        classToAdd = session.query(ClassDetail).get(dic["name"])
        if classToAdd:
            session.merge(classToAdd)
            session.commit()
            return False 
        classDetail = ClassDetail(name=dic["name"])
        session.add(classDetail)
        session.commit()
        
    #跟新Class
    def update(self, id, dic):
        classDetail = ClassDetail(name=id)
        session.merge(classDetail)
        session.commit()

    
    # 测试表dao
class CheckTableDao():
    def findList(self):
        return session.query(CheckTableBo).all()
    
    def getById(self, id):
        return session.query(CheckTableBo).get(id)
    
    def save(self, dic):
        checkTableBo = CheckTableBo(name = dic["name"], code = dic["code"],# to modify
                                      address = dic["address"]);
        session.add(checkTableBo)
        session.commit()
        
    def update(self, id, dic):
        checkTableBo = CheckTableBo(name = dic["name"], code = dic["code"],
                                      address = dic["address"]);
        session.merge(checkTableBo)
        session.commit() 
        
    def deleteById(self, id):
        checkTableBoToDelete = session.query(CheckTableBo).get(id)
        session.delete(checkTableBoToDelete)
        session.commit()
    

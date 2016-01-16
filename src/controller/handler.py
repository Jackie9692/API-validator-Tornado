# coding:utf-8

from database.dao import ProjectDetailDao
from database.dao import ModuleDetailDao
from database.dao import EnvironmentDetailDao
from database.dao import ClassDetailDao
from database.dao import APIDetailDao 
from database.dao import CheckTableDao
import tornado.web

from util.utilClass import PageUtil

import urllib
import urllib2
import json


# API 注册界面
class  RegisterHandler(tornado.web.RequestHandler):
    def __init__(self, application, request):
        tornado.web.RequestHandler.__init__(self, application, request)
        self.projectDetailDao = ProjectDetailDao()
        self.moduleDetailDao = ModuleDetailDao ()
        self.environmentDetailDao = EnvironmentDetailDao()
        self.classDetailDao = ClassDetailDao()
    
    def get(self):
        projectCodeList = self.projectDetailDao.findList()
        moduleCodeList = self.moduleDetailDao.findList()
        classDetailCodeList = self.classDetailDao.findList()
        self.render("register.html", projectCodeList=projectCodeList, moduleCodeList=moduleCodeList, classDetailCodeList=classDetailCodeList)

# API 注册界面保存处理
class  RegisterSaveHandler(tornado.web.RequestHandler):
    def post(self):
        self.apiDetailDao = APIDetailDao()
        projectName = self.get_argument("projectName")
        moduleName = self.get_argument("moduleName")
        className = self.get_argument("className")
        methodName = self.get_argument("methodName")
        restMethodName = self.get_argument("restMethodName")
        requestWay = self.get_argument("requestWay")
        requestWay = requestWay.upper()
        paraDescription = self.get_argument("paraDescription")
        invokeExample = self.get_argument("invokeExample")
        returnSegment = self.get_argument("returnSegment")
        returnDescription = self.get_argument("returnDescription")
        workStatus = self.get_argument("workStatus")
        retrunFormat = self.get_argument("retrunFormat")
        retrunFormat = retrunFormat.upper()
        returnExample = self.get_argument("returnExample")
        testStatus = self.get_argument("testStatus")
        responser = self.get_argument("responser")
        apiDetailDic = {"projectName":str(projectName), "moduleName":str(moduleName), "className":str(className),
               "methodName":str(methodName), "restMethodName":str(restMethodName), "requestWay":str(requestWay),
               "paraDescription":str(paraDescription), "invokeExample":str(invokeExample), "returnSegment":str(returnSegment),
               "returnDescription":str(returnDescription), "workStatus":str(workStatus), "retrunFormat":str(retrunFormat),
               "returnExample":str(returnExample), "testStatus":str(testStatus), "responser":str(responser)}
        self.apiDetailDao.save(apiDetailDic)
        self.write("register success!")
        


# API查询handler
class APIQuery(tornado.web.RequestHandler):
    apiDetailDao = APIDetailDao();
    projectDetailDao = ProjectDetailDao()
    moduleDetailDao = ModuleDetailDao ()
    environmentDetailDao = EnvironmentDetailDao()
    classDetailDao = ClassDetailDao()
    def get(self):
        projectCodeList = self.projectDetailDao.findList()
        moduleCodeList = self.moduleDetailDao.findList()
        classDetailCodeList = self.classDetailDao.findList()
        apiMatchedList = self.apiDetailDao.query({});
        self.render("apiQuery.html", projectCodeList=projectCodeList, moduleCodeList=moduleCodeList, classDetailCodeList=classDetailCodeList, apiMatchedList=apiMatchedList)
    def post(self):
        projectName = self.get_argument("projectName")
        moduleName = self.get_argument("moduleName")
        className = self.get_argument("className")
        methodName = self.get_argument("methodName")
        restMethodName = self.get_argument("restMethodName")
        requestWay = self.get_argument("requestWay")
        if (requestWay == "GET") or (requestWay == "POST"):
            print "请求方式正常"
        else:
            requestWay = ""
        retrunFormat = self.get_argument("retrunFormat")
        if (retrunFormat == "XML") or (retrunFormat == "JSON"):
            print "返回格式正常"
        else:
            retrunFormat = ""       
        apiDetailDic = {"projectName":projectName, "moduleName":moduleName, "className":className,
               "methodName":methodName, "restMethodName":restMethodName, "requestWay":requestWay, "retrunFormat":retrunFormat} 
        apiMatchedList = self.apiDetailDao.query(apiDetailDic);
        projectCodeList = self.projectDetailDao.findList()
        moduleCodeList = self.moduleDetailDao.findList()
        classDetailCodeList = self.classDetailDao.findList()
        self.render("apiQuery.html", projectCodeList=projectCodeList, moduleCodeList=moduleCodeList, classDetailCodeList=classDetailCodeList, apiMatchedList=apiMatchedList)

# API详情handler
class APIDetail(tornado.web.RequestHandler):
    apiDetailDao = APIDetailDao();
    def get(self):
        id = self.get_argument("id")        
        apiDetail = self.apiDetailDao.getById(id)
        self.render("apiDetail.html", apiDetail=apiDetail)
    def post(self):
        self.write("Register success!")

# API编辑内容
class APIEdit(tornado.web.RequestHandler):
    apiDetailDao = APIDetailDao();
    def get(self):
        id = self.get_argument("id")        
        apiDetail = self.apiDetailDao.getById(id)
        self.render("apiEdit.html", apiDetail=apiDetail)
    def post(self):
        id = self.get_argument("id")
        projectName = self.get_argument("projectName")
        moduleName = self.get_argument("moduleName")
        className = self.get_argument("className")
        methodName = self.get_argument("methodName")
        restMethodName = self.get_argument("restMethodName")
        requestWay = self.get_argument("requestWay")
        requestWay = requestWay.upper()
        paraDescription = self.get_argument("paraDescription")
        invokeExample = self.get_argument("invokeExample")
        returnSegment = self.get_argument("returnSegment")
        returnDescription = self.get_argument("returnDescription")
        workStatus = self.get_argument("workStatus")
        retrunFormat = self.get_argument("retrunFormat")
        retrunFormat = retrunFormat.upper()
        returnExample = self.get_argument("returnExample")
        testStatus = self.get_argument("testStatus")
        responser = self.get_argument("responser")
        apiDetailDic = {"projectName":projectName, "moduleName":moduleName, "className":className,
               "methodName":methodName, "restMethodName":restMethodName, "requestWay":requestWay,
               "paraDescription":paraDescription, "invokeExample":invokeExample, "returnSegment":returnSegment,
               "returnDescription":returnDescription, "workStatus":workStatus, "retrunFormat":retrunFormat,
               "returnExample":returnExample, "testStatus":testStatus, "responser":responser}
        self.apiDetailDao.update(id, apiDetailDic)
        self.redirect("/api/query")


# API删除
class APIRemove(tornado.web.RequestHandler):
    apiDetailDao = APIDetailDao()
    def get(self):
        id = self.get_argument("id")
        self.apiDetailDao.deleteById(id)
        self.redirect("/api/query")
    def post(self):
        self.write("Register success!")



# ################## 类表处理

class ClassQueryHandler(tornado.web.RequestHandler):
    classDetailDao = ClassDetailDao()
    def get(self):
        classList = self.classDetailDao.findList()
        self.render("classQuery.html", classList=classList)
    def post(self):
        self.write("")
        
class ClassDeleteHandler(tornado.web.RequestHandler):
    classDetailDao = ClassDetailDao()
    def get(self):
        id = self.get_argument("id")
        self.classDetailDao.deleteById(name=id)
        self.redirect("/class/query")
    def post(self):
        self.write("!")

class ClassCreateHandler(tornado.web.RequestHandler):
    classDetailDao = ClassDetailDao()
    def get(self):
        return 
    def post(self):
        id = self.get_argument("id")
        if id:
            classDic = {"name":id}
            self.classDetailDao.save(classDic)
            self.redirect("/class/query")
        else:
            self.write("创建失败！")

class ClassEditHandler(tornado.web.RequestHandler):
    classDetailDao = ClassDetailDao()
    def get(self):
        id = self.get_argument("id")
        self.apiDetailDao.deleteById(id)
        self.redirect("/api/query")
    def post(self):
        self.write("")
        
class ClassEditSaveHandler(tornado.web.RequestHandler):
    classDetailDao = ClassDetailDao()
    def get(self):
        id = self.get_argument("id")
        self.classDetailDao.update(id, {})
        self.redirect("/class/query")
    def post(self):
        self.write("!")
        
               
# Project         
class ProjectQueryHandler(tornado.web.RequestHandler):
    projectDetailDao = ProjectDetailDao()
    def get(self):
        projectList = self.projectDetailDao.findList()
        self.render("projectQuery.html", projectList=projectList)
    def post(self):
        self.write("")
        
class ProjectDeleteHandler(tornado.web.RequestHandler):
    projectDetailDao = ProjectDetailDao()
    def get(self):
        id = self.get_argument("id")
        self.projectDetailDao.deleteById(code=id)
        self.redirect("/project/query")
    def post(self):
        self.write("!")

class ProjectCreateHandler(tornado.web.RequestHandler):
    projectDetailDao = ProjectDetailDao()
    environmentDetailDao = EnvironmentDetailDao()
    def get(self):
        environmentList = self.environmentDetailDao.findList();
        self.render("projectCreate.html", environmentList=environmentList)
    def post(self):
        projectName = self.get_argument("projectName")
        projectCode = self.get_argument("projectCode")
        projectContext = self.get_argument("projectContext")
        projectProEnvi = self.get_argument("projectProEnvi")
        projectTestEnvi = self.get_argument("projectTestEnvi")
        self.projectDetailDao.save(dic={"projectName":projectName, "projectCode":projectCode,
                                          "projectContext":projectContext, "projectProEnvi":projectProEnvi,
                                          "projectTestEnvi":projectTestEnvi})
        self.redirect("/project/query")


class ProjectEditHandler(tornado.web.RequestHandler):
    projectDetailDao = ProjectDetailDao()
    environmentDetailDao = EnvironmentDetailDao()
    def get(self):
        id = self.get_argument("id")
        projectDetail = self.projectDetailDao.getById(code=id)
        environmentList = self.environmentDetailDao.findList();
        self.render("projectEdit.html", projectDetail=projectDetail, environmentList=environmentList)
    def post(self):
        self.write("")
        
class ProjectEditSaveHandler(tornado.web.RequestHandler):
    projectDetailDao = ProjectDetailDao()
    def get(self):
        self.redirect("/project/query")
    def post(self):
        projectName = self.get_argument("projectName")
        projectCode = self.get_argument("projectCode")
        projectContext = self.get_argument("projectContext")
        projectProEnvi = self.get_argument("projectProEnvi")
        projectTestEnvi = self.get_argument("projectTestEnvi")
        self.projectDetailDao.update(id=projectCode, dic={"projectName":projectName, "projectCode":projectCode,
                                          "projectContext":projectContext, "projectProEnvi":projectProEnvi,
                                          "projectTestEnvi":projectTestEnvi})       
        self.redirect("/project/query")
class ProjectDetailHandler(tornado.web.RequestHandler):
    projectDetailDao = ProjectDetailDao()
    def get(self):
        id = self.get_argument("id")        
        projectDetail = self.projectDetailDao.getById(code=id)
        self.render("projectDetail.html", projectDetail=projectDetail)
    def post(self):
        self.write("Register success!")    
        
        
# environment       
class EnvirQueryHandler(tornado.web.RequestHandler):
    environmentDetailDao = EnvironmentDetailDao()
    def get(self):
        environmentList = self.environmentDetailDao.findList()
        self.render("environmentQuery.html", environmentList=environmentList)
    def post(self):
        self.write("")
        
class EnvirDeleteHandler(tornado.web.RequestHandler):
    environmentDetailDao = EnvironmentDetailDao()
    def get(self):
        id = self.get_argument("id")
        self.environmentDetailDao.deleteById(code=id)
        self.redirect("/environment/query")
    def post(self):
        self.write("!")

class EnvirCreateHandler(tornado.web.RequestHandler):
    environmentDetailDao = EnvironmentDetailDao()
    def get(self):
        environmentList = self.environmentDetailDao.findList();
        self.render("projectCreate.html", environmentList=environmentList)
    def post(self):
        name = self.get_argument("name")
        code = self.get_argument("code")
        address = self.get_argument("address")
        self.environmentDetailDao.save(dic={"name":name, "code":code, "address":address})
        self.redirect("/environment/query")


class EnvirEditHandler(tornado.web.RequestHandler):
    environmentDetailDao = EnvironmentDetailDao()
    def get(self):
        id = self.get_argument("id")
        environmentDetail = self.environmentDetailDao.getById(code=id)
        self.render("environmentEdit.html", environmentDetail=environmentDetail)
    def post(self):
        self.write("")
        
class EnvirEditSaveHandler(tornado.web.RequestHandler):
    environmentDetailDao = EnvironmentDetailDao()
    def get(self):
        self.redirect("/environment/query")
    def post(self):
        name = self.get_argument("name")
        code = self.get_argument("code")
        address = self.get_argument("address")
        self.environmentDetailDao.update(id=id, dic={"name":name, "code":code, "address":address})
        self.redirect("/environment/query")      
      
      
      
# module    
class ModuleQueryHandler(tornado.web.RequestHandler):
    moduleDetailDao = ModuleDetailDao()
    def get(self):
        moduleList = self.moduleDetailDao.findList()
        self.render("moduleQuery.html", moduleList=moduleList)
    def post(self):
        self.write("")
        
class ModuleDeleteHandler(tornado.web.RequestHandler):
    moduleDetailDao = ModuleDetailDao()
    def get(self):
        id = self.get_argument("id")
        self.moduleDetailDao.deleteById(code=id)
        self.redirect("/module/query")
    def post(self):
        self.write("!")

class ModuleCreateHandler(tornado.web.RequestHandler):
    moduleDetailDao = ModuleDetailDao()
    projectDetailDao = ProjectDetailDao()
    def get(self):
        projectList = self.projectDetailDao.findList();
        self.render("moduleCreate.html", projectList=projectList)
    def post(self):
        code = self.get_argument("code")
        name = self.get_argument("name")
        projectCode = self.get_argument("projectCode")
        self.moduleDetailDao.save(dic={"code":code, "name":name, "projectCode":projectCode})
        self.redirect("/module/query")


class ModuleEditHandler(tornado.web.RequestHandler):
    moduleDetailDao = ModuleDetailDao()
    projectDetailDao = ProjectDetailDao()
    def get(self):
        id = self.get_argument("id")
        moduleDetail = self.moduleDetailDao.getById(code=id)
        projectList = self.projectDetailDao.findList();
        self.render("moduleEdit.html", moduleDetail=moduleDetail, projectList=projectList)
    def post(self):
        self.write("")
        
class ModuleEditSaveHandler(tornado.web.RequestHandler):
    moduleDetailDao = ModuleDetailDao()
    def get(self):
        self.redirect("/module/query")
    def post(self):
        code = self.get_argument("code")
        name = self.get_argument("name")
        projectCode = self.get_argument("projectCode")
        self.moduleDetailDao.update(dic={"code":code, "name":name, "projectCode":projectCode})
        self.redirect("/module/query")       


class CheckTableHandler(tornado.web.RequestHandler):
    checkTableDao = CheckTableDao()
    environmentDetailDao = EnvironmentDetailDao()
    apiDetailDao = APIDetailDao();
    def get(self):
        checkTableList = self.checkTableDao.findList()
        for checkTableEach in checkTableList:
            self.checkOneAPI(each=checkTableEach)
            pass
        
#         self.redirect("/module/query")
    def post(self):
#         code = self.get_argument("code")
#         name = self.get_argument("name")
#         projectCode = self.get_argument("projectCode")
#         self.moduleDetailDao.update(dic = {"code":code, "name":name, "projectCode":projectCode})
        self.redirect("/module/query")
        
    def checkOneAPI(self, each):   
        apiId = each.api_id
        enviromentId = each.enviroment_code
        apiDetail = self.apiDetailDao.getById(apiId)
        environmentDetail = self.environmentDetailDao.getById(enviromentId)
        
        
        statusJudge = True;  # 判断是否匹配标志
        preUrl = 'http://' + environmentDetail.address + ':8080' + apiDetail.rest_method_name  # 访问地址前缀
        
        res = self.getResResult(each=each, preUrl=preUrl)
        statusJudge = self.checkResResult(res=res, each=each)
        
        if statusJudge :
           print 'get url = ' + preUrl + '   正常访问'.decode('UTF-8')
        else:
           print 'get url = ' + preUrl + '   访问有误'.decode('UTF-8')        


     # 得到返回结果
    def getResResult(self, each, preUrl):
        res = {}
        if each.visit_way == 'GET':  # get请求  
            parametersDic = dict(eval(each.parameters))
            if each.encrypt_status == '00':  # 不加密
                if parametersDic:
                    url = preUrl + '?'
                    for key in parametersDic:
                        oneParameter = key + '=' + parametersDic[key]
                        url += oneParameter
#                     print 'url = ' + url
                    req = urllib2.Request(url)
                    res_data = urllib2.urlopen(req)
                    res = res_data.read()
        elif each.visit_way == 'POST':  # POST请求      
            values = {'username': 'Jackie'}
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            res = response.read()
        else:
            print '请求方式有误'.encode()
        return res
          
     #   验证返回结果
    def checkResResult(self, res, each):
        resJudge = True
        if each.match_strategy == 'JSON':
            jsonTarget = json.loads(res, encoding='UTF-8')
            matchContentDic = dict(eval(each.match_content))
            for key in matchContentDic:
                if key not in jsonTarget or matchContentDic[key] != jsonTarget[key]:
                    resJudge = False
                    break        
        return resJudge
        
        
        
        
        
        
           
        

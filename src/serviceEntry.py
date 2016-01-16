#coding:utf-8

import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from controller import handler

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

handlers = [
    (r"/api/register", handler.RegisterHandler),    #apihandler注册
    (r"/api/registerSave", handler.RegisterSaveHandler),
    (r"/api/query", handler.APIQuery),
    (r"/api/detail", handler.APIDetail),
    (r"/api/edit", handler.APIEdit),
    (r"/api/remove", handler.APIRemove),
    
    (r"/class/query", handler.ClassQueryHandler), #class handler
    (r"/class/delete", handler.ClassDeleteHandler),
    (r"/class/create", handler.ClassCreateHandler),
    (r"/class/edit", handler.ClassEditHandler),
    (r"/class/editSave", handler.ClassEditSaveHandler),
    
    (r"/project/query", handler.ProjectQueryHandler), #类模块handler
    (r"/project/delete", handler.ProjectDeleteHandler),
    (r"/project/create", handler.ProjectCreateHandler),
    (r"/project/edit", handler.ProjectEditHandler),
    (r"/project/editSave", handler.ProjectEditSaveHandler),
    (r"/project/detail", handler.ProjectDetailHandler),
   
    (r"/environment/query", handler.EnvirQueryHandler), #环境
    (r"/environment/delete", handler.EnvirDeleteHandler),
    (r"/environment/create", handler.EnvirCreateHandler),
    (r"/environment/edit", handler.EnvirEditHandler),
    (r"/environment/editSave", handler.EnvirEditSaveHandler),   
    
    (r"/module/query", handler.ModuleQueryHandler), #module 
    (r"/module/delete", handler.ModuleDeleteHandler),
    (r"/module/create", handler.ModuleCreateHandler),
    (r"/module/edit", handler.ModuleEditHandler),
    (r"/module/editSave", handler.ModuleEditSaveHandler), 
    
    
    (r"/test/checkTable", handler.CheckTableHandler)
]


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers= handlers,
        template_path=os.path.join(os.path.dirname(__file__), "template"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
#         debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
    
    
    
    
    
    
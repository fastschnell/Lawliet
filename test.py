# -*- coding: utf-8 -*-
from lawliet import Routes, app, Route

Route.debug = True
Routes(
    ('/ping', 'ping.views.ping'),
    ('/字典', 'ping.views.res_json'),
    ('/json', 'ping.views.res_json'),
    ('/xml/', 'ping.views.test_response'),
    ('/ok', 'test.ok'),
    ('/auto_method', 'ping.auto_method.auto_method', ['AUTO'])
)

if __name__ == '__main__':
    app.run()


def ok():
    return 'okokok'
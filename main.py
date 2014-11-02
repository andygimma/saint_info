#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
from handlers import MainHandler, PublicMapHandler, PrivateMapHandler, LoginHandler, LogoutHandler, CSVHandler, DataVisualizationHandler

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'LK@#J$LK@#J$@#IUR(E*R)WE(FIUAFOJOWE%IUQ#)(%*TU$OIJQTJRWKGUWRE(T*W)$#(*%W$#%OIJRWOIEUWR"0t9*',
}
app = webapp2.WSGIApplication([
    ('/', MainHandler.MainHandler),
    ('/map', PublicMapHandler.PublicMapHandler),
    ('/csv', CSVHandler.CSVHandler),
    ('/dataviz', DataVisualizationHandler.DataVisualizationHandler),
    ('/login', LoginHandler.LoginHandler),
    ('/logout', LogoutHandler.LogoutHandler)
], config=config, debug=True)

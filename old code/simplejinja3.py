import cherrypy
import os

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

class Root(object):
    @cherrypy.expose
    def index(self):
        templ = env.get_template('index.html')
        return templ.render()

    @cherrypy.expose
    def profile(self, user):
        templ = env.get_template('profile.html')
        return templ.render(username=user)

cherrypy.config.update({'server.socket_host': '0.0.0.0'})

if __name__ == '__main__':
    cherrypy.quickstart(Root(),config={
        '/assets':
        {
            'tools.staticdir.on':True,
            'tools.staticdir.dir': os.path.abspath("./templates/assets")
        }
    })
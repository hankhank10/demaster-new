import cherrypy
import demaster
import string
import json
import sys
import time
import os
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

class go(object):
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render(salutation='Hello', target='World'
        )
    @cherrypy.expose
    def demaster(self, long_track_name, format="simple"):

        # get the data
        short_track_name = demaster.strip_name(long_track_name)

        # log it simply
        f = open ("demaster-log-simple.txt", "a")
        f.write (short_track_name + " >>> " + long_track_name + "\n")
        f.close

        # log it csv
        remoteip = cherrypy.request.remote.ip
        print (remoteip)
        f = open ("demaster-log-csv.csv", "a")
        f.write (time.strftime('%X %x') + "," + long_track_name + "," + short_track_name + "," + remoteip + "\n")
        f.close

        if format == "html":
            return ("Long track name: " + long_track_name + "<br>" + "Short track name: " + short_track_name)

        if format == "simple":
            return (str(short_track_name))

        if format == "json":
            # put it into json
            json_output = {
                "long_track_name": long_track_name,
                "short_track_name": short_track_name
                }
            return json.dumps(json_output)

    @cherrypy.expose
    def generate(self, length=8):
        return "Generate page"

cherrypy.config.update({'server.socket_host': '0.0.0.0'})

if __name__ == '__main__':
    cherrypy.quickstart(go(),config={
        '/assets':
        {
            'tools.staticdir.on':True,
            'tools.staticdir.dir': os.path.abspath("./templates/assets")
        }
    })
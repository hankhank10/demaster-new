import cherrypy
import string
import json
import sys
import time
import os
from jinja2 import Environment, FileSystemLoader

import easy_slack
import demaster
import random_text_prompt
import counter

env = Environment(loader=FileSystemLoader('templates'))
descriptive_text_for_results = ""

class go(object):
    @cherrypy.expose
    def index(self):
        #easy_slack.send_message ("Home page load: " + cherrypy.request.remote.ip)
        tmpl = env.get_template('index.html')
        return tmpl.render(random_prompt = random_text_prompt.random_text_prompt())
    
    @cherrypy.expose
    def demaster(self, long_track_name, format="simple"):

        # get the data
        short_track_name = demaster.strip_name(long_track_name)

        # add one to the counter
        counter.add_one()

        # log it simply to file
        f = open ("demaster-log-simple.txt", "a")
        f.write (short_track_name + " >>> " + long_track_name + "\n")
        f.close

        # log it to csv
        remoteip = cherrypy.request.remote.ip
        print (remoteip)
        f = open ("demaster-log-csv.csv", "a")
        f.write (time.strftime('%X %x') + "," + long_track_name + "," + short_track_name + "," + remoteip + "\n")
        f.close

        # log it to slack
        easy_slack.send_message (format + ": " + long_track_name + " >>> " + short_track_name)

        if format == "html":
            tmpl = env.get_template('result.html')
            if long_track_name == short_track_name:
                descriptive_text_for_results = "I can't do any better than"
                long_track_name = ""
            else:
                descriptive_text_for_results = "should really be called"
            return tmpl.render(long_name = long_track_name, short_name = short_track_name, descriptive_text_for_results = descriptive_text_for_results)

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
    def feedback(self, feedback, long_track_name, short_track_name):
        
        # log it csv
        remoteip = cherrypy.request.remote.ip
        print (remoteip)
        f = open ("demaster-feedback.csv", "a")
        f.write (time.strftime('%X %x') + "," + long_track_name + "," + short_track_name + "," + feedback + ","+ remoteip + "\n")
        f.close
        
        if feedback == "thumbs-up":
            feedback_text = "Great! <br> Thanks for letting us know!"
        else:
            feedback_text = "Ah, sorry about that. <br> We'll work on it."
        
        tmpl = env.get_template('feedback.html')
        return tmpl.render(feedback_text = feedback_text)

    @cherrypy.expose
    def api_instructions(self):
        tmpl = env.get_template('api_instructions.html')
        return tmpl.render()
        

cherrypy.config.update({'server.socket_host': '0.0.0.0','server.socket_port': 8080})

if __name__ == '__main__':
    cherrypy.quickstart(go(),config={
        '/assets':
        {
            'tools.staticdir.on':True,
            'tools.staticdir.dir': os.path.abspath("./templates/assets")
        },

        '/favicon.ico':
        {
            'tools.staticfile.on': True,
            'tools.staticfile.filename': os.path.abspath("./favicon/favicon.ico")
        }

    })

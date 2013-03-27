#This webservice requires the flask package.
import flask.views
from flask import Response
#import os # for eval
from fibonacci import fibonacci, fibonacci_xml_response
app = flask.Flask(__name__)
xml = True #Toggles giving the response to the user in an XML format

app.secret_key = "asjklfjlr421509vml5m305kl2m35ijdvm34m5l3y09"

class View(flask.views.MethodView):
    def get(self):
        return flask.render_template("index.html")
        
    def post(self):
        if not(flask.request.form["expression"].isdigit()):
            result = "Please enter a positive integer."
            flask.flash(result)
            return self.get()
        if not xml:
            result = str(fibonacci(flask.request.form["expression"]))
            flask.flash(result)
            return self.get()
        if xml:
            result = str(fibonacci_xml_response(flask.request.form["expression"]))
            
            flask.flash(result)
            #return self.get()
            return self.xml_response(result)

    @app.route('/xml_response')
    def xml_response(self, xml):
        return Response(xml, mimetype='text/xml')


app.add_url_rule("/", view_func=View.as_view("main"))

app.debug = True
app.run()

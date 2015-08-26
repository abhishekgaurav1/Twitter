'''
Created on 25-Aug-2015

@author: Abhishek.Gaurav
'''
import tornado.ioloop
import tornado.web
import os
import OauthRequest
import OauthAccess
import DisplayBox

oauth_token = ""
oauth_token_secret = ""
access_token_key = ""
access_token_secret= ""

class ShowName(tornado.web.RequestHandler):
    def get(self,request = {}):
        global oauth_token
        global oauth_token_secret
        global access_token_key
        global access_token_secret
        request = self.request.arguments
        print request["oauth_verifier"]
        access = OauthAccess.OauthAccess()
        access_token_secret,access_token_key = access.getOauthAccess(oauth_token, oauth_token_secret, request["oauth_verifier"])
        display = DisplayBox.DisplayBox()
        displayName = display.ReturnName(access_token_key, access_token_secret)
        html = """<b>%s</b></br></br>
        <form class="register" action="/showTweet" METHOD="POST">
        <input type="text" name="tweet" maxlength="140"><br>
        <input type="submit" value="submit">
          </form>""" %displayName
        self.write(html)
        
class ShowTweet(tornado.web.RequestHandler):
    def post(self,request = {}):
        global oauth_token
        global oauth_token_secret
        global access_token_key
        global access_token_secret
        request = self.request.arguments
        display = DisplayBox.DisplayBox()
        display.PostTweets(access_token_key, access_token_secret, request["tweet"])
        tweets = display.ReturnTweets(access_token_key, access_token_secret)
        counter = 0
        if len(tweets) >= 10:
            counter = 10
        else:
            counter = len(tweets)
        html = "Here are your Last Tweets </br>"
        for i in range(counter):
            html += "<li>"+tweets[i].text+"</li>"
        self.write(html)
class Test1(tornado.web.RequestHandler):
    def get(self,request = {}):
        self.render('awsform.html')
class Redirect(tornado.web.RequestHandler):
    def get(self):
        global oauth_token
        global oauth_token_secret
        global access_token_key
        global access_token_secret
        authReq = OauthRequest.OauthRequest()
        url,oauth_token,oauth_token_secret = authReq.GetRequest()
        self.redirect(url)
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/test", Test1),
                    (r"/redirect", Redirect),
                    (r"/success", ShowName),
                    (r"/showTweet", ShowTweet),]
        settings = {
                "debug": True,
                "template_path": os.path.join(os.getcwd(), "templates"),
                "static_path": os.path.join(os.getcwd(), "static")
                }
        tornado.web.Application.__init__(self, handlers, **settings)
        
if __name__ == "__main__":
    application = Application()
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
        
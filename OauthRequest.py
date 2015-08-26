'''
Created on 25-Aug-2015

@author: Abhishek.Gaurav
'''
import urlparse
import oauth2 as oauth
 
class OauthRequest():
    consumer_key='fSD8fOrZU4il5YETXjZoqLZLB'   # Fill in your key 
    consumer_secret='N6NLAiaks3NSGCceSwTAQTwGsFZFo0j0IbcfcgR5LTKch9BoPo' # Fill in your secret
    request_token_url='https://api.twitter.com/oauth/request_token'
    access_token_url='https://api.twitter.com/oauth/access_token'
    authorize_url='https://api.twitter.com/oauth/authorize'
 
    def GetRequest(self):
        consumer=oauth.Consumer(self.consumer_key,self.consumer_secret)
        client=oauth.Client(consumer)
        resp, content = client.request(self.request_token_url, "GET")
         
        if resp['status'] != '200':
            raise Exception("Invalid response %s." % resp['status'])
         
        request_token = dict(urlparse.parse_qsl(content))
        return ("%s?oauth_token=%s" % (self.authorize_url, request_token['oauth_token']),request_token['oauth_token'],request_token['oauth_token_secret'])
'''
Created on 25-Aug-2015

@author: Abhishek.Gaurav
'''
import urlparse
import oauth2 as oauth
 
class OauthAccess():
 
    consumer_key='fSD8fOrZU4il5YETXjZoqLZLB'   # Fill in your key 
    consumer_secret='N6NLAiaks3NSGCceSwTAQTwGsFZFo0j0IbcfcgR5LTKch9BoPo' # Fill in your secret
    request_token_url='https://api.twitter.com/oauth/request_token'
    access_token_url='https://api.twitter.com/oauth/access_token'
    authorize_url='https://api.twitter.com/oauth/authorize'
 
    def getOauthAccess(self,oauth_token,oauth_token_secret,oauth_verifier):
        consumer=oauth.Consumer(self.consumer_key,self.consumer_secret)
        token = oauth.Token(oauth_token,oauth_token_secret)
 
        token.set_verifier(oauth_verifier)
        client = oauth.Client(consumer, token)
         
        resp, content = client.request(self.access_token_url, "POST")
        if resp['status'] != '200':
            raise Exception("Invalid response %s." % resp['status'])
        access_token = dict(urlparse.parse_qsl(content))
        return (access_token["oauth_token_secret"],access_token["oauth_token"])
'''
Created on 26-Aug-2015

@author: Abhishek.Gaurav
'''
import twitter
class DisplayBox:
    def ReturnName(self,access_key,access_secret):
        api = twitter.Api(consumer_key='fSD8fOrZU4il5YETXjZoqLZLB',
                              consumer_secret='N6NLAiaks3NSGCceSwTAQTwGsFZFo0j0IbcfcgR5LTKch9BoPo',
                              access_token_key=access_key,
                              access_token_secret=access_secret)
        name = api.VerifyCredentials()
        return name.name
    def ReturnTweets(self,access_key,access_secret):
        api = twitter.Api(consumer_key='fSD8fOrZU4il5YETXjZoqLZLB',
                              consumer_secret='N6NLAiaks3NSGCceSwTAQTwGsFZFo0j0IbcfcgR5LTKch9BoPo',
                              access_token_key=access_key,
                              access_token_secret=access_secret)
        statuses = api.GetUserTimeline()
        return statuses
    def PostTweets(self,access_key,access_secret,tweet):
        api = twitter.Api(consumer_key='fSD8fOrZU4il5YETXjZoqLZLB',
                              consumer_secret='N6NLAiaks3NSGCceSwTAQTwGsFZFo0j0IbcfcgR5LTKch9BoPo',
                              access_token_key=access_key,
                              access_token_secret=access_secret)
        api.PostUpdate(tweet)
        
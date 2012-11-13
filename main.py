from twisted.internet import reactor
from twisted.web.client import Agent
from twisted.web.http_headers import Headers

agent = Agent(reactor)

d = agent.request(
                  'GET', 
                  'http://127.0.0.1:8007', 
                  Headers({'User-Agent': ['Whiskey Aggregator']}), 
                  None)
                  
def cbResponse(ignored):
    print 'Response recieved'
d.addCallback(cbResponse)

def cbShutdown(ignored):
    reactor.stop()
d.addBoth(cbShutdown)

reactor.run()

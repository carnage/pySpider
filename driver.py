'''
Created on 5 May 2012

@author: Carnage
'''

from spider.spider import spider
from spider.plugins import titleTest

#list of plugins to use
plugins = [titleTest.titleTest()]

#blacklist these absolute urls - any urls in this list will not be visited.
blacklistUrls = ['http://www.example.com/forum']

test = spider(plugins, blacklistUrls)
test.spider('http://www.example.com')

test.report()
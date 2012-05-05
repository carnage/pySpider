'''
Created on 5 May 2012

@author: Carnage
'''

import mechanize, urllib2
from collections import deque as Queue

class spider:
    _plugins = []
    _baseUrl = ''
    _errors = {}

    def __init__(self,plugins,blacklist):
        self._plugins = plugins
        self._visited = set()
        self._queue = Queue()   
        self._blacklist = set(blacklist)
        
    def spider(self,url):
        self._queue.append(url)
        self._baseUrl = url
        try:
            while 1:
                url = self._queue.pop()
                self._visit(url)
        except IndexError:
            pass

    def _visit(self,url):
        if url in self._visited:
            return
        print 'visiting: ' + url
        self._visited.add(url)
        br = mechanize.Browser()
        
        try:
            resp = br.open(url)  
        except urllib2.HTTPError, e:
            self._errors[e.geturl()] = [e.getcode()]
            return
        
        if not br.viewing_html():
            return
        
        for plugin in self._plugins:
            plugin.parsePage(br)
        
        unique = set()
        
        for l in br.links():
            if l.absolute_url[0:len(self._baseUrl)] == self._baseUrl and not l.absolute_url in self._blacklist:
                visitableUrl = l.absolute_url.split('#')[0]
                if not visitableUrl in unique and not visitableUrl in self._visited:
                    self._queue.append(visitableUrl)
                    unique.add(visitableUrl)
                    print 'found: ' + visitableUrl
            
        print 'visited: ' + url

    def report(self):
        print self._errors
        
        for plugin in self._plugins:
            plugin.printReport()         
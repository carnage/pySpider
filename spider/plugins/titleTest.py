'''
Created on 5 May 2012

@author: Carnage
'''

from .plugin import plugin

class titleTest(plugin):
    def parsePage(self, br):
        try:
            self._titleLen[br.response().geturl()] = len(br.title())
        except AttributeError:
            self._titleLen = dict()
            self._titleLen[br.response().geturl()] = len(br.title())
    
    def printReport(self):
        print self._titleLen   
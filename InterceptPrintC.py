#-------------------------------------------------------------------------------
# Name:        InterceptPrintM
# Purpose:     A class to allow Python 2.7's print function to be intercepted and augmented
#
# Author:      Simon Cox
#
# Created:     19/10/2015
# Copyright:   (c) Simon Cox 2015
# Licence:     Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
#-------------------------------------------------------------------------------

import traceback
import sys
import datetime

class InterceptPrint(object):

    def __init__(self, linenumber=False, timestamp=False):
        self.realstdout = sys.stdout
        sys.stdout = self
        self.linenumber = linenumber
        self.timestamp = timestamp

    def write(self, message):
        prepends = []
        if self.linenumber:
            prepends.append('Line number: ' + str(traceback.extract_stack()[-2][1]))

        if self.timestamp:
            prepends.append('Datetime: ' + datetime.datetime.now().isoformat())

        if prepends:
            prependstring = ' '.join(prepends) + ' '
        else:
            prependstring =''

        if message == '\n' or message == ' ':
            return
        sys.stdout = self.realstdout
        print prependstring + message
        sys.stdout = self

if __name__ == '__main__':

    ip = InterceptPrint(linenumber=True)

    for i in range(0,100):
        print i, 'hello'

    ip.timestamp = True

    for i in range(0,100):
        print i, 'bob'

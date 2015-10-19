#-------------------------------------------------------------------------------
# Name:        InterceptPrintM
# Purpose:     A module to allow Python 2.7's print function to be intercepted and augmented
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

realstdout = sys.stdout
sys.stdout = sys.modules[__name__]
linenumber = False
timestamp = False

def write(message):
    prepends = []
    if linenumber:
        prepends.append('Line number: ' + str(traceback.extract_stack()[-2][1]))

    if timestamp:
        prepends.append('Datetime: ' + datetime.datetime.now().isoformat())

    if prepends:
        prependstring = ' '.join(prepends) + ' '
    else:
        prependstring =''

    if message == '\n' or message == ' ':
        return
    sys.stdout = realstdout
    print prependstring + message
    sys.stdout = sys.modules[__name__]



#InterceptPrint


Python module/class to intercept the print function and add datetime, line numbers, etc

##How to use

###Module

```python
import InterceptPrintM
InterceptPrintM.timestamp = True # optional, adds a datetime stamp to the print
InterceptPrintM.linenumber = True # optional, adds the line number to the print
```

###Class

```python
import InterceptPrintC
ip = InterceptPrint(datetime=True, linenumber=True)
```
Please note this is not set up as a singleton, multiple instantiation will be terminal. If you're scared, use the module approach.

###Customise
This is written in Python and is pretty easy to understand, it's intended to be customised. Write the prints to a file, or to a database. Email someone. Execute weird and wonderful code (don't do that). Use your imagination.

##Problems
- Currently when printing comma-separated arguments, these end up on multiple lines, e.g.
```python
print "hello", "world"
>>> hello
>>> world
```

#!/usr/bin/env python

a = {}
b = []
print 'hello'

a['name'] = 'whatever'

try:
    print 'string2'
    print a['name']
    print b[0]
    print 'string3'
except KeyError as e:
    print 'There was a key exception'
except IndexError, e:
    print str(e)
    print 'There was an index exception'

print 'world'

import overpy
import json

api = overpy.Overpass()

# My box:

#    "minlat": 37.3612,
#    "minlon": -122.082,
#    "maxlat": 37.4326,
#    "maxlon": -121.965

# Just Sunnyvale or thereabouts.
#
#result = api.query('relation'
#                   '["boundary"="administrative"]'
#                   '(37.3612,-122.082,37.4326,-121.965);out body;')

# All of California...
#
result = api.query('relation'
                   '["boundary"="administrative"]'
                   '(32.0,-125.0,42.0,-114.0);'
                   'out body;')

#print json.dumps(result)
#exit()

print ''

print 'relations %d' % len(result.relations)

print ''

print 'name\tadmin_level\tplace\tboundary\ttype\t%s'

for relation in result.relations:

#    print ''
#
#    for tag in relation.tags:
#        print '%s --> %s' % (tag, relation.tags.get(tag, "n/a"))

     print '%s\t%s\t%s\t%s\t%s\t%d' % (relation.tags.get('name','').encode('utf8'),
                                       relation.tags.get('admin_level','').encode('utf8'),
                                       relation.tags.get('place','').encode('utf8'),
                                       relation.tags.get('boundary','').encode('utf8'),
                                       relation.tags.get('type','').encode('utf8'),
                                       relation.id)
 
print ''

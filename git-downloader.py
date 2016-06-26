# import json
# import urllib2
# import urllib
# import socket
# socket.setdefaulttimeout(15)
#
# has_records = True
# start_index = 0;
#
# while has_records == True:
#     end_index = start_index + 1
#     url = "http://www.krazychefs.com/web/getrecord?start="+str(start_index)+"&end="+str(end_index)
#     response = urllib2.urlopen(url)
#     data = response.read()
#     array = json.loads(data)
#     if array and len(array) > 0:
#         if array[0].has_key("imgUrls") and array[0]['imgUrls'] is not None and array[0]['imgUrls'] is not "None" and str(array[0]['imgUrls']) is not "":
#             print array[0]['imgUrls']
#             if array[0]['imgUrls'].index("githubusercontent") != -1:
#                 if array[0]['_id'] is not None:
#                     urllib.urlretrieve(array[0]['imgUrls'], array[0]['_id']+".jpg")
#         else:
#             print "http://www.krazychefs.com/krazychefs/attachment/"+array[0]['imageId']
#             try:
#                 urllib.urlretrieve("http://www.krazychefs.com/krazychefs/attachment/"+array[0]['imageId'], array[0]['_id']+".jpg")
#             except:
#                 print "Error: http://www.krazychefs.com/krazychefs/attachment/"+array[0]['imageId']
#         start_index = end_index
#     else:
#         has_records = False
# print "Completed"


import json
import urllib2
import urllib
import socket
import os
import sys
import cgi
socket.setdefaulttimeout(15)

has_records = True
start_index = 0;

while has_records == True:
    end_index = start_index + 1
    url = "http://www.krazychefs.com/web/getrecord?start="+str(start_index)+"&end="+str(end_index)
    response = urllib2.urlopen(url)
    data = response.read()
    array = json.loads(data)
    if array and len(array) > 0:
        if array[0].has_key("steps"):
            print array[0]['_id']
            if array[0]['_id'] is not None:
                # print array[0]['steps'].decode('ascii', 'ignore')
                print "audio/"+array[0]['_id']+".mp4"
                value = cgi.escape(array[0]['title']).encode("ascii", "replace")
                value = value + " . "
                value = value + "Preparation time"
                value = value + array[0]['prepTime']
                value = value + " . "
                value = value + "Ingredients"
                value = value + cgi.escape(array[0]['ingredients']).encode("ascii", "replace")
                value = value + " . "
                value = value + "Preparation method"
                value = value + cgi.escape(array[0]['steps']).encode("ascii", "replace")
                value = cgi.escape(value).encode("ascii", "replace")
                os.system("/usr/bin/say -v Victoria -o audio/"+array[0]['_id']+".mp4 \""+ value +"\"")
        start_index = end_index
    else:
        has_records = False
print "Completed"

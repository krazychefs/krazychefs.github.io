import json
import urllib2
import urllib
import socket
socket.setdefaulttimeout(15)

has_records = True
start_index = 0;

while has_records == True:
    end_index = start_index + 1
    url = "http://www.krazychefs.com/web/getrecord?start="+str(start_index)+"&end="+str(end_index)
    response = urllib2.urlopen(url, timeout=4)
    data = response.read()
    array = json.loads(data)
    if array and len(array) > 0:
        if array[0].has_key("imgUrls") and array[0]['imgUrls'] is not None and array[0]['imgUrls'] is not "None" and str(array[0]['imgUrls']) is not "":
            print array[0]['imgUrls']
            if array[0]['_id'] is not None:
                urllib.urlretrieve(array[0]['imgUrls'], array[0]['_id']+".jpg")
        else:
            print "http://www.krazychefs.com/krazychefs/attachment/"+array[0]['_id']
            try:
                urllib.urlretrieve("http://www.krazychefs.com/krazychefs/attachment/"+array[0]['_id'], array[0]['_id']+".jpg")
            except:
                print "Error: http://www.krazychefs.com/krazychefs/attachment/"+array[0]['_id']
        start_index = end_index
    else:
        has_records = False
print "Completed"

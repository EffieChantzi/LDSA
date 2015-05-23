
#!/usr/bin/env python

import swiftclient

username = 'efch0787'
password = 'wpfeP429::ec'
tenant_name = 'g2015016'
#auth_url = 'http://smog.uppmax.uu.se:5000/v2.0'

swift = swiftclient.client.Connection(auth_version='2',
                                      user=username,
                                      key=password,
                                      tenant_name=tenant_name,
                                      authurl='http://smog.uppmax.uu.se:5000/v2.0',
)

#(response, bucket_list) = swift. get_account()
#for bucket in bucket_list:
        #print bucket['name']
(response, obj_list) = swift.get_container('GenomeData')
for i in obj_list:
        print i['name']

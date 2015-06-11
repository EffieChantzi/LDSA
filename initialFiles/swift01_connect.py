
#!/usr/bin/env python

import swiftclient

username = ''
password = ''
tenant_name = ''
#auth_url = ''

swift = swiftclient.client.Connection(auth_version='2',
                                      user=username,
                                      key=password,
                                      tenant_name=tenant_name,
                                      authurl='',
)

#(response, bucket_list) = swift. get_account()
#for bucket in bucket_list:
        #print bucket['name']
(response, obj_list) = swift.get_container('GenomeData')
for i in obj_list:
        print i['name']


# API Tester Class
# Author: Prashanth Raghavan
# Description: This class contains a set of pre-defined tests to test the user creation API at
# http://interview.onforce.com/qe/. This also contains methods to obtain user input for user 
# creation and validation

import requests
import re
from collections import OrderedDict
from telnetlib import STATUS


class ApiTester(object):
    
    def __init__(self,url,data):
        self.url = url
        self.data = data
        
        
        fields= ['firstName', 'lastName', 'username','password','email','phoneNumber']
        #self.val_functions = OrderedDict([
        #                        ('firstName', self.val_name), 
        #                        ('lastName', self.val_name),
        #                        ('username', self.val_user),
        #                        ('password', self.val_pass),
        #                        ('email'   , self.val_email),
        #                        ('phoneNumber', self.val_phone)
        #                        ])
                                
    
    def post_req(self):
        status = 0
        req = requests.post(self.url,json=self.data)
        resp_json = req.json()
        if resp_json['success'] == 'True' :
            print("User {} creation successful!\n".format(self.data['username']))
            status +=1
        else :
            print("User {} creation failed with the following error(s):\n")
            for err in resp_json['errors']:
                print("{}\n".format(err))
        
        return status
    
    def file_parse(self,file):
        
        status = 0
        self.tlist = list()
        try:
            with open(file) as f :
                for line in f.strip("{} \t\n") :
                    if re.match(".*:", line, re.I) :
                        (k,v) = line.split(':')
                        if k not in fields :
                            print("{} is not a valid field. Valid fields are ".format(' '.join(map(str,fields))))
                            return status
                        else :
                            self.data[k] = v
                            
                for k in fields:
                if k not in self.data :
                    print("{} missing in file")
                            
                        
                
            
    
    
                
            
    
        
        
        
        
    


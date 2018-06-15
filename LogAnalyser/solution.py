import json
import os
import logging
import sys
import re
import hashlib
from pprint import pprint


# Creted the solution on basis of four parts of the entitre message

#   1 - the stuck reason (extracted before the POST parameter and 
#       after the post parameter
#
#   2- service upon POSTing to which the error occured
#
#   3- the stack trace part

# Logic Explanation
# stack trace is something which will ever generate a specific digest code
# if for a specific url for a particular error digest is not present 
# than insertr all the informatio, if for the same url erro is different then 
# increased the occurance and inserted the error message in the list and also 
# unserted the new digest in the digest list
#



# exception reason part 1
#group1
stuck_trace_1_regex = re.compile(r'((\[)STUCK(\])\s+(.*))')


#The URL which which was being accessed when exception occured
#group2
post_url = re.compile(r'(\[)\nPOST\s+(.*)')

# exception reason part 1
#group1
stuck_trace_2_regex = re.compile(r'\]",\s+(.*)\s*Stack\s+trace')

#exception stack trace
#group
stack_trace_regex = re.compile(r'Stack\s+trace[:](\n.*)*')

class Solution:
    def __init__(self, data_file=None):

        #The error message
        self.stuck_reason = None

        #service url
        self.request_url = None

        #stack trace
        self.stack_trace = None


        self.solution_dict = {}
        self.json_data = None
        #default log location
        self.default_location =\
             os.path.join(os.environ['HOME'], 'oracle') 
        

        if not data_file:
            self.logfile = 'sample.log'
        else:
            self.logfile = data_file


    def get_json_log(self):
        try:
            self.json_data = json.loads(open(self.logfile).read())
        except Exception as exc:
            print(exc) 
        return self.json_data


    def get_digest(self, data):
        m = hashlib.md5()
        m.update(data)
        return m.hexdigest()


    def populate(self):
        self.get_json_log()
        if not self.json_data:
            print("Failed to read the data")
            sys.exit()

        for node in self.json_data['hits']['hits']:
            stuck, stuck1, stuck2, stack_trace, service_url = None, None, None, None, None
            try:
                stuck1 = re.search(stuck_trace_1_regex, node['_source']['msgText']).group(1)
            except Exception as exc:
                print(exc)

            try:
                stuck2 = re.search(stuck_trace_2_regex, node['_source']['msgText']).group(1)
            except Exception as exc:
                print(exc)

            try:
                service_url = re.search(post_url, node['_source']['msgText']).group(2)
            except Exception as exc:
                print(exc)


            try:
                stack_trace = re.search(stack_trace_regex, node['_source']['msgText']).group()
            except Exception as exc:
                print(exc)

            #import pdb;pdb.set_trace()
            stuck = stuck1+stuck2

            #get the digest of stack trace
            stack_trace_digest = self.get_digest(stack_trace)
       
            if service_url not in self.solution_dict.keys():
                self.solution_dict[service_url] = {'stack_trace_digest':[stack_trace_digest],
                                                   'occurance':1,
                                                   'error_reasons':[stuck] 
                                                 }
            else:
                if stack_trace_digest in self.solution_dict[service_url]['stack_trace_digest']:
                    self.solution_dict[service_url]['occurance']+=1
                else:
                    self.solution_dict[service_url]['occurance']+=1
                    self.solution_dict[service_url]['error_reasons'].append(stuck)
                    self.solution_dict[service_url]['stack_trace_digest'].append(stack_trace_digest)

        return self.solution_dict

if __name__ == "__main__":
    pprint(Solution().populate())

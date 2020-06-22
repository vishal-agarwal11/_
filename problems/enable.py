import requests
#import pdb
import json

data = {
   "India": {
      "properties": {
        "totalconfirmed": {
          "type": "text",
          "fielddata": "true"
        }
      }
   }
}


data1 = {"mappings": {
    "my-type": {
      "properties": {
        "totalconfirmed": {
          "type": "text",
          "fielddata": "true"
        }
      }
    }
  }
}

headers = {"Content-Type": "application/json"}

es_url = "http://10.145.68.212:9200/my-index"
res = requests.put(
                    es_url,
                    data=json.dumps(data1),
                    headers=headers)


print(res.text)
#pdb.set_trace()



curl -XPUT http://10.145.68.212:9200/my-index  -H 'Content-Type: application/json' -d '{
  "mappings": {
    "mytype": {
      "properties": {
        "publis": {
          "type": "long",
          "fielddata": true
        }
      }
    }
  }
}'



curl -XPUT http://10.145.68.212:9200/user 


curl -XPUT http://10.145.68.212:9200/user/_mapping -H 'Content-Type: application/json' -d '{
  "properties": {
    "name": {
      "type": "keyword"
    },
    "loginCount": {
      "type": "long"
    }
  }
}'



curl -XPOST http://10.145.68.212:9200/user/_doc/ -H 'Content-Type: application/json' -d '{
  "name": "John",
  "loginCount": 4
}'




curl -XPUT http://10.145.68.212:9200/user -H 'Content-Type: application/json' -d '{
  "mappings": {
    "doc": {
      "properties": {
        "publisher": {
          "type": "text",
          "fielddata": true
        }
      }
    }
  }
}'


curl -XPUT http://10.145.68.212:9200/my-index










curl -XPOST http://10.145.68.212:9200/my-index/_doc/ -H 'Content-Type: application/json' -d '{
  "employee-id": "25"
}'




curl -XPUT http://10.145.68.212:9200/my-index -H 'Content-Type: application/json' -d '{
  "mappings": {
    "properties": {
      "session_data": {
        "type": "object",
        "enabled": false
      }
    }
  }
}'


curl -XPUT http://10.145.68.212:9200/my-index -H 'Content-Type: application/json' -d '{
  "session_data": "foo bar" 
}'






------------------------------------



curl -XPUT http://10.145.68.212:9200/my-index

curl -XPUT http://10.145.68.212:9200/my-index -H 'Content-Type: application/json' -d '{
  "mappings": {
    "_field_names": {
      "enabled": true
    }
  }
}'


curl -X PUT "10.145.68.212:9200/my-index/_mapping?pretty" -H 'Content-Type: application/json' -d'{
  "properties": {
    "employee-id": {
      "type": "keyword",
      "index": true
    }
  }
}'



curl -XPOST http://10.145.68.212:9200/my-index/_doc/ -H 'Content-Type: application/json' -d '{
  "employee-id": "2885"
  "city":"Bangalore"
}'





--------------------------------
curl -XPUT http://10.145.68.212:9200/test

curl -XPOST "10.145.68.212:9200/test/doc?pretty" -H "Content-Type: application/json" -d '{
    "properties": {
        "city": {
          "type": "keyword",
          "index": false
        }
    }
}'

curl -XPOST "10.145.68.212:9200/test/doc?pretty" -H "Content-Type: application/json" -d '{
    "properties": {
        "description": {
            "type": "keyword",
            "index": false
        }
    }
}'

curl -XPOST http://10.145.68.212:9200/test/doc -H 'Content-Type: application/json' -d '{
  "city": "New York"
}'


curl -XPOST http://10.145.68.212:9200/test/doc -H 'Content-Type: application/json' -d '{
  "city": "Old York"
}'

curl -XPOST http://10.145.68.212:9200/test/doc/_search -H 'Content-Type: application/json' -d '{'
  "query": {
    "match": {
      "name": "find"
    }
  }
}'












curl -XPOST http://10.145.68.212:9200/api/datasources/proxy/5/_msearch?max_concurrent_shard_requests=5


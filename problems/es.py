

`Creating Inex`
curl -XPUT http://localhost:9200/course

`adding an item`
curl -XPUT http://localhost:9200/course/product -H 'Content-Type: application/json' -d'{
    "category" : "mobile",
    "company" : "Samsung",
    "model" : "A31",
    "cost" : 10000,
    "colors" :["Red", "Black", "White"]
    }

{   
    "_index":"course",
    "_type":"product",
    "_id":"5oNGc3EBD-RpcmJKGUDP",
    "_version":1,
    "result":"created",
    "_shards":{
        "total":2,
        "successful":1,
        "failed":0
        },
    "_seq_no":0,
    "_primary_term":1
}

`Retreving data`
curl -XGET http://localhost:9200/course/product/5oNGc3EBD-RpcmJKGUDP?pretty
{
  "_index" : "course",
  "_type" : "product",
  "_id" : "5oNGc3EBD-RpcmJKGUDP",
  "_version" : 1,
  "_seq_no" : 0,
  "_primary_term" : 1,
  "found" : true,
  "_source" : {
    "category" : "mobile",
    "company" : "Samsung",
    "model" : "A31",
    "cost" : 10000,
    "colors" : [
      "Red",
      "Black",
      "White"
    ]
  }
}


`Updating `
curl -XPUT http://localhost:9200/course/product/5oNGc3EBD-RpcmJKGUDP -H 'Content-Type: application/json' -d'{
    "category" : "mobile",
    "company" : "Samsung",
    "model" : "A31",
    "cost" : 10000,
    "colors" : ["Blue", "Black", "White"]
}'
{
    "_index":"course",
    "_type":"product",
    "_id":"5oNGc3EBD-RpcmJKGUDP",
    "_version":2,           `Version changed to 2 upon updating`
    "result":"updated",
    "_shards":{
        "total":2,
        "successful":1,
        "failed":0
        },
    "_seq_no":1,
    "_primary_term":1
}



`Adding a new fied`

curl -XPOST http://localhost:9200/course/product/5oNGc3EBD-RpcmJKGUDP/_update?pretty -H 'Content-Type: application/json' -d'{
    "doc" : { 
        "Reviews" : ["Great", "Nice"] }
}'

{
  "_index" : "course",
  "_type" : "product",
  "_id" : "5oNGc3EBD-RpcmJKGUDP",
  "_version" : 3,
  "result" : "updated",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 2,
  "_primary_term" : 1
}


`Retrieving `
curl -XGET http://localhost:9200/course/product/5oNGc3EBD-RpcmJKGUDP?pretty
{
  "_index" : "course",
  "_type" : "product",
  "_id" : "5oNGc3EBD-RpcmJKGUDP",
  "_version" : 3,
  "_seq_no" : 2,
  "_primary_term" : 1,
  "found" : true,
  "_source" : {
    "category" : "mobile",
    "company" : "Samsung",
    "model" : "A31",
    "cost" : 10000,
    "colors" : [
      "Blue",
      "Black",
      "White"
    ],
    "Reviews" : [
      "Great",
      "Nice"
    ]
  }
}


`script execution`

curl -XPOST http://localhost:9200/course/product/5oNGc3EBD-RpcmJKGUDP/_update?pretty -H 'Content-Type: application/json' -d'{
    "script" : "ctx._source.cost += 500" 
}'

{
  "_index" : "course",
  "_type" : "product",
  "_id" : "5oNGc3EBD-RpcmJKGUDP",
  "_version" : 4,
  "result" : "updated",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 3,
  "_primary_term" : 1
}

curl -XGET http://localhost:9200/course/product/5oNGc3EBD-RpcmJKGUDP?pretty
{
  "_index" : "course",
  "_type" : "product",
  "_id" : "5oNGc3EBD-RpcmJKGUDP",
  "_version" : 4,
  "_seq_no" : 3,
  "_primary_term" : 1,
  "found" : true,
  "_source" : {
    "category" : "mobile",
    "company" : "Samsung",
    "model" : "A31",
    "cost" : 10500,
    "colors" : [
      "Blue",
      "Black",
      "White"
    ],
    "Reviews" : [
      "Great",
      "Nice"
    ]
  }
}


`dding another item`

curl -XPOST http://localhost:9200/course/product -H 'Content-Type: application/json' -d'{
    "category" : "mobile",
    "company" : "Samsung",
    "model" : "A51",
    "cost" : 21000,
    "colors": ["Red", "Black", "White"]
}'

{
    "_index":"course",
    "_type":"product",
    "_id":"6INic3EBD-RpcmJKP0Bj",
    "_version":1,
    "result":"created",
    "_shards":{
        "total":2,
        "successful":1,
        "failed":0},
    "_seq_no":4,
    "_primary_term":1
}


`Deleting item`

curl -XDELETE http://localhost:9200/course/product/6INic3EBD-RpcmJKP0Bj?pretty
{
  "_index" : "course",
  "_type" : "product",
  "_id" : "6INic3EBD-RpcmJKP0Bj",
  "_version" : 2,
  "result" : "deleted",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 5,
  "_primary_term" : 1
}







curl -XPUT http://localhost:9200/logs -H 'Content-Type: application/json' -d '{
  "mappings": {
    "_source": {
      "includes": [
        "*.count",
        "meta.*"
      ],
      "excludes": [
        "meta.description",
        "meta.other.*"
      ]
    }
  }
}'

curl -XPUT http://localhost:9200/logs/_doc/1 -H 'Content-Type: application/json' -d '{
  "requests": {
    "count": 10,
    "foo": "bar" 
  },
  "meta": {
    "name": "Some metric",
    "description": "Some metric description", 
    "other": {
      "foo": "one", 
      "baz": "two" 
    }
  }
}'



curl -XGET http://localhost:9200/logs/_search?pretty -H 'Content-Type: application/json' -d '{
  "query": {
    "match": {
      "meta.other.foo": "one" 
    }
  }
}'
{
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 0.2876821,
    "hits" : [
      {
        "_index" : "logs",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 0.2876821,
        "_source" : {
          "meta" : {
            "other" : { },
            "name" : "Some metric"
          },
          "requests" : {
            "count" : 10
          }
        }
      }
    ]
  }
}




curl -XPUT -H "Content-Type: application/json;charset=UTF-8" 'http://localhost:9200/_snapshot/esrestore -d ‘{
  "type": "fs",
  "settings": {
     "location": "/esdata/esbackup",
     "compress": true
  }
}'

curl  -XPOST "http://10.0.0.2:9200/_snapshot/esrestore/mybackup/_restore?wait_for_completion=true" -d '{
  "indices": "service-mesh-tests",
  "ignore_unavailable": true,
  "include_global_state": true,
  "rename_pattern": "index_(.+)",
  "rename_replacement": "restored_index_$1"
}'

curl -XPOST -H "Content-Type: application/json;charset=UTF-8" http://localhost:9200/_snapshot/my_backup/snapshot_1/_restore -d '{
  "indices": "index_1,index_2",
  "ignore_unavailable": true,
  "include_global_state": true,
  "rename_pattern": "index_(.+)",
  "rename_replacement": "restored_index_$1"
}'




curl  -XPOST -H "Content-Type: application/json;charset=UTF-8" locahost:9200/_snapshot/esbackup/mybackup/_restore?wait_for_completion=true -d '{
  "indices": "service-mesh-tests",
  "ignore_unavailable": true,
  "include_global_state": true,
}'


curl -XPUT  "http://localhost:9200/_snapshot/backup/mybackup3?wait_for_completion=true&pretty=true" -H "Content-Type: application/json;charset=UTF-8" -d '{
  "indices": "blog,course",
  "ignore_unavailable": true,
  "include_global_state": false,
  "rename_pattern": "index_(.+)",
  "rename_replacement": "restored_index_$1"
}'



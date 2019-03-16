  "use strict";

  var http = require ('http');
  var redisStore = require('connect-redis');
  var redis = require ('redis');
  var client = redis.createClient({host : '35.190.194.170', port : 6379});
  
  client.on('connect', function(){
             console.log ('Redis Client connected from function handleGET!!');
    
             });

 client.on('error', function(err){
            console.log('Error when connecting from handleGET.. ' + err);
            });




function handleGET (req, res){
  
  let user;   
  let key;
  user= req.body.user;
  key= req.body.key;
 
 
        
    client.hgetall(key, function (error, results)
          {
        
    res.status(200).send(results);}
       );
       
}

function handlePOST (req, res) {
 /*   var http = require ('http');
  var redisStore = require('connect-redis');
  var redis = require ('redis');
  var client = redis.createClient({host : '35.240.113.134', port : 6379});*/
  

let key;
let user;
//var fields = new Array();
let field0;
let field1;
let field2;
let field3;
let field4;
let field5;
let field6;
let field7;
let field8;
let field9;
user = req.body.user;
key= req.body.key;
field0 = req.body.field0;
field1 = req.body.field1;
field2 = req.body.field2;
field3 = req.body.field3;
field4 = req.body.field4;
field5 = req.body.field5;
field6 = req.body.field6;
field7 = req.body.field7;
field8 = req.body.field8;
field9 = req.body.field9;
client.hmset(key, ["field0", field0, "field1", field1, "field2", field2, "field3", field3, "field4", field4, "field5", field5, "field6", field6, "field7", field7, "field8", field8 ,"field9",field9], function (err, results)  
     {res.status(200)} );
}

exports.hello = (req , res) =>
{
  
    switch (req.method) {
    case 'GET':
      handleGET(req, res);
      break;
    case 'POST':
      handlePOST(req, res);
      res.status(200).send();
      break;
    default:
      res.status(500).send({ error: 'Something blew up!' });
      break;
  }
};
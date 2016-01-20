var express = require('express')
var app = express()

app.get('/', function (req, res) {
  res.send('Hello World!')
})

app.listen(3000,'localhost',function() {
  console.log('Robot is listening on port 3000!')
})
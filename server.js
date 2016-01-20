var express = require('express')
var app = express()

app.get('/', function (req, res) {
  res.send('Hello.')
})

app.listen(3000,'0.0.0.0',function() {
  console.log('Robot is listening on port 3000...')
})
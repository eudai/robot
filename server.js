var express = require('express')
var app = express()
var robot = require('./library/robot')
var os = require('os')

app.get('/:command',function(req,res){
	var command = req.params.command
    var options = {}
    for ( var key in req.query ){
        options[key] = req.query[key]
    }
	robot.execute(command,options,function(error,data){
		res.json( error || data )
	})
})

app.use(express.static('public'));

app.listen(3000,'0.0.0.0',function() {
    var name = os.hostname().split('.')[0]
    var interfaces = os.networkInterfaces()
    var address = interfaces.en0[1].address
	console.log('%s is listening at %s:3000',name,address)
})
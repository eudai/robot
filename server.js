var express = require('express')
var app = express()
var robot = require('./library/robot')

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
	console.log('Robot is listening on port 3000...')
})
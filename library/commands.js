// commands should follow the following format:
// function ([options],callback) { callback(error,data) }

var movement = require('movement')
 

var commands = {
    
    hello: function(options,callback){
        var name = options.name || "World" 
        var response = "Hello, " + name + "."
        callback(null,response)
    } 

    forward: function(options,callback){


    	
    }
    
}

module.exports = commands
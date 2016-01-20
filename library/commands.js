// commands should follow the following format:
// function ([options],callback) { callback(error,data) }
 

var commands = {
    
    hello: function(options,callback){
        var name = options.name || "World" 
        var response = "Hello, " + name + "."
        callback(null,response)
    }  
    
}

module.exports = commands
var os = require('os')
var commands = require('./commands')

var Robot = function(){

	var execute = function(command,options,callback){
		if ( typeof commands[command] == 'function' ){
			if ( !options || typeof options == 'function' ){     // makes options optional
                callback = options
                options = {}
            }
            if ( !callback || typeof callback != 'function' ){   // makes callback optional
                callback = function(error,data){
                    console.log( error || data )
                }
            }
			try {                                                // attempts to execute command
				commands[command](options,callback)
			} catch (error) {
				callback(error)
			}
		} else {
            callback({
                error: true,
                reason: 'Unkown command: ' + command
            })
        }
	}
    
    var name = function(){
        return os.hostname().split('.')[0]
    }()
    
    var address = function(){
        var adapters = os.networkInterfaces()
        for ( var key in adapters ){
            var ifaces = adapters[key]
            for ( var i in ifaces ){
                var iface = ifaces[i]
                if ( iface.family == "IPv4" && iface.internal == false )
                return iface.address
            }
        }
    }()

    this.name = name
	this.address = address
    this.execute = execute
    

}

module.exports = new Robot
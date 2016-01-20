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

	this.execute = execute

}

module.exports = new Robot
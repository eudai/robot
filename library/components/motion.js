var Cylon = require('cylon')


Cylon.robot({
			
	connections: {
		raspi: { adaptor: 'raspi' }
	},

	devices: {
		rightForwardMotor: { driver: 'motor', pin: 16 },
		rightBackwardMotor: { driver: 'motor', pin: 15 },
		leftForwardMotor: { driver: 'motor', pin: 23 },
		leftBackwardMotor: { driver: 'motor', pin: 24}		
	},

	work: function(my){
		my.rightForwardMotor.speed(100)
		my.rightBackwardMotor.stop()
		my.leftForwardMotor.speed(100)
		my.leftBackwardMotor.stop()

		after((5).seconds(),function(){
			my.rightForwardMotor.stop()
			my.leftForwardMotor.stop()
		})
	}


}).start()


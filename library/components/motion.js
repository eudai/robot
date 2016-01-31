var Cylon = require('cylon')


Cylon.robot({
			
	connections: {
		raspi: { adapter: 'raspi' }
	},

	devices: {
		motors: {
			right: {
				foward: { driver: 'motor', pin: 16 },
				backward: { driver: 'motor', pin: 15 }
			},
			left: {
				forward: { driver: 'motor', pin: 23 },
				backward: { driver: 'motor', pin: 24}
			}
		}
		
	},

	work: function(my){
		my.motors.right.forward.speed(100)
		my.motors.right.backward.stop()
		my.motors.left.forward.speed(100)
		my.motors.left.backward.stop()

		after((5).seconds(),function(){
			my.motors.right.forward.stop()
			my.motors.left.forward.stop()
		})
	}


})


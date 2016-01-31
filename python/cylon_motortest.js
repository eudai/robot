var Cylon = require('cylon');

Cylon.robot({
  connections: {
    raspi: { adaptor: 'raspi' }
  },

  devices: {
    motorL: {driver: 'motor', pin: 23 }
    motorLR: {driver: 'motor', pin: 24}
    motorR: {driver: 'motor', pin: 15}
    motorRR: {driver: 'motor', pin: 16}
    L_Speed: {driver: 'motor', pin: 18}
    R_Speed: {driver: 'motor', pin: 12}

  },

  work: function(my) {
    my.motorLR.turnOn();
    my.motorRR.turnOn();
    my.L_Speed.speed(100);
    my.R_Speed.speed(100);
    

    after((5).seconds(), function() {
      my.motor.stop();
    });
  }
}).start();

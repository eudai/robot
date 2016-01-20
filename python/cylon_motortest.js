var Cylon = require('cylon');

Cylon.robot({
  connections: {
    raspi: { adaptor: 'raspi' }
  },

  devices: {
    motorLR: { driver: 'motorL', pin: 23 }
    motorLF: {driver: 'motorL2', pin: 24}
    motorRF: {driver: 'motorR', pin: 15}
    motorRR: {driver: 'motorR2', pin: 16}
    L_Speed: {driver: 'L_Speed', pin: 18}
    R_Speed: {driver: 'R_Speed', pin: 12}

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
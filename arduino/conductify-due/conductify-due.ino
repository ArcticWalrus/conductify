#include "MPU9250.h"

MPU9250 mpu;
uint8_t is_conducting;
float volume;
uint8_t channel;
float yaw;

void setup()
{
    Wire.begin();
    Serial.begin(115200);

    delay(2000);
    mpu.setup();
}

void loop()
{
    mpu.update();
    if (Serial.available())
    {
        while(Serial.available()){
          Serial.read();
        }
        if(abs(mpu.getRoll()) < 120 ){
          is_conducting = 1;
        }
        else {
          is_conducting = 0;
        }

        volume = 1 - (mpu.getPitch() + 50)/100;
        if(volume < 0) volume = 0;
        else if(volume > 1) volume = 1;

        yaw = mpu.getYaw();
        if(abs(yaw) > 160 ) channel = 2;
        else if(abs(yaw) > 100 & yaw < 0) channel = 1;
        else if(abs(yaw) > 40 & yaw < 0) channel = 0;
        else if(abs(yaw) > 100 & yaw > 0) channel = 3;
        else if(abs(yaw) > 40 & yaw > 0) channel = 4;
        else channel = -1;
        
        Serial.print(is_conducting);
        Serial.print(", ");
        Serial.print(volume);
        Serial.print(", ");
        Serial.println(channel);

    }
}

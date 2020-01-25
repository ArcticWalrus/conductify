#include "MPU9250.h"

MPU9250 mpu;

void setup()
{
    Serial.begin(115200);

    Wire.begin();

    delay(2000);
    mpu.setup();
}

void loop()
{
    mpu.update();
    delay(1);
    if (Serial.available())
    {
        while(Serial.available()){
          Serial.read();
        }
        Serial.print(mpu.getPitch());
        Serial.print(", ");
        Serial.println(mpu.getYaw());

    }
}

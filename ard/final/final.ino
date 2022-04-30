#include <EEPROM.h>
#include <OneWire.h>
#include <GravityTDS.h>
#include <DallasTemperature.h>

GravityTDS gravityTds;
OneWire oneWire(2);
DallasTemperature sensors(&oneWire);

int buffer_arr[10], temp;
float calibration_value = 21.84;
float ppm = 0;
float degc = 0;
float volt;
float ntu;
unsigned long int avgval;

void setup()
{
  Serial.begin(9600);
  sensors.begin();
  gravityTds.setPin(A3);
  gravityTds.setAref(5.0);
  gravityTds.setAdcRange(1024);
  gravityTds.begin();
}

void loop(){
  //temp degc
  sensors.requestTemperatures();
  degc = sensors.getTempCByIndex(0);

  //ph
  for (int i = 0; i < 10; i++)
  {
    buffer_arr[i] = analogRead(A2);
    delay(30);
  }
  for (int i = 0; i < 9; i++)
  {
    for (int j = i + 1; j < 10; j++)
    {
      if (buffer_arr[i] > buffer_arr[j])
      {
        temp = buffer_arr[i];
        buffer_arr[i] = buffer_arr[j];
        buffer_arr[j] = temp;
      }
    }
  }
  avgval = 0;
  for (int i = 2; i < 8; i++)
    avgval += buffer_arr[i];
  float volt = (float)avgval * 5.0 / 1024 / 6;
  float ph = -5.70 * volt + calibration_value;

  //tds ppm
  gravityTds.setTemperature(27);  // set the temperature and execute temperature compensation
  gravityTds.update();  //sample and calculate
  ppm = gravityTds.getTdsValue();  // then get the value

  //turb ntu
  volt = 0;

  for (int i = 0; i < 800; i++)
  {
    volt += ((float)analogRead(A0) / 1023) * 5;
  }
  volt = volt / 800;
  volt = round_to_dp(volt, 2);

  if (volt < 2.5) {
    ntu = 3000;
  }
  else {
    ntu = -1120.4 * square(volt) + 5742.3 * volt - 4353.8;
  }
  Serial.print(degc,2);
  Serial.print(',');
  Serial.print(ph,2);
  Serial.print(',');
  Serial.print(ppm,0);
  Serial.print(',');
  Serial.println(ntu,0);
  delay(1000);
}

float round_to_dp(float in_value, int decimal_place){
  float multiplier = powf( 10.0f, decimal_place );
  in_value = roundf( in_value * multiplier ) / multiplier;
  return in_value;
}

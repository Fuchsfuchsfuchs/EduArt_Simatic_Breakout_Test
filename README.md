# EduArt_Simatic_Breakout_Test

## Introduction

This repository contains the ECAD Files and the code for a project which was created in the time at my Internship at EduArt Robotics. On the top side of the Eduard Robot sits a breakout Board for the Simatic IoT 2050 GPIO Pins. The Board is connected to the IPC with a flat ribbon cable which could be prone to cracks. So a simple solution to test the Robot before shipping was searched for. You plug the Simatic_Breakout_Test in and run the IOT_PCB_TEST program on the Robot. LEDs indicate for each pin if the connection works.

## How to use

Flash the Arduino Nano with the **NANO_PCB_TEST.ino** and place the Testboard on the IoT Breakout on the back of the Eduard Robot. After that execute the **IOT_PCB_TEST.py** on the Robot.

First run 
```
chmod +x IOT_PCB_TEST.py
```
to make the file executable. After that you can run the programm with:
```
sudo python3 IOT_TEST_PCB.py
```

GPIOs D0 and D1 are not tested, they are non existent on the Breakout board and are used to communicate with the Motorcontrollers.
The GPIOs D2 - D7 are directly tested if they are connected. GPIOs D8 to D13 and A0 to A5 are tested in pairs. So A0 gets a Signal from the Arduino and D8 is set to Output a HIGH Signal, which the Arduino receives and the A0 and D8 LEDs will light up. If one of the GPIOs is not connected or doesnt work properly both LEDs (A0 and D8) will not work.
The paired GPIOs are the following: A0 and D8, A1 and D9, A2 and D10, A3 and D11, A4 and D12, A5 and D13.

## Bill of Materials (BOM)

| Component    | Datasheet | Amount | Value  |
| ------------ | --------- | ------ | ------ |
| LED 1        | [WS2812B](https://www.digikey.com/en/htmldatasheets/production/1829370/0/0/1/ws2812b)      | 18     |        |
| Capacitors   | ToDo      | 18     | 100 nF |
| Arduino Nano | [Arduino Nano](https://docs.arduino.cc/hardware/nano/)      | 1      |        |
| Resistor     | ToDo      | 1      | 10K    |
| LED 2        | ToDo      | 1      |        |

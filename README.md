# Davy Crocket

## Wi-Fi tracking extraordinaire

Wrote this little program to work with an arduino. The idea is to have two different wireless cards listening to the RSSI (signal strength) of the same Wi-Fi Access Point (AP). Based on the RSSI of both antennas it will send a serial signal to an arduino attached to a servo or stepper motor. The Arduino will then skew the antenna array in the direction of the best signal.

You'll have to manual input what USB port you're using and make sure the Arduino gets flashed with the right code to receive the input. Additionally, i've only been successful if I have the Arduino serial monitor window open.

Have bench tested this successfully but have yet to actually implement all the physical components together.

===

Using:
    Kali Linux
    Python (pyshark, numpy, serial)
    tshark
    Arduino Uno
    Microstep Driver CW230 + Stepper Motor NEMA 23 from BuildYourOwnCNC.com
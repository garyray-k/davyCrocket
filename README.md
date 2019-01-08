# Davy Crocket

## Wi-Fi tracking extraordinaire

Wrote this little program to work with an arduino. The idea is to have two different wireless cards listening the RSSI (signal strength) of the same Wi-Fi Access Point (AP). Based on the RSSI of both it will send a serial signal to an arduino attached to a servo or stepper motor. The Arduino will then skew the antenna array in the direction or the best signal.

===

Using:
    Kali Linux
    Python (pyshark, numpy, serial)
    tshark
    Arduino Uno
    Microstep Driver CW230 + Stepper Motor NEMA 23 from BuildYourOwnCNC.com
# USB-Adapter automatisch starten und konfigurieren mit udev-Regeln.
Ich habe meine Systeme damit eingerichtet, weil ich 2 CAN-Adapter an einem Rechner nutze und sicher gehen will, dass die Zuordnung von Adapter auf CAN-Bus immer richtig ist. Die Vorteile der Konfiguration über udev-Regeln sind:

- Automatische Konfiguration beim Systemstart
- Automatische Konfiguration beim (erneuten) Anstecken des Gerätes im laufenden Betrieb
- Sichere Zuordnung eines Gerätes zu einem Device-Name

Eine generelle Beschreibung zu udev gibt es hier: https://wiki.ubuntuusers.de/udev/ . Für unseren Anwendungsfall funktioniert es so:

Mit `lsusb` lässt man sich die Liste der USB-Devices anzeigen. Bei mir sieht das so aus (wobei im Moment nur ein CAN2USB-Adapter angeschlossen ist wg. Timeout-Problem):

    Bus 002 Device 003: ID 8087:07da Intel Corp. Centrino Bluetooth Wireless Transceiver```
    Bus 002 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub  
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub  
    Bus 001 Device 003: ID 2232:1045 Silicon Motion WebCam SC-10HDP12631N
    Bus 001 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 004 Device 003: ID 090c:1000 Silicon Motion, Inc. - Taiwan (formerly Feiya Technology Corp.) Flash Drive
    Bus 004 Device 002: ID 05e3:0626 Genesys Logic, Inc. USB3.1 Hub
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 006: ID 0403:6015 Future Technology Devices International, Ltd Bridge(I2C/SPI/UART/FIFO)
    Bus 003 Device 004: ID 0bda:0129 Realtek Semiconductor Corp. RTS5129 Card Reader Controller
    Bus 003 Device 008: ID 1d50:606f OpenMoko, Inc. Geschwister Schneider CAN adapter
    Bus 003 Device 003: ID 05e3:0610 Genesys Logic, Inc. Hub
    Bus 003 Device 002: ID 1a86:7523 QinHeng Electronics CH340 serial converter
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

Nun kann man die Seriennummer des CAN-Adapter anzeigen. Man sucht den passenden Eintrag, hier `Bus 003 Device 008` und fragt die Seriennummer ab mit `lsusb -vs 003:008` (evtl. ein `sudo` voran stellen). Es folgt eine längliche Ausgabe. Relevant ist der Eintrag

    iSerial                 3 002600495631511820373756

Nun legt man eine Datei mycanbus.rules an mit
    sudo nano /etc/udev/rules.d/mycanbus.rules

und trägt folgendes ein (natürlich die Seriennummer verwenden, die man selbst ermittelt hat):

    # USB2CAN-Adapter fuer VitoCal sicher konfigurieren
    # Externer CAN ist am linken Adapter (gruene Punkte) angeschlossen:
    SUBSYSTEMS=="usb", ATTRS{serial}=="002600495631511820373756", NAME="canexternal", ACTION=="add", RUN+="/usr/local/bin/can_startup_external.sh"

`NAME` und Kommentare auch an die eigenen Bedürfnisse anpassen. Falls man nur einen Adapter hat, empfehle ich `NAME="can0"` zu nehmen, dann muss man sich nicht umgewöhnen.

Jetzt legt man noch die Datei `/usr/local/bin/can_startup_external.sh` an mit

    sudo nano /usr/local/bin/can_startup_external.sh

und fügt folgendes ein:

    #!/bin/sh
    sudo ip link set canexternal type can bitrate 250000 && sudo ifconfig canexternal up

und macht die Datei ausführbar.

Der Name `(canexternal)` muss natürlich gleich sein, wie der oben festgelegte.

Fertig. Die evtl. bisher konfigurierte CAN-Initialisierung sollte man nun abschalten.
Jetzt einmal den Rechner neu starten und der CAN-Adapter sollte automatisch konfiguriert werden.

Funktioniert bei mir unter Raspi Buster und Ubuntu 22.04TLS.
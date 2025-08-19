#include <SPI.h>
#include <LoRa.h>

void setup() {
  SerialUSB.begin(9600);
  while (!SerialUSB);

  LoRa.setPins(8, 4, 3); // NSS, RESET, DIO0 – adjust to your wiring

  if (!LoRa.begin(915E6)) {
    SerialUSB.println("LoRa init failed!");
    while (1);
  }
  SerialUSB.println("LoRa Receiver");
}

void loop() {
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    SerialUSB.print("Received: ");
    while (LoRa.available()) {
      SerialUSB.print((char)LoRa.read());
    }
    SerialUSB.println("not received");
  }
  delay(100);
}


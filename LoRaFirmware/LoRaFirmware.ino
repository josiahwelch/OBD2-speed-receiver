#include <SPI.h>
#include <LoRa.h>

void setup() {
  Serial.begin(9600);
  while (!Serial);

  LoRa.setPins(8, 4, 3); // NSS, RESET, DIO0 – adjust to your wiring

  if (!LoRa.begin(915E6)) {
    Serial.println("LoRa init failed!");
    while (1);
  }
  Serial.println("LoRa Receiver");
}

void loop() {
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    Serial.print("Received: ");
    while (LoRa.available()) {
      Serial.print((char)LoRa.read());
    }
    Serial.println();
  }
}


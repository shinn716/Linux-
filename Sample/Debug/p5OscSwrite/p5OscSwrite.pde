import processing.serial.*;
import oscP5.*;
import netP5.*;


Serial myPort;  
OscP5 oscP5;
NetAddress myRemoteLocation;

int port = 12000;
String address = "/data";

void setup() 
{
  size(200, 200);

  //OSC
  oscP5 = new OscP5(this, port);  

  //Serail
  for (int i=0; i<Serial.list().length; i++)
    println((i+1) + " " + Serial.list()[i]);
  try {
    String portName = Serial.list()[1];
    myPort = new Serial(this, portName, 9600);
  }
  catch(Exception e) {
  }
}

void draw(){}

void keyPressed() {
  if (key == 'q' || key == 'Q') {
    myPort.write('q');
  }
  if (key == 'w' || key == 'W') {
    myPort.write('w');
  }
  if (key == 'e' || key == 'E') {
    myPort.write('e');
  }
}

/* incoming osc message are forwarded to the oscEvent method. */
void oscEvent(OscMessage theOscMessage) {
  /* print the address pattern and the typetag of the received OscMessage */
  print("### received an osc message.");
  //println(" addrpattern: "+theOscMessage.addrPattern());
  //println(" typetag: "+theOscMessage.typetag());

  if (theOscMessage.addrPattern().equals(address)) {
    if (theOscMessage.get(0).intValue() == 0) {
      println("Serial write - q");
      myPort.write('q');
    } else if (theOscMessage.get(0).intValue() == 1) {
      println("Serial write - w");
      myPort.write('w');
    } else if (theOscMessage.get(0).intValue() == 2) {
      println("Serial write - e");
      myPort.write('e');
    }
  }
}

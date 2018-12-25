float tx = 183;
float ty = 63;

PImage bk;
PImage tile;

int framen = 1;

void setup() {
  size(100, 100, P2D);
  frame.setTitle("!float");
  frameRate(255);
  
  bk = loadImage("bk.png");
  frame.setSize(bk.width,bk.height);
  
  tile = loadImage("1.png"); 
}

void draw() { 
  if (frameCount == 1) image(bk, 0, 0);
  
  if (frameCount >= 60) {
    image(tile, tx, ty);
    
    tx = (tx + 0.5f) % bk.width;
    ty = (ty + 0.5f) % bk.height;
  }
  
  if (frameCount % 5 == 0) {
    //saveFrame(String.format("%05d.png", framen));
    framen += 1;
  }
  
  /*if (frameCount >= 3600) {
    exit();
  }*/
}
float fontSize = 14;
int spacing = 16;
PFont font;
int internalWidth, internalHeight;
PImage colours;
char[] characters = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~".toCharArray();

char rChar() {
  return characters[(int)random(characters.length)];
}

void drawCharsAt(int x, int y, char ch, float brightness) {
  if (y >= internalHeight) return;
  
  color colour = colours.pixels[y*internalWidth+x];
  if (ch == '$') {
    ch = rChar();
    brightness *= 0.3;
  }
  
  fill(hue(colour), saturation(colour), 255 * brightness);
  
  String s = ch + "";
  if (random(0, 100) < 5) s += rChar();
  
  for(char c : s.toCharArray()) {
    text(c, x*spacing, y*spacing + fontSize);
  }
}

void setup() {
  size(3840, 2160, P2D);
  colorMode(HSB, 255);
  internalWidth = width/spacing;
  internalHeight = height/spacing;
  
  colours = loadImage("arch.png");
  colours.resize(internalWidth, internalHeight);
  colours.loadPixels();
  
  background(0);
  PImage bk = loadImage("wallpaper.png");
  image(bk, 0, 0);
  
  fill(0);
  rect(2*spacing - fontSize/4.0, 0, 2*spacing, height);

  font = createFont("Hack", fontSize);
  textFont(font);
  
  String s;
  float currentBrightness = random(0.5, 1);
  s = "$With every step you take$$$$ A $$$$$$ tangent$ is left in your wake$$$$$$ And everywhere you see $$$$$Blindly, point infinitely$$$$$$$";
  for (int i = 0; i < s.length(); i++) {
    drawCharsAt(2, i, s.charAt(i), currentBrightness);
    float brightnessChange = random(0.05, 0.1);
    currentBrightness = constrain(currentBrightness + ((int)random(0, 2) == 0 ? -brightnessChange : brightnessChange), 0.5, 1);
  }

  currentBrightness = random(0.5, 1);
  s = "$$$$The $$spectrum of our time $$$$$$ Makes from its shape of a line$$$$This instance proves to be$$$$$A moment $reaching endlessly.$$$";
  for (int i = 0; i < s.length(); i++) {
    drawCharsAt(3, i, s.charAt(i), currentBrightness);
    float brightnessChange = random(0.05, 0.1);
    currentBrightness = constrain(currentBrightness + ((int)random(0, 2) == 0 ? -brightnessChange : brightnessChange), 0.5, 1);
  }
  
  saveFrame("test.png");
}
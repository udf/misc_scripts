import java.util.Collections;

float fontSize = 14;
int spacing = 16;
PFont font;
char[] characters;
int internalWidth, internalHeight;
PImage colours;
columnFaller[] fallControllers;
ArrayList<Integer> queue;
int queueIndex;
boolean firstDrawDone = false;

class columnFaller{
    private int x;
    private int y;
    private float currentBrightness;
    private String prevCharacters;
    
    private boolean falling;
    
    columnFaller(int row) {
      x = row;
      y = 0;
      falling = false;
    }
    
    boolean isFalling() {
      return falling;
    }
    
    void beginFall() {
      if (falling) return;
      
      falling = true;
      y = 0;
      prevCharacters = "";
      currentBrightness = random(0.4, 1);
    }
    
    void update() {
      if (!falling) return;
      
      if (y > 0) {
        drawCharsAt(x, y-1, prevCharacters, currentBrightness);
        float brightnessChange = random(0.1, 0.25);
        currentBrightness = constrain(currentBrightness + ((int)random(0, 2) == 0 ? -brightnessChange : brightnessChange), 0.1, 0.7);
      }

      prevCharacters = getRandomChars();
      drawCharsAt(x, y, prevCharacters, 1);
      
      if (++y > internalHeight) {
        falling = false;
      }
    }
}

void setup() {
  size(3840, 2160, P2D);
  frameRate(15);
  colorMode(HSB, 255);
  internalWidth = width/spacing;
  internalHeight = height/spacing;
  
  characters = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~".toCharArray();
  colours = loadImage("arch.png");
  colours.resize(internalWidth, internalHeight);
  colours.loadPixels();
  
  font = createFont("Hack", fontSize);
  textFont(font);
  
  background(0);
  
  fallControllers = new columnFaller[internalWidth];
  queue = new ArrayList<Integer>(); queueIndex = 0;
  for (int x = 0; x < internalWidth; x++) {
    fallControllers[x] = new columnFaller(x);
    queue.add(x);
  }
  Collections.shuffle(queue);
}

void draw() {
  if (random(0, 100) < 70) {
    fallControllers[queue.get(queueIndex++)].beginFall();
    if (queueIndex >= queue.size()) {
      Collections.shuffle(queue);
      queueIndex = 0;
      firstDrawDone = true;
    }
  }
  
  for(columnFaller o : fallControllers) {
    o.update();
  }
  
  if (firstDrawDone) {
    drawCharsAt((int)random(0, internalWidth+1), (int)random(0, internalHeight+1), getRandomChars(), random(0.1, 0.8));
  }
}

String getRandomChars() {
  String s = characters[(int)random(characters.length)] + "";
  if (random(0, 100) < 30) {
    s += characters[(int)random(characters.length)];
  }
  return s;
}

void drawCharsAt(int x, int y, String chars, float brightness) {
  if (y >= internalHeight) return;
  fill(0);
  rect(x*spacing, y*spacing, spacing, spacing);
  
  color colour = colours.pixels[y*internalWidth+x];
  fill(hue(colour), saturation(colour), 255 * brightness);
  
  for(char c : chars.toCharArray()) {
    text(c, x*spacing, y*spacing + fontSize);
  }
}
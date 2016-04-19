//Final Sktech project
//Cody Kaiser and Scott McGowan

/*
 * This function takes a file name requests it from the server to
 * get a file. From there we dump line by line(all values will be on sepereate lines) 
 * into a dataframe to be later manipulated in other functions
 */

public void get_data()
{
  String lines[] = loadStrings("list.txt");
  for (int i = 0 ; i < lines.length; i++) {
    println(lines[i]);
  } 
}

void star(float x, float y, float radius1, float radius2, int npoints) {
  float angle = TWO_PI / npoints;
  float halfAngle = angle/2.0;
  beginShape();
  for (float a = 0; a < TWO_PI; a += angle) {
    float sx = x + cos(a) * radius2;
    float sy = y + sin(a) * radius2;
    vertex(sx, sy);
    sx = x + cos(a+halfAngle) * radius1;
    sy = y + sin(a+halfAngle) * radius1;
    vertex(sx, sy);
  }
  endShape(CLOSE);
}


/*
*######################################################################################################################
*                                                                                                                     #
*  88888888ba                                                                   88                         88           #
*  88      "8b                                                                  ""                         88           #
*  88      ,8P                                                                                             88           #
*  88aaaaaa8P' 8b,dPPYba,  ,adPPYba,   ,adPPYba,  ,adPPYba, ,adPPYba, ,adPPYba, 88 8b,dPPYba,   ,adPPYb,d8 88           #
*  88""""""'   88P'   "Y8 a8"     "8a a8"     "" a8P_____88 I8[    "" I8[    "" 88 88P'   `"8a a8"    `Y88 88           #
*  88          88         8b       d8 8b         8PP"""""""  `"Y8ba,   `"Y8ba,  88 88       88 8b       88 ""           #
*  88          88         "8a,   ,a8" "8a,   ,aa "8b,   ,aa aa    ]8I aa    ]8I 88 88       88 "8a,   ,d88 aa           #
*  88          88          `"YbbdP"'   `"Ybbd8"'  `"Ybbd8"' `"YbbdP"' `"YbbdP"' 88 88       88  `"YbbdP"Y8 88           #
*                                                                                               aa,    ,88              #
*                                                                                                "Y8bbdP"               #  
*                                                                                                                     #                                                                                                                     #
*######################################################################################################################
*/

public void setup()
{
  size(1000, 1000)
  background(167)
}

public void draw()
{
  
}
float val[];
int i=0,j=0;
void setup(){
  size(1000,1000);
  val=new float[width];
  for(int i=0;i<width;i++)
  {
    val[i]=random(height);
  }
}

void draw(){
  background(0);
  if(i<val.length)
  {
    for(j=0;j<val.length-i-1;j++)
    {
      if(val[j]>val[j+1])
      {
        float temp=val[j];
        val[j]=val[j+1];
        val[j+1]=temp;
      }
    }
    i++;
  }
  else
  {
    println("Done");
    noLoop();
  }
  for(int i=0;i<val.length;i++)
  {
    stroke(255);
    line(i,height,i,height-val[i]);
  }
}

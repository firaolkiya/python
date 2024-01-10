class Robot(object):

    def __init__(self, width, height):
        print (height,width)
        self.width=width
        self.per = 2*width+2*height-4
        self.height=height
        self.x = 1
        self.y=0
        self.robot = [0,0]
    def make(self,num):
        if self.robot[0]>=self.width :
            self.y=1
            self.x=0
            self.robot[1]+=(self.robot[0]+1-self.width)*self.y
            self.robot[0]=self.width-1
        if self.robot[1]>=self.height:
            self.y=0
            self.x=-1
            self.robot[0]+=(self.robot[1]+1-self.height)*self.x
            self.robot[1]=self.height-1
        if self.robot[0]<0:
            self.y=-1
            self.x=0
            self.robot[1]+=(0-self.robot[0])*self.y
            self.robot[0]=0
        if self.robot[1]<0:
            self.y=0
            self.x=1
            self.robot[0]+=(0-self.robot[1])*self.x
            self.robot[1]=0


    def step(self, num):
        n = num%self.per
        if self.robot[0]+self.robot[1]==0 and num//self.per>0:
            self.x=0
            self.y=-1
        elif self.robot[0]==self.width-1 and self.robot[1]==0 and num//self.per>0:
            self.x=1
            self.y=0
        elif self.robot[0]==self.width-1 and self.robot[1]==self.height and num//self.per>0:
            self.x=0
            self.y=1
        elif self.robot[0]==0 and self.robot[1]==self.height and num//self.per>0:
            self.x=-1
            self.y=0
      
        self.robot[0]+=self.x*n
        self.robot[1]+=self.y*n
        while self.robot[0]<0 or self.robot[0]>=self.width or self.robot[1]<0 or self.robot[1]>=self.height:
            self.make(self,)


    def getPos(self):
        return self.robot
    def getDir(self):
        if self.x==1:
            return "East"
        elif self.x ==-1:
            return "West"
        if self.y==1:
            return "North"
        elif self.y ==-1:
            return "South"
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
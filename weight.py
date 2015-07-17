from SimpleCV import Image, Color, Display
from sworks  import Cropx, Part
from rnum import d, iHunt, db, hunt, cpause ,Gd
global db,Gd
class Scale:
    global db,Gd  
    name = 'Scale'
    def __init__(self,fname):
        self.img = Image(fname)
        if not fname == "input.png": self.img.save("input.png")
        self.cropped = Cropx(self.img)    # crop image
        self.cropped.save("cropTest.png")      # save intermediat results
        [self.wt,
         self.fat,
         self.h2o] = Part(self,self.cropped) # partition cropped image
        self.fat.save("fatTest.png")
        self.h2o.save("h2oTest.png")
        self.wt.save ("wtTest.png")
        #  hunt for the appropriate number in each partitioned image
        self.nwt =  hunt(self.wt,'wt')
        self.nfat = hunt(self.fat,'fat')
        self.nh2o = hunt(self.h2o,'h2o')
        return(None)
    
if  __name__ == '__main__':
    
    filename = "input.png"
    print 'weight.py', filename
  #  Gd  = Display((1040,410))
    db = True
    s = Scale(filename)
   
    print  s.name, 'wt is' ,s.nwt,'iHunt global'
    for i in iHunt:
        print i
    s.cropped.save(Gd)    #   test image display
    cpause(' end Scale')
    
    Gd.quit()
    
    
    

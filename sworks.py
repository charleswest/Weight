from SimpleCV import Image, Color ,Display
from rnum import cpause, Gd, db, iHunt
def Cropx( img):
    global db,Gd
    #img = self.__img
    img.save(Gd)
    print ' w x h', img.width, img.height
    if img.height == 2988:
        img = img.rotate(90)   #  all Dec set rotate
    #fi = cropSetx(img)
    
     
##    mask =   imgE.hueDistance(128.0)
##    img2  =   mask.binarize(128)
    img2 = img.hueDistance(Color.BLUE).invert()
    fi = cropSub(img2,.03, .21 )      # tolerance .03   
    if fi is None:
        print 'fi is None try  no mask'
        imgE = img.erode(2)
        fi = cropSub(imgE, .1, .21)
        if fi is None:
            print 'fi is none - try  100%'
            fi = cropSub(img2, .1, 1)
            if fi is None: raise ValueError('Cropx failed')
    
    print 'Sub blb area', fi.area(),
    print round( 100.0 * fi.area()/img.area(),2) ,'pct'
    img3 = img.crop( fi)                  # crop the original image
    angle = tstInvert(img3)    
    img3 = img3.rotate(angle,fixed=False)   # remove skew or inversion
    
    img4 = img3.resize(w=1040,h=410)
    img4.save(Gd)
    if db: cpause('cropx',Gd)
    return(img4)

def cropSub(img,t,mx):
    img.save(Gd)
    fs = img.findBlobs(minsize= .01 * img.area(),maxsize=mx * img.area())
    if isinstance(fs, list):
        print len(fs), 'blobs found'
        if len(fs) > 1: iHunt.append(('xcrop', len(fs), 0,0,0))
        for f in sorted(fs, key = lambda b:b.area(), reverse=True ):
            
            if (f.isRectangle(tolerance=t)
            and f.width() > f.height() ):    
                #print 'IS  Masked RECTANGLE ************'
                f.draw(color=Color.RED,width=5)
                img.save(Gd)
                return( f)
    #print 'cropSub croaked'        
    return None



  
    
def tstInvert(img):
  ' inverted images have a horizontal line at .3 instead of .7 '
  if db: img.save("invert.png")
  fset = img.findLines(minlinelength=100)
  fh = fset.filter(abs(fset.angle()) < 2 )    #   near horizon
  if db:
      fh.draw(color=Color.RED,width=9)
      img.save(Gd)
      if db: cpause(['tst invert fset >>',len(fset)],Gd)
  v7 =  0 ; v3 = 0
  for fx in fh:
       yh = round( fx.y / float(img.height),1 )  # % dist on y axis
       if   yh == 0.3: v3 = v3 + 1
       elif yh == 0.7: v7 = v7 + 1
       if db: print 'yh  v3  v7',  yh ,v3, v7, fx.angle()
  #print 'v3', v3, 'v7', v7
  if( v3 > v7):
      return(180)
  else:
      fmx = fh.filter( abs(fh.angle()) == max(   abs(fh.angle()  )  ))
      x = fmx.angle()[0]    # one is enough
      print ' remove skew', x
      return( x )  #  largest < 2 deg

def Part(self,imgx):
    from SimpleCV import Image, Color
    #img = self.__img
    fv1 = .67 * imgx.width    #.7
    fv2 = .5 * fv1
    fcut = .3 * fv2
    fcut2 = .95*(fv1 + fcut)
    dy = .15 * imgx.height
    fy = .67 * imgx.height
    fyc =   fy           #   cut line for h20 allow some slack
    imgx.drawLine((fcut,0),  (fcut,imgx.height),  color=Color.YELLOW,thickness=3)
    imgx.drawLine((fcut2,0), (fcut2,imgx.height), color=Color.YELLOW,thickness=3)
    imgx.drawLine(( 0,fy),    ( imgx.width, fy ) ,color=Color.YELLOW,thickness=3)
    imgx.drawLine(( 0,fyc),   ( imgx.width, fyc) ,color=Color.ORANGE,thickness=3)
    imgx.drawLine( (fv1,0), ( fv1,imgx.height),   color=Color.YELLOW,thickness=3)
    imgx.drawLine( (fv2,fy), ( fv2,imgx.height),  color=Color.YELLOW,thickness=3)
    #imgx.show()
    wt = imgx.crop( (fcut, 0), (fv1, fy) )  #  100  x 300   st at 150   asp = .33
    dy = .15 * imgx.height
    fat = imgx.crop((  fcut2, 0 ),  (imgx.width,  fy -dy  ))  # fy - dy ??
    h2o = imgx.crop((fcut,fyc), (fv2, imgx.height)  )
    return([wt,fat,h2o])

  
if  __name__ == '__main__':
    Gd  = Display((1040,410))
    db = True
    fil = "input.png"
    #fil = 'C:\\Users\\charles\\Desktop\\ScTest\\TX\\20141103_0629.JPG' 
    print 'sworks.py', fil
    img = Image(fil)
    if not fil == "input.png":  img.save("input.png")
     
    
    imt = Cropx( img)
    imt.save(Gd) 
    [wt,fat,h2o]=Part(1,imt)
    fat.save(Gd)
    cpause('fat',Gd)
    h2o.save(Gd)
    cpause('h2o',Gd)
    
    raw_input('press enter to quit')
    Gd.quit() 
    #cpause('end Scale')
    
    

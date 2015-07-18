# Weight
OCR for pictues of a Bathroom scale

Requires.  Python2 , SimpleCv --  

This is a prototype for software to read common machine information using a smartphone camera.
The jpg from the phone has accurate date and time and so all we need to do is upload pictures
to a server and parse the picture for the numbers we are interested in.

This project also serves to demonstrate instrumentation and regression testing.  The testloop.py script 
reads a txt file which contains the expected output and the file-name to process.  It verifys that the
algorithm is returning the correct numbers for each picture and keeps track of elapsed time currently 
around 5 sec/per picture.

the weight.py script analyses a single picture.

I have not included my daily script which uses the scale object in weight to update statistics that I keep in R.

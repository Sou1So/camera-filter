# Digital Imaging Final
# Ignacio Franke & Sonny Olivas
# 10/03/2022

#import libraries
import cv2
import numpy 
import os.path

#load files into program
print ("Save your original image in the same folder as this program.")
filename_valid = False 
while filename_valid == False: #loop until image file is found
    filename = input("Enter the complete image file name, including the extension, and then press 'enter': ") #enter image name
    if os.path.isfile(filename) == True: 
        configfile = input("Enter the complete config file name, including .npy, and then press 'enter': ") #enter config name
        if os.path.isfile(configfile) == True: #selected configuration file loaded into RGB values
            loadedconfig = numpy.load(configfile)
            R1 = loadedconfig[0]
            G1 = loadedconfig[1]
            B1 = loadedconfig[2]
            R2 = loadedconfig[3]
            G2 = loadedconfig[4]
            B2 = loadedconfig[5]
            R3 = loadedconfig[6]
            G3 = loadedconfig[7]
            B3 = loadedconfig[8]
            R4 = loadedconfig[9]
            G4 = loadedconfig[10]
            B4 = loadedconfig[11]
            R5 = loadedconfig[12]
            G5 = loadedconfig[13]
            B5 = loadedconfig[14]
            R6 = loadedconfig[15]
            G6 = loadedconfig[16]
            B6 = loadedconfig[17]
            grayscale_break = loadedconfig[18]
            print("Configuration found!")
        else:
            print("No such configuration file found!") #no congifuration found, set RGB to usual values
            R1 = 255
            G1 = 0
            B1 = 0
            R2 = 255
            G2 = 155
            B2 = 0
            R3 = 255
            G3 = 255
            B3 = 0
            R4 = 0
            G4 = 255
            B4 = 0
            R5 = 0
            G5 = 0
            B5 = 255
            R6 = 255
            G6 = 0
            B6 = 255
            grayscale_break = 100
        filename_valid = True
    else:
        print ("Something was wrong with that filename. Please try again.") 

#load images into variables
original_image = cv2.imread(filename, 1) 
grayscale_image_simple = cv2.imread(filename, 0) 
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR) 

#construct windows and sliders
cv2.namedWindow("Original Image")
cv2.namedWindow("Grayscale Image")
cv2.namedWindow("Customized Image")    

cv2.createTrackbar("R", "Customized Image", R1, 255, lambda X:None)
cv2.createTrackbar("G", "Customized Image", G1, 255, lambda X:None)
cv2.createTrackbar("B", "Customized Image", B1, 255, lambda X:None)

cv2.createTrackbar("GreyBreak", "Customized Image", grayscale_break, 255, lambda X:None)

cv2.createTrackbar("Color Select", "Customized Image", 1, 6, lambda X:None)

#get values for image width, height, and channels
image_height = original_image.shape[0] 
image_width = original_image.shape[1]
image_channels = original_image.shape[2]

#define constant array for image dimensions
def ARRAY_CONSTANT():
    return numpy.zeros((image_height,image_width,image_channels), numpy.uint8)



#color change detector init
selectOn = [0,0,0,0,0,0]

#set tracbars to their correct values corresponding to their colors
def quickReset(f,g,h):
    cv2.setTrackbarPos("R", "Customized Image", f)
    cv2.setTrackbarPos("G", "Customized Image" , g)
    cv2.setTrackbarPos("B", "Customized Image", h)

#establish a second variable used to detremine if the color slider has changed values
ColorSelect2 = 1

#loop until 's' or escape key pressed
keypressed = cv2.waitKey(100)
while keypressed != 27 and keypressed != ord("s"):
    #fetch trackbar position
    ColorSelect = cv2.getTrackbarPos("Color Select", "Customized Image")
    #set sliders to their correct color values one time, then update image with changes in colors made by the user
    if(ColorSelect == 1):
        if selectOn[0] == 0:
            quickReset(R1, G1, B1)
            selectOn[0] = 1
        R1 = cv2.getTrackbarPos("R", "Customized Image")
        G1 = cv2.getTrackbarPos("G", "Customized Image")
        B1 = cv2.getTrackbarPos("B", "Customized Image")
    if(ColorSelect != ColorSelect2):
        selectOn = [0,0,0,0,0,0] #set back to 0 if there is a change in the color selection

    if(ColorSelect == 2):
        if selectOn[1] == 0:
            quickReset(R2, G2, B2)
            selectOn[1] = 1
        R2 = cv2.getTrackbarPos("R", "Customized Image")
        G2 = cv2.getTrackbarPos("G", "Customized Image")
        B2 = cv2.getTrackbarPos("B", "Customized Image")
    if(ColorSelect != ColorSelect2):
        selectOn = [0,0,0,0,0,0]

    if(ColorSelect == 3):
        if selectOn[2] == 0:
            quickReset(R3, G3, B3)
            selectOn[2] = 1
        R3 = cv2.getTrackbarPos("R", "Customized Image")
        G3 = cv2.getTrackbarPos("G", "Customized Image")
        B3 = cv2.getTrackbarPos("B", "Customized Image")
    if(ColorSelect != ColorSelect2):
        selectOn = [0,0,0,0,0,0]

    if(ColorSelect == 4):
        if selectOn[3] == 0:
            quickReset(R4, G4, B4)
            selectOn[3] = 1
        R4 = cv2.getTrackbarPos("R", "Customized Image")
        G4 = cv2.getTrackbarPos("G", "Customized Image")
        B4 = cv2.getTrackbarPos("B", "Customized Image")
    if(ColorSelect != ColorSelect2):
        selectOn = [0,0,0,0,0,0]
    
    if(ColorSelect == 5):
        if selectOn [4] == 0:
            quickReset(R5, G5, B5)
            selectOn[4] = 1
        R5 = cv2.getTrackbarPos("R", "Customized Image")
        G5 = cv2.getTrackbarPos("G", "Customized Image")
        B5 = cv2.getTrackbarPos("B", "Customized Image")
    if(ColorSelect != ColorSelect2):
        selectOn = [0,0,0,0,0,0]
    
    if(ColorSelect == 6):
        if selectOn[5] == 0:
            quickReset(R6, G6, B6)
            selectOn[5] = 1
        R6 = cv2.getTrackbarPos("R", "Customized Image")
        G6 = cv2.getTrackbarPos("G", "Customized Image")
        B6 = cv2.getTrackbarPos("B", "Customized Image")
    if(ColorSelect != ColorSelect2):
        selectOn = [0,0,0,0,0,0]

    ColorSelect2 = ColorSelect #update color selection value after all if statements have been completed
    
    #set blank page to correct size
    paper_1 = ARRAY_CONSTANT()
    paper_2 = ARRAY_CONSTANT()
    paper_3 = ARRAY_CONSTANT()
    paper_4 = ARRAY_CONSTANT()
    paper_5 = ARRAY_CONSTANT()
    paper_6 = ARRAY_CONSTANT()
    #set rgb for each color to a different trackbar

    #make colored papers with proper rgb values and sizing
    paper_1[0:image_height, 0:image_width, 0:image_channels] = [B1, G1, R1]
    paper_2[0:image_height, 0:image_width, 0:image_channels] = [B2, G2, R2]
    paper_3[0:image_height, 0:image_width, 0:image_channels] = [B3, G3, R3]
    paper_4[0:image_height, 0:image_width, 0:image_channels] = [B4, G4, R4]
    paper_5[0:image_height, 0:image_width, 0:image_channels] = [B5, G5, R5]
    paper_6[0:image_height, 0:image_width, 0:image_channels] = [B6, G6, R6]

    #change cutoff values for each section of color (greyscale break)
    grayscale_break = cv2.getTrackbarPos("GreyBreak", "Customized Image") #separates light and dark parts of photo

    #change grayscale values for each color
    scale6 = (grayscale_break/6)

    min_grayscale_for_1 = [0,0,0]
    max_grayscale_for_1 = [scale6,scale6,scale6]
    min_grayscale_for_2 = [scale6+1,scale6+1,scale6+1]
    max_grayscale_for_2 = [(scale6)*2,(scale6)*2,(scale6)*2]
    min_grayscale_for_3 = [((scale6)*2)+1,((scale6)*2)+1,((scale6)*2)+1]
    max_grayscale_for_3 = [(scale6)*3,(scale6)*3,(scale6)*3]
    min_grayscale_for_4 = [((scale6)*3)+1,((scale6)*3)+1,((scale6)*3)+1]
    max_grayscale_for_4 = [(scale6)*4,(scale6)*4,(scale6)*4]
    min_grayscale_for_5 = [((scale6)*4)+1,((scale6)*4)+1,((scale6)*4)+1]
    max_grayscale_for_5 = [(scale6)*5,(scale6)*5,(scale6)*5]
    min_grayscale_for_6 = [((scale6)*5)+1,((scale6)*5)+1,((scale6)*5)+1]
    max_grayscale_for_6 = [255,255,255]

    min_grayscale_for_1 = numpy.array(min_grayscale_for_1, dtype = "uint8")
    max_grayscale_for_1 = numpy.array(max_grayscale_for_1, dtype = "uint8")
    min_grayscale_for_2 = numpy.array(min_grayscale_for_2, dtype = "uint8")
    max_grayscale_for_2 = numpy.array(max_grayscale_for_2, dtype = "uint8")
    min_grayscale_for_3 = numpy.array(min_grayscale_for_3, dtype = "uint8")
    max_grayscale_for_3 = numpy.array(max_grayscale_for_3, dtype = "uint8")
    min_grayscale_for_4 = numpy.array(min_grayscale_for_4, dtype = "uint8")
    max_grayscale_for_4 = numpy.array(max_grayscale_for_4, dtype = "uint8")
    min_grayscale_for_5 = numpy.array(min_grayscale_for_5, dtype = "uint8")
    max_grayscale_for_5 = numpy.array(max_grayscale_for_5, dtype = "uint8")
    min_grayscale_for_6 = numpy.array(min_grayscale_for_6, dtype = "uint8")
    max_grayscale_for_6 = numpy.array(max_grayscale_for_6, dtype = "uint8")

    #generate color masks
    block_all_but_color_1 = cv2.inRange(grayscale_image, min_grayscale_for_1, max_grayscale_for_1)
    block_all_but_color_2 = cv2.inRange(grayscale_image, min_grayscale_for_2, max_grayscale_for_2)
    block_all_but_color_3 = cv2.inRange(grayscale_image, min_grayscale_for_3, max_grayscale_for_3)
    block_all_but_color_4 = cv2.inRange(grayscale_image, min_grayscale_for_4, max_grayscale_for_4)
    block_all_but_color_5 = cv2.inRange(grayscale_image, min_grayscale_for_5, max_grayscale_for_5)
    block_all_but_color_6 = cv2.inRange(grayscale_image, min_grayscale_for_6, max_grayscale_for_6)

    #combine color masks with solid color pictures
    parts_of_image_1 = cv2.bitwise_or(paper_1, paper_1, mask = block_all_but_color_1)
    parts_of_image_2 = cv2.bitwise_or(paper_2, paper_2, mask = block_all_but_color_2)
    parts_of_image_3 = cv2.bitwise_or(paper_3, paper_3, mask = block_all_but_color_3)
    parts_of_image_4 = cv2.bitwise_or(paper_4, paper_4, mask = block_all_but_color_4)
    parts_of_image_5 = cv2.bitwise_or(paper_5, paper_5, mask = block_all_but_color_5)
    parts_of_image_6 = cv2.bitwise_or(paper_6, paper_6, mask = block_all_but_color_6)

    #create images
    customized_image = cv2.bitwise_or(parts_of_image_1, parts_of_image_2)
    customized_image2 = cv2.bitwise_or(customized_image, parts_of_image_3)
    customized_image3 = cv2.bitwise_or(customized_image2, parts_of_image_4)
    customized_image4 = cv2.bitwise_or(customized_image3, parts_of_image_5)
    customized_image5 = cv2.bitwise_or(customized_image4, parts_of_image_6)

    #display images
    cv2.imshow("Original Image", original_image)
    cv2.imshow("Customized Image",customized_image5)
    cv2.imshow("Grayscale Image", grayscale_image_simple)

    keypressed = cv2.waitKey(30) 
    if keypressed == 27: 
        cv2.destroyAllWindows() #press escape to close everything
    elif keypressed == ord('s'): #press 's' to save
        cv2.destroyAllWindows() 
        renamed = input('Enter Filename: ') #enter name of file you would like to save
        colorarray = numpy.array([R1,G1,B1,R2,G2,B2,R3,G3,B3,R4,G4,B4,R5,G5,B5,R6,G6,B6,grayscale_break]) #forward color configuration to array
        numpy.save(renamed + 'config', colorarray) #save array as configuration to be loaded in later
        cv2.imwrite(renamed + 'GS.jpg',grayscale_image) #save gs image
        cv2.imwrite(renamed + 'color.jpg',customized_image5) #save color images
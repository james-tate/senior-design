#-------------------------------------------------------------------------------
# Name:        Landing Zone Detection
# Purpose: This code is designed to read images and write its truth's to a .txt
#          file
#
# Author:      Josh Dowdy
#              jld563@msstate.edu
#
# Created:     04/03/2015
# Copyright:   (c) Josh 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import cv2
import numpy as np
import os
import glob
import time

start_time = time.time()

# -----------------------------------------
# RGB values in OpenCV are ordered as BGR |
# -----------------------------------------

# Set the path to the image directory
# path = r'C:\\Users\\Josh\\Documents\\Senior Design\\images\\*.jpg'

path = r'/home/pi/IPS/*.jpg'

def detectLandingZone():
    minReq = 5
    counter = 0
    truthArr = []
    resultsFile = open('IPSresults.txt','w+')

    # Loop through all images in the directory
    for imName in glob.glob(path):
        if (counter >= minReq ):
            resultsFile.write('The minimum requirements have been met, Landing now\n')
            print 'Minimum requirements have been met'
            break
        else:
            print 'Loading the image: %s'% imName.split('/')[4]
            resultsFile.write('The image being processed is %s\n' % imName.split('/')[4])
        # Load the image
            im = cv2.imread(imName)

        # Define the boundaries
            boundaries= [([0,0,128],[34,34,255])]

        # Loop over the boundaries
            print 'Getting image mask'
            for (lower,upper) in boundaries:
            # Create NumPy arrays for lower and upper boundaries
                lower = np.array(lower, dtype='uint8')
                upper = np.array(upper, dtype='uint8')

            # Find the color (red) within the specified boundaries and apply the mask
                mask = cv2.inRange(im,lower,upper)
                masked_im = cv2.bitwise_and(im,im,mask=mask)
                maxPix = np.max(masked_im[:,:,2])
                minPix = np.min(masked_im[:,:,2])

            #print 'Max for %s is %d \n Min for %s is %d' % (imName,maxPix,imName,minPix)

            # Display the image for testing purposes (will be commented out in final product)
##            cv2.imshow(imName,masked_im)
##            cv2.waitKey(0)
##            cv2.destroyAllWindows()


            # Check to see if the max pixel value is what we are looking for


                if (maxPix >= 128):
                    flag = True
                    truthArr.append(1)
                    counter = counter + 1
                    resultsFile.write('Result: %s\n\n' % flag)
                if (maxPix < 128):
                    flag = False
                    truthArr.append(0)
                    resultsFile.write('Result: %s\n\n' % flag)



    print 'Writing truths to file'
    print truthArr
    truthFile = open('detectionTruth.txt','w')
    if (counter >= minReq):
	   truthFile.write('Pass\n')
    else:
		truthFile.write('Fail\n')
#    for x in truthArr:
#        truthFile.write('%d, '%x)
#    truthFile.close()

##    truthFile = 'detectionTruth.csv'
##    with open(truthFile, "w") as csvfile:
##        writer = csv.writer(csvfile, lineterminator=',')
##        for x in truthArr:
##            writer.writerow([x])


    # Display the image for testing purposes (will be commented out in final product)
##    cv2.imshow(imName,masked_im)
##    cv2.waitKey(0)

    print 'DONE!'

def main():
    detectLandingZone()
    print '%s seconds' % (time.time() - start_time)

if __name__ == '__main__':
    main()
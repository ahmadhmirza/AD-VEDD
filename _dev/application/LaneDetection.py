import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

# return gray_scaled image
def grayscale(img): 
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Filter to select white objects
# intended for extracting lane markings
def selectWhite(img):
    converted = cv2.cvtColor(img,cv2.COLOR_RGB2HLS)
    lower = np.uint8([0,200,0])
    upper = np.uint8([255,255,255])

    #test
    lower = np.uint8([0,25,0])
    upper = np.uint8([25,250,145])
    
    white_mask = cv2.inRange(converted,lower,upper)
    return cv2.bitwise_and(img,img,mask=white_mask)

# applies gaussian filter to remove noise
def gaussian_noise(img, kernel_size=5): 
   return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

# canny edge detection
def canny(img, low_threshold=0, high_threshold=255): 
   return cv2.Canny(img, low_threshold, high_threshold)

# shows image inline
def showImageInline(img,title):
    plt.imshow(img)
    plt.title(title)
    plt.show()
    return True

def calculateSlope(x1,y1,x2,y2):
    Num = y2-y1
    Den = x2-x1
    try:
        if Num == 0:
            slope = Num/Den
            #print("Horizontal Line detected.")
            #print(slope)
            return 1
        if Den == 0:
            #print("Vertical line detected.")
            return 1
        else:
            slope = Num/Den
            return slope
    except Exception as e:
        print(str(e))
        return -1

#hough transform, draws lines on the passed image
def houghTransform(image, edges):
    rho = 2
    theta = np.pi/180
    threshold = 15
    min_line_length = 900
    max_line_gap = 20

    line_image = np.copy(image)*0 #creating a blank to draw lines on
    # skipping line_image part for now.
    line_image = np.copy(image)
    # Run Hough on edge detected image
    lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)
    usedLines = []
    try:
        # Iterate over the output "lines" and draw lines on the blank
        for line in lines:
            for x1,y1,x2,y2 in line:
                slope = calculateSlope(x1,y1,x2,y2)
                if slope == 1:
                    cv2.line(line_image,(x1,y1),(x2,y2),(0,128,0),20)
                    usedLines.append(line)
                elif slope >= -0.09 and slope <=0.09:
                    cv2.line(line_image,(x1,y1),(x2,y2),(0,128,0),20)
                    usedLines.append(line)
                else:
                    pass
                    #print("The line is neither vertical nor horizontal, slope = " + str(slope))
                    #cv2.line(line_image,(x1,y1),(x2,y2),(0,139,0),20)
        #skipping overlaying line_image over original image for now.
        #print("line coordinates:")
        counter = 0
        #Calucaling the center of the detected lane marker
        #Assumes only one lane marker
        try:
            for x1,y1,x2,y2 in usedLines[0]:
                x1_mean = x1
                y1_mean = y1
                x2_mean = x2
                y2_mean = y2
            for line in usedLines:
                #print(line)
                counter += 1
                for x1,y1,x2,y2 in line:
                    if counter ==1:
                        #print("skip")
                        pass
                    else:
                        x1_mean = x1_mean + x1
                        y1_mean = y1_mean + y1
                        x2_mean = x2_mean + x2
                        y2_mean = y2_mean + y2
            x1_mean = int(x1_mean / counter)
            y1_mean = int(y1_mean / counter)
            x2_mean = int(x2_mean / counter)
            y2_mean = int(y2_mean / counter)
            
        #print("mean")
            meanCoordinates = [x1_mean,y1_mean,x2_mean,y2_mean]
            cv2.line(line_image,(x1_mean,y1_mean),(x2_mean,y2_mean),(255,0,0),10)
        except:
            return line_image,False
        return line_image, meanCoordinates
    except  Exception as e:
        print(str(e))
        return image
    # Create a "color" binary image to combine with line image
    color_edges = np.dstack((edges, edges, edges))
    # Draw the lines on the edge image
    alpha = 0.8 
    beta = 1.0 
    combo = cv2.addWeighted(image, 0.7, line_image, 1, 1)
    return combo

def detectLanesWhite(image):
    print("LaneDetector: Starting analysis...")
    print(image.shape)
    #img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # apply white filter to extract the white lane lines
    img = selectWhite(image)   
    # apply thresholding
    ret,img = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
    #convert image to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # gaussian filter to remove noise
    img = gaussian_noise(img, 5) 
    #apply hough transform to detect the lines
    img,coordinates = houghTransform(image,img)
    #print(coordinates)
    #print("LaneDetector: Analysis complete.")
    return img,coordinates
    
def main():
    img_path = "/home/ahmad/Desktop/test_1_3.jpg"
    img_path = [
        "/home/ahmad/Desktop/test_images/test_1_1.jpg",
        "/home/ahmad/Desktop/test_images/test_1_2.jpg",
        "/home/ahmad/Desktop/test_images/test_1_3.jpg",
        "/home/ahmad/Desktop/test_images/test_2_1.jpg",
        "/home/ahmad/Desktop/test_images/test_2_2.jpg",
        "/home/ahmad/Desktop/test_images/test_2_3.jpg",
        "/home/ahmad/Desktop/test_images/test_3_1.jpg",
        "/home/ahmad/Desktop/test_images/test_3_2.jpg",
        "/home/ahmad/Desktop/test_images/test_3_3.jpg",
        "/home/ahmad/Desktop/test_images/test_4_1.jpg",
        "/home/ahmad/Desktop/test_images/test_4_2.jpg",
        "/home/ahmad/Desktop/test_images/test_4_3.jpg",
        "/home/ahmad/Desktop/test_images/test_5_1.jpg",
        "/home/ahmad/Desktop/test_images/test_5_2.jpg",
        "/home/ahmad/Desktop/test_images/test_5_3.jpg"]
    for imgPath in img_path:
        # Read in the image
        image = cv2.imread(imgPath)
        image = gaussian_noise(image, 5) 
        img = detectLanesWhite(image)
        showImageInline(img,"results")

    
    
# =============================================================================
#     # apply white filter to extract the white lane lines
#     img_whiteFilter = selectWhite(image)
#     img_canny = canny(img_whiteFilter)
#     ret,img_thresh = cv2.threshold(image,150,255,cv2.THRESH_BINARY)
#     img_thresh = cv2.cvtColor(img_thresh, cv2.COLOR_BGR2GRAY)
#     # gaussian filter to remove noise
#     img = gaussian_noise(img_thresh, 5)
#     img = houghTransform(image,img)
#     # show image in-line
#     showImageInline(img,"Result")
#     print("Done")
if __name__ == "__main__":
    main()
# =============================================================================
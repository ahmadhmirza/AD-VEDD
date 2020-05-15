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

#hough transform, draws lines on the passed image
def houghTransform(image, edges):
    rho = 2
    theta = np.pi/180
    threshold = 15
    min_line_length = 800
    max_line_gap = 20

    line_image = np.copy(image)*0 #creating a blank to draw lines on

    # Run Hough on edge detected image
    lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)
    
    try:
        # Iterate over the output "lines" and draw lines on the blank
        for line in lines:
            for x1,y1,x2,y2 in line:
                cv2.line(line_image,(x1,y1),(x2,y2),(0,128,0),20)
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
    print(image.shape)
    #img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # apply white filter to extract the white lane lines
    img = selectWhite(image)   
    # apply thresholding
    ret,img = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
    #convert image to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # gaussian filter to remove noise
    img = gaussian_noise(img, 5) 
    #apply hough transform to detect the lines
    img = houghTransform(image,img)
    return img
    
def main():
    img_path = "/home/ahmad/Desktop/test_images/test_4_2.jpg"
    outimg_path = "/home/ahmad/Desktop/out.JPG"
    
    # Read in the image
    image = cv2.imread(img_path)
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
#if __name__ == "__main__":
#    main()
# =============================================================================
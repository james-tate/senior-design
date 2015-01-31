import cv2, math
import numpy as np

class ColorTracker:
  def __init__(self):
    # Capture frame from the device
    cv2.namedWindow("ColourTrackerWindow", cv2.CV_WINDOW_AUTOSIZE)
    self.capture = cv2.VideoCapture(0)
    self.scale_down = 4

  def run(self):
    while True:
      f, orig_img = self.capture.read()

      # flip the frame to reflect a virtual image
      orig_img = cv2.flip(orig_img, 1)

      # Blur the frame
      img = cv2.GaussianBlur(orig_img, (5,5), 0)

      # convert the frame from BGR to HSV
      img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2HSV)

      # scale down to reduce processing time
      img = cv2.resize(img, (len(orig_img[0]) / self.scale_down, len(orig_img) / self.scale_down))

      # get the lower and upper red color bounds -> need to possibly change
      red_lower = np.array([0, 150, 0],np.uint8)
      red_upper = np.array([5, 255, 255],np.uint8)

      # sees if values are in the range of the upper and lower bounds (1,0)
      red_binary = cv2.inRange(img, red_lower, red_upper)

      # creates 15x15 array of ones
      dilation = np.ones((15, 15), "uint8")

      # find the red contours
      red_binary = cv2.dilate(red_binary, dilation)
      contours, hierarchy = cv2.findContours(red_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
      max_area = 0
      largest_contour = None

      for idx, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > max_area:
          max_area = area
          largest_contour = contour

      if not largest_contour == None:
        moment = cv2.moments(largest_contour)

        if moment["m00"] > 1000 / self.scale_down:
          rect = cv2.minAreaRect(largest_contour)
          rect = ((rect[0][0] * self.scale_down, rect[0][1] * self.scale_down), (rect[1][0] * self.scale_down, rect[1][1] * self.scale_down), rect[2])
          box = cv2.cv.BoxPoints(rect)
          box = np.int0(box)
          cv2.drawContours(orig_img,[box], 0, (0, 0, 255), 2)
          cv2.imshow("ColourTrackerWindow", orig_img)
          if cv2.waitKey(20) == 27:
            cv2.destroyWindow("ColourTrackerWindow")
            self.capture.release()
            break

if __name__ == "__main__":
  colour_tracker = ColorTracker()
  colour_tracker.run()

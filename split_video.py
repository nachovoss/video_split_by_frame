
import cv2



# Set a destination path
destination_path = ""

# from video file:
video_path = ""
cap = cv2.VideoCapture(video_path)

# from webcam: uncomment line below
# cap = cv2.VideoCapture(0)

total_number_of_frames = 300

frame_index = 0
if cap.isOpened():
    for i in range(total_number_of_frames):
        ret, video = cap.read()
        if ret:
            name = str(frame_index) + '.jpg'
            cv2.imwrite(destination_path + name, video)
            cv2.imshow("your video", video)
            frame_index += 1

            # Press enter to quit
            if cv2.waitKey(10) == 13:
                break


cap.release()
cv2.destroyAllWindows()

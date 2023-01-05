
import cv2
import argparse


parser = argparse.ArgumentParser(description='Split video into frames')

parser.add_argument('-vp', '--video_path',  type=str, help='<Required> Path to the video file', required=True)
parser.add_argument('-bn', '--base_name', default="", type=str, help='Base name of the frames (e.g. frame_')
parser.add_argument('-sp', '--save_path', default="", type=str, help='Path to the save frames')
parser.add_argument('-nf', '--number_of_frames', default=300, type=int, help='Max amount of frames to be extracted from webcam')
parser.add_argument('-f', '--image_format', default=".jpg", type=str, help='output image format (jpg, png, etc.')
parser.add_argument('-s' , '--source', default="file", type=str, help='source of the video ("file" or "webcam" )')
parser.add_argument('-ixs', '--imgs_x_second', default=1, nargs='*', type=str, help='frames to be extracted from all frames in one second (e.g. 1 , 7, 28)')
args = parser.parse_args()

# from video file:
video_path = args.video_path
# Set a destination path
destination_path = args.save_path

if args.source == "file":
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_number_of_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) * -1 if cap.get(cv2.CAP_PROP_FRAME_COUNT) < 0 else int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
else:
    cap = cv2.VideoCapture(0)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_number_of_frames= args.number_of_frames

if float(args.imgs_x_second[0]) < 1:
    fps = int(fps / float(args.imgs_x_second[0]))
    args.imgs_x_second = "1"

frame_index = 0
fps_loop = 0

if cap.isOpened():
    for i in range(total_number_of_frames):
        ret, video = cap.read()
        frame_index += 1
        fps_loop = 1 if fps_loop == fps else fps_loop + 1
        if ret and str(fps_loop) in args.imgs_x_second:
            name = args.base_name + str(frame_index) + args.image_format
            cv2.imwrite(destination_path + name, video)
            cv2.imshow(name, video)
            
            # Press enter to quit"
            if cv2.waitKey(10) == 13:
                break
            if frame_index + 1  == int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) * -1:
                break

cap.release()
cv2.destroyAllWindows()

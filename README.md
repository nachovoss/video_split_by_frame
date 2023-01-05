# Video split by frame
## A fast an easy way to split a video by frames

### To use run the following commands:
    - pip install -r requirements.txt
    - python split_video.py
    
    - press Enter to exit

## ARGS:
usage: split_video.py [-h] -vp VIDEO_PATH [-bn BASE_NAME] [-sp SAVE_PATH] [-nf NUMBER_OF_FRAMES] [-f IMAGE_FORMAT]
                      [-s SOURCE] [-ixs [IMGS_X_SECOND [IMGS_X_SECOND ...]]]

Split video into frames

optional arguments:
  -h, --help            show this help message and exit
  -vp VIDEO_PATH, --video_path VIDEO_PATH
                        <Required> Path to the video file
  -bn BASE_NAME, --base_name BASE_NAME
                        Base name of the frames (e.g. frame_
  -sp SAVE_PATH, --save_path SAVE_PATH
                        Path to the save frames
  -nf NUMBER_OF_FRAMES, --number_of_frames NUMBER_OF_FRAMES
                        Max amount of frames to be extracted from webcam
  -f IMAGE_FORMAT, --image_format IMAGE_FORMAT
                        output image format (jpg, png, etc.
  -s SOURCE, --source SOURCE
                        source of the video ("file" or "webcam" )
  -ixs [IMGS_X_SECOND [IMGS_X_SECOND ...]], --imgs_x_second [IMGS_X_SECOND [IMGS_X_SECOND ...]]
                        frames to be extracted from all frames in one second (e.g. 1 , 7, 28)
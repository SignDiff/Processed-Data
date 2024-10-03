For training SignDiff using ControlNet, we need to obtain "train_poseimg" and "train_img" files, as well as a json file containing file names and prompt information for each image.

## Step for train_poseimg

The number of train_poseimg comes from the separation of OpenPose visualized black videos. The number of frames you separate should correspond to the number of json files for the corresponding how2sign video clip. The existence of json files is the basis for us to determine whether OpenPose visualized skeleton images exist.

1. Sort according to the "SENTENCE_NAME" in the fourth column of the csv, use renameDir(order) to rename the json folder, which facilitates counting, and then separate the visualized black background pose videos in order.

2. According to the number of json files in the json folder, separate the same number of frames from the black background pose video.

## Step for train_img

train_img comes from the images after separating video frames from the corresponding how2sign video clips (24 frames per second, 24 images)

3. First use renameMP4(order) to rename the video, which sorts according to the "SENTENCE_NAME" in the fourth column of the csv

4. Then use split_video_frame(unorder).py to separate video frames

## Step for prompt.json

5. Use extract_json.py to extract the json file needed for ControlNet
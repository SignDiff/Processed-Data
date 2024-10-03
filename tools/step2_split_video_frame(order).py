import os
import subprocess
import datetime
import shutil

def separate_video_into_images(video, folder_name, y):
    '''
    Separate a given video into a specified number of images and save them to the specified folder

    Args:
    video: Video file name
    folder_name: Name of the folder where the separated images are saved
    y: Total number of pictures to be separated into

    Returns:
    None
    '''
    # Gets the duration of each incoming video
    duration_output = subprocess.check_output(
        f"ffprobe -i train_img/{video} -show_entries format=duration -v quiet -of csv=\"p=0\"",
        shell=True)
    duration_seconds = float(duration_output)
    video_time = str(datetime.timedelta(seconds=duration_seconds))

    # Use FFmpeg to separate the video into multiple images and save them to a folder named after the video
    cmd = f"ffmpeg -i train_img/{video} -ss 00:00:00 -t {video_time} -frames:v {y} train_img/{folder_name}/image_%05d.jpg"
    subprocess.call(cmd, shell=True)

    # Wait for the cmd command to complete
    subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()

    folder_1 = os.path.join('./train_img/', folder_name)  # Delete folder 1
    folder_2 = os.path.join('./train_openpose/', folder_name)  # Delete folder 2

    # Get the number of images
    img_count = len(os.listdir(os.path.join('./train_img/', folder_name)))
    # Exclude non-compliant folders
    if y != img_count:
        # Delete image folders
        print(f"openpose folder1 is {folder_1} and num is {img_count}")
        print(f"openpose folder2 is {folder_2} and num is {y}")
        if os.path.exists(folder_1):
            [os.remove(os.path.join(folder_1, f)) for f in os.listdir(folder_1)]
            os.rmdir(folder_1)
            print('')
        if os.path.exists(folder_2):
            [os.remove(os.path.join(folder_2, f)) for f in os.listdir(folder_2)]
            os.rmdir(folder_2)
        print(f"Deleted {folder_1} and {folder_2} because the number of files in the two folders are not equal.")


def main():
    # Part A: Record the number of JSON files in each folder
    folder_num = 10000  # Maximum total number of folders, 10,000 for dev set, 100,000 for training set
    file_count_arr = [0] * folder_num  # Initialize array to 0
    print('Main function running')
    for i in range(folder_num):
        folder_name = str(i + 1).zfill(6)  # Convert number to six digits, e.g., 1 -> '000001'
        folder_path = os.path.join('./train_openpose/', folder_name)
        if not os.path.exists(folder_path):  # Skip if folder doesn't exist
            continue
        file_count = len(os.listdir(folder_path))  # Get the number of files in the folder
        file_count_arr[i] = file_count  # Add the file count to the array
    print(file_count_arr)

    # Part B: Separate video frames, and ensure the number of video frames equals the number of JSON files
    # Get all video files in the current directory
    dir_path = os.path.dirname(os.path.abspath(__file__))
    # Get all image files in the train_img directory
    videos = [f for f in os.listdir(os.path.join(dir_path, 'train_img')) if
              os.path.isfile(os.path.join(dir_path, 'train_img', f)) and f.endswith('.mp4')]
    # Iterate through each video file
    for i, video in enumerate(videos):
        # Create a folder named after the current video
        folder_name = os.path.splitext(video)[0]
        os.makedirs('train_img/'+folder_name, exist_ok=True)
        print(video, folder_name)
        if file_count_arr[i]==0:
            i=i+1
        separate_video_into_images(video, folder_name, file_count_arr[i])

if __name__ == '__main__':
    main()

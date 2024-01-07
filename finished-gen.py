import cv2
import os
import numpy as np

# Configuration
input_folder_path = 'INPUT_FOLDER_PATH/input'
output_video_path = 'OUTPUT_FOLDER_PATH/OUTPUT_VIDEO_NAME.mp4'

framerate = 24

fade_duration = 12

width = 1280
height = 720

resolution = (width, height)

# Image Functions
def show_counter(text, duration, out):
    text = str(text)
    blue_image = np.zeros((height, width, 3), dtype=np.uint8)
    blue_image[:] = (255, 142, 0)

    font = cv2.FONT_HERSHEY_COMPLEX
    text_size = cv2.getTextSize(text, font, 3, 5)[0]
    text_x = int((width - text_size[0]) / 2)
    text_y = int((height + text_size[1]) / 2)

    cv2.putText(blue_image, text, (text_x, text_y), font, 3, (0, 0, 0), 5, cv2.LINE_AA)
    cv2.putText(blue_image, text, (text_x+5, text_y-5), font, 3, (255, 255, 255), 5, cv2.LINE_AA)
    
    for i in range(fade_duration):
        alpha = i / fade_duration
        frame = cv2.addWeighted(blue_image, alpha, np.zeros_like(blue_image), 0, 0)
        out.write(frame)

    frame_count = 0
    while frame_count < duration:
        cv2.putText(blue_image, text, (text_x, text_y), font, 3, (0, 0, 0), 5, cv2.LINE_AA)
        cv2.putText(blue_image, text, (text_x+5, text_y-5), font, 3, (255, 255, 255), 5, cv2.LINE_AA)
        out.write(blue_image)
        frame_count += 1

    for i in range(fade_duration):
        alpha = i / fade_duration
        frame = cv2.addWeighted(blue_image, 1 - alpha, np.zeros_like(blue_image), 0, 0)
        out.write(frame)



def show_image(image_path, duration, out):
    global fade_duration
    
    img = cv2.imread(image_path)
    img = cv2.resize(img, resolution)

    for i in range(fade_duration):
        alpha = i / fade_duration
        frame = cv2.addWeighted(img, alpha, np.zeros_like(img), 0, 0)
        out.write(frame)

    frame_count = 0
    while frame_count < duration:
        out.write(img)
        frame_count += 1
        
    for i in range(fade_duration):
        alpha = i / fade_duration
        frame = cv2.addWeighted(img, 1 - alpha, np.zeros_like(img), 0, 0)
        out.write(frame)

def intro(text, duration, out):
    global fade_duration

    blue_image = np.zeros((height, width, 3), dtype=np.uint8)
    blue_image[:] = (255, 142, 0)

    font = cv2.FONT_HERSHEY_COMPLEX
    text_size = cv2.getTextSize(text, font, 3, 5)[0]
    text_x = int((width - text_size[0]) / 2)
    text_y = int((height + text_size[1]) / 2)
    
    cv2.putText(blue_image, text, (text_x, text_y), font, 3, (0, 0, 0), 5, cv2.LINE_AA)
    cv2.putText(blue_image, text, (text_x+5, text_y-5), font, 3, (255, 255, 255), 5, cv2.LINE_AA)
    
    for i in range(fade_duration):
        alpha = i / fade_duration
        frame = cv2.addWeighted(blue_image, alpha, np.zeros_like(blue_image), 0, 0)
        out.write(frame)

    frame_count = 0
    while frame_count < duration:
        cv2.putText(blue_image, text, (text_x, text_y), font, 3, (0, 0, 0), 5, cv2.LINE_AA)
        cv2.putText(blue_image, text, (text_x+5, text_y-5), font, 3, (255, 255, 255), 5, cv2.LINE_AA)
        out.write(blue_image)
        frame_count += 1

    for i in range(fade_duration):
        alpha = i / fade_duration
        frame = cv2.addWeighted(blue_image, 1 - alpha, np.zeros_like(blue_image), 0, 0)
        out.write(frame)

def outro(text, duration, out):
    global fade_duration

    blue_image = np.zeros((height, width, 3), dtype=np.uint8)
    blue_image[:] = (255, 142, 0)

    font = cv2.FONT_HERSHEY_COMPLEX
    text_size = cv2.getTextSize(text, font, 3, 5)[0]
    text_x = int((width - text_size[0]) / 2)
    text_y = int((height + text_size[1]) / 2)

    cv2.putText(blue_image, text, (text_x, text_y), font, 3, (0, 0, 0), 5, cv2.LINE_AA)
    cv2.putText(blue_image, text, (text_x+5, text_y-5), font, 3, (255, 255, 255), 5, cv2.LINE_AA)
    
    for i in range(fade_duration):
        alpha = i / fade_duration
        frame = cv2.addWeighted(blue_image, alpha, np.zeros_like(blue_image), 0, 0)
        out.write(frame)

    frame_count = 0
    while frame_count < duration:
        cv2.putText(blue_image, text, (text_x, text_y), font, 3, (0, 0, 0), 5, cv2.LINE_AA)
        cv2.putText(blue_image, text, (text_x+5, text_y-5), font, 3, (255, 255, 255), 5, cv2.LINE_AA)
        out.write(blue_image)
        frame_count += 1

    for i in range(fade_duration):
        alpha = i / fade_duration
        frame = cv2.addWeighted(blue_image, 1 - alpha, np.zeros_like(blue_image), 0, 0)
        out.write(frame)

# Video Generation
def generate_video():
    global input_folder_path
    global output_video_path
    global resolution
    global framerate

    count = sum(1 for file in os.listdir(input_folder_path) if os.path.isfile(os.path.join(input_folder_path, file)))

    image_files = sorted(os.listdir(input_folder_path))  # Define image_files within generate_video()

    if os.path.exists(output_video_path):
        file_name, file_extension = os.path.splitext(output_video_path)
        index = 1
        while os.path.exists(f"{file_name}_{index}{file_extension}"):
            index += 1
        output_video_path = f"{file_name}_{index}{file_extension}"

    out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), framerate, resolution)

    # Read the first and last frames to use in fade_in and fade_out
    first_frame_path = os.path.join(input_folder_path, image_files[0])
    last_frame_path = os.path.join(input_folder_path, image_files[-1])
    initial_frame = cv2.resize(cv2.imread(first_frame_path), resolution)
    final_frame = cv2.resize(cv2.imread(last_frame_path), resolution)

    intro(f"Top {count} ______", 72, out)
    
    for image_file in image_files:
        show_counter(f"Number {count}", 24, out)
        image_path = os.path.join(input_folder_path, image_file)
        show_image(image_path, 24, out)
        count -= 1
    
    outro("Thanks for Watching!", 72, out)
    
    out.release()
    print("Video Successfully Generated")

# Generate the Video
generate_video()
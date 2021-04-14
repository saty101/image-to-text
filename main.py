import cv2
import pytesseract
import os
import subprocess
from sys import argv
from annotate import get_string
import matplotlib.pyplot as plt
if __name__ == "__main__":
    # if len(argv)<2:
    #     print("Usage: python image-to-text.py relative-filepath")
    # else:
    #     print("---Start recognize text from vide ---")
    video_name = "news.mp4"
    video_path = f"{video_name}"
    VIDEO_CODEC = "MP4V"
    video_name = os.path.basename(video_path)
    vidcap = cv2.VideoCapture(video_path)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    width = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    output_path = "labeled_" + video_name
    tmp_output_path = "tmp_" + output_path
    output_video = cv2.VideoWriter(tmp_output_path, cv2.VideoWriter_fourcc(*VIDEO_CODEC), fps, (width, height))
    # Sanity check

    print("Sanity check\n",fps, height, width, "\n\n")
    frame = 0
    annotations = []
    while True:
        it_worked, img = vidcap.read()
        if not it_worked:
            break
        frame += 1
        img_name = f"{video_name}_frame{frame}"
        text = get_string(img)
        
        cv2.putText(img, text, (10,300), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,255), thickness=1)
        d = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
        n_boxes = len(d["level"])
        for i in range(n_boxes):
            if int(d["conf"][i])>0:
                (x, y, w, h) = (d["left"][i], d["top"][i], d["width"][i], d["height"][i])
                cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 255), 2)
                annotations.append(text)
    #         color = (0,255,0)
    #         cv2.putText(img, text, (x,y), (x+w, y+h), cv2.FONT_HERSHEY_SIMPLEX, color, 2)
    #     cv2.imshow(img)
        output_video.write(img)
    output_video.release()
    if os.path.exists(output_path):
        os.remove(output_path)
    subprocess.run(["ffmpeg", "-i", tmp_output_path, "-crf", "18", "-preset", "fast", "-vcodec", "libx264", output_path])
    os.remove(tmp_output_path)

    # Saving the annotations to a file
    with oepn("annotations.txt", "w") as output:
        output.write(str(annotations))
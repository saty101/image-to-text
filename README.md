# image-to-text

### Video -> Text extraction

Extracting text from video with pytesseract.

First clone the repository.

```
git clone https://github.com/saty101/image-to-text.git
cd image-to-text/
pip install -r requirements.txt
```

If you encounter file note found as below:

`FileNotFoundError: [Errno 2] No such file or directory: 'tesseract'`

Run the following command - 

`apt install tesseract`

---

You can download a youtube video using the `youtube_video.py` and change the link to your desired video.

`python youtube_video.py`

Since we mainly work with news videos/videos with text embedded in it, it will be saved as news.mp4 in the same directory.
The mp4 file is downloaded in the same directory.

---

For annotating the videos, run

`python main.py`

This will create a labeled_news.mp4 along with annotations.txt where you can find the annotated video along with a file of captions produced in the video.


You can also find the [kaggle notebook](https://www.kaggle.com/saty101/image-text) where you can find the code with embedded videos(along with the results)

The full workflow code is in this [notebook](https://github.com/saty101/image-to-text/blob/main/full_workflow.ipynb) which shows how annotations with one image and then creating the whole vide0 but the videos are not visible in the jupyter notebook.
Colab notebook link of the same notebook - [link](https://colab.research.google.com/github/saty101/image-to-text/blob/main/full_workflow.ipynb)

Simply change the `link = <desired link>` to annotate the video you want to.

[Colab noteboook](https://colab.research.google.com/github/saty101/image-to-text/blob/main/final_workflow.ipynb) but the videos can only be downloaded as embedded videos in colab crash and cause the runtime to start again.


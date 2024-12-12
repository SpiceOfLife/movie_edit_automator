# Movie Processing Scripts

This repository contains two Python scripts. These scripts can be used to generate videos from audio files and split videos into smaller segments.

## Overview

1. **movie_gen.py**  
   This script processes audio files and generates videos with black backgrounds, synchronizing the audio with the video, and saves them in MP4 format.

2. **split_video.py**  
   This script splits a video into smaller segments based on a specified duration and applies fade-in and fade-out effects to each segment. Each segment is saved into its own subfolder.

---

## 1. `movie_gen.py` - Generate Videos from Audio

### Overview

`movie_gen.py` processes audio files (in .mp3, .wav, .m4a formats) from a specified folder, generates a video with a black background, synchronizes the audio, and saves the video in MP4 format. The generated videos are saved in the specified output folder.

### Required Libraries

- `moviepy`: For video editing.

### Usage

1. Set the `base_folder` variable in the script to the directory where the audio files are stored.
2. The script processes audio files in the `audio` folder and saves the corresponding videos in the `video` folder.
3. When run, the script generates a video file for each audio file.

#### Code Example

```python
base_folder = "/path/to/your/folder"
audio_folder = os.path.join(base_folder, "audio")
video_folder = os.path.join(base_folder, "video")

# Video generation process

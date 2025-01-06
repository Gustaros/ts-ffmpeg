# ts-ffmpeg

To create a new video using FFmpeg that consists of the original video followed by its reversed version, while also cutting off the last frame, you can use the following command:

```bash
ffmpeg -i input.mp4 -vf "trim=end=1,reverse" -af "areverse" -preset ultrafast -c:v libx264 -c:a aac output.mp4
```

### Explanation of the Command:

1. **Input File**: `-i input.mp4` specifies the input video file.
2. **Video Filter**: 
   - `-vf "trim=end=1,reverse"`:
     - `trim=end=1` cuts the video to remove the last frame (you can adjust the time as needed).
     - `reverse` reverses the trimmed video.
3. **Audio Filter**: `-af "areverse"` reverses the audio of the trimmed video.
4. **Encoding Options**:
   - `-preset ultrafast` speeds up the encoding process.
   - `-c:v libx264` specifies the video codec for output.
   - `-c:a aac` specifies the audio codec for output.
5. **Output File**: `output.mp4` is the name of the resulting video file.

### Complete Process
To concatenate both the original and reversed videos into one file, you can use:

```bash
ffmpeg -i input.mp4 -vf "reverse" reversed.mp4
ffmpeg -i input.mp4 -i reversed.mp4 -filter_complex "[0:v][1:v]concat=n=2:v=1:a=0" final_output.mp4
```

### Explanation of Concatenation:
1. The first command creates a reversed version of your input video.
2. The second command concatenates the original and reversed videos:
   - `[0:v][1:v]concat=n=2:v=1:a=0` specifies that we are concatenating two video streams without audio.

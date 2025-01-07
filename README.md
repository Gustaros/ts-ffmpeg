# ts-ffmpeg

```bash
ffmpeg -i input.mp4 -filter_complex "[0:v]split[v0][v1];[v1]reverse[v1r];[v1r]trim=start_frame=1[v1r_cut];[v0][v1r_cut]concat=n=2:v=1:a=0[v]" -map "[v]" -c:v libx264 output.mp4
```

Explanation:
• In this command, everything is kept on a single line (without shell line-break backslashes) so FFmpeg won’t treat '\' as part of the filter.  
• [0:v]split[v0][v1] splits the video stream into two outputs.  
• [v1]reverse[v1r] reverses the second split.  
• [v1r]trim=start_frame=1[v1r_cut] removes the first frame of the reversed stream (which corresponds to the last frame of the original).  
• [v0][v1r_cut]concat=n=2:v=1:a=0[v] concatenates the original ([v0]) and trimmed reversed ([v1r_cut]) segments.  
• -map "[v]" selects only the processed video.  
• -c:v libx264 ensures encoding with H.264.


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

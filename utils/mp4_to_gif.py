from moviepy.editor import VideoFileClip
import os


def convert_mp4_to_gif(input_path, output_path, start_time=0, duration=None, resize_factor=0.8):
    try:
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")

        clip = VideoFileClip(input_path)

        if duration is not None:
            clip = clip.subclip(start_time, min(start_time + duration, clip.duration))
        elif start_time > 0:
            clip = clip.subclip(start_time)

        if resize_factor != 1:
            clip = clip.resize(resize_factor)

        clip.write_gif(output_path, fps=15, colors=256, program='ffmpeg')

        print(f"GIF created successfully: {output_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        if 'clip' in locals():
            clip.close()


# Example usage
input_video = "Input Path"
output_gif = "Output Path"

convert_mp4_to_gif(input_video, output_gif, start_time=0, resize_factor=1)

# https://cloudconvert.com/mp4-to-gif

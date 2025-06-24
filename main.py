from utils import (read_video,save_video)
from trackers import PlayerTracker

def main():
    input_video_path="input_videos/input_video.mp4"
    video_frames = read_video(input_video_path)

    player_tracker = PlayerTracker(model_path='yolov8x')
    player_detections=player_tracker.detect_frame(video_frames)

    # # Draw Output
    # # Draw Player Bounding Boxes to Output video using Function from player_tracker.py
    output_video_frames = player_tracker.draw_bboxes(video_frames,player_detections)
    save_video(output_video_frames,"output_videos/output_video.avi")

if __name__=="__main__":
    main()
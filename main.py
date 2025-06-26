from youtube_client import get_channel_videos, get_all_video_data
from mongo_client import insert_video_data

channel_name = "SUPER XANDÃO"
videos = get_channel_videos(channel_name, max_results=5)

for video_data in get_all_video_data(videos):
    insert_video_data(video_data)

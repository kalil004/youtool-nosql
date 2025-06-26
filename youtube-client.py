from youtool import YouTubeClient

API_KEY = "SUA_API_KEY"
client = YouTubeClient(API_KEY)

def get_channel_videos(channel_name, max_results=10):
    channel = client.get_channel(channel_name)
    return client.get_channel_videos(channel['id'], max_results=max_results)

def get_all_video_data(videos):
    for video in videos:
        yield {
            "video_id": video['id'],
            "title": video['title'],
            "published_at": video['publishedAt'],
            "comments": client.get_video_comments(video['id']),
            "transcript": try_get_transcript(video['id']),
            "live_chat": try_get_livechat(video['id']),
        }

def try_get_transcript(video_id):
    try:
        return client.get_transcript(video_id)
    except:
        return None

def try_get_livechat(video_id):
    try:
        return client.get_live_chat(video_id)
    except:
        return None

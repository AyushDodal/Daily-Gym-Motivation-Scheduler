import json
import random
import requests
import os
import boto3
from googleapiclient.discovery import build

# Use environment variables for API keys
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
SNS_TOPIC_ARN = os.getenv('SNS_TOPIC_ARN')

def get_youtube_short(api_key, hashtag):
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    request = youtube.search().list(
        part="snippet",
        q=hashtag,
        type="video",
        videoDuration="short",
        maxResults=50,
        order="date"
    )
    response = request.execute()
    
    if response['items']:
	video_item = random.choice(response['items'])  # Pick a random video from the fetched list
        video_id = video_item['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        return video_url
    else:
        return None

def send_sns_notification(message):
    sns_client = boto3.client('sns')
    response = sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message,
        Subject="Your Daily Gym Motivation"
    )
    return response

def lambda_handler(event, context):
    video_url = get_youtube_short(YOUTUBE_API_KEY, "#gymmotivation")
    if video_url:
        send_sns_notification(f"Here's that gym motivation you didn't ask for: {video_url}")
    return {
        'statusCode': 200,
        'body': json.dumps('YouTube short sent!')
    }

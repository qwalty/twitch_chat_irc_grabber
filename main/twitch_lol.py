import os
import asyncio
import requests
import json
from dotenv import load_dotenv


load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


async def get_user_id(client_id: str, access_token: str, user_login: str) -> str:
    token_url = 'https://api.twitch.tv/helix/users'
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Client-Id": client_id
    }
    params = {
        'login': f'{user_login}'
    }
    resp = requests.get(token_url, headers=headers, params=params)
    return resp.json()["data"][0]["id"]

async def get_app_access_token(client_id: str, client_secret: str) -> str:
    token_url = "https://id.twitch.tv/oauth2/token"
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    resp = requests.post(token_url, data=data)
    return resp.json()["access_token"]

async def get_global_chat_badges(access_token: str, client_id: str) -> dict:
    url = "https://api.twitch.tv/helix/chat/badges/global"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Client-Id": client_id
    }
    resp = requests.get(url, headers=headers)
    return resp.json()

async def get_badges(access_token: str, client_id: str, broadcaster_id: str) -> dict:
    url = 'https://api.twitch.tv/helix/chat/badges'
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Client-Id": client_id
    }
    params = {
        'broadcaster_id':f'{broadcaster_id}'
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

async def main():
    try:
        token = get_app_access_token(CLIENT_ID, CLIENT_SECRET)
        id = get_user_id(CLIENT_ID, token, "bratishkinoff")
        badges_json = get_badges(token, CLIENT_ID, id)
        with open("../lol.json", "w") as f:
            f.write(json.dumps(badges_json, indent=2))
    except Exception as e:
        raise e


if __name__ == "__main__":
    asyncio.run(main())



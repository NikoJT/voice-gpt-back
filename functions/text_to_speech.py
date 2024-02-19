import requests

from decouple import config

ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")

def text_to_speech(message):
    print("text_to_speech message: ")
    print(message)

    body = {
        "text": message,
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0,
        }
    }

    voice_alexandra = "21m00Tcm4TlvDq8ikWAM"

    headers = { "xi-api-key": ELEVEN_LABS_API_KEY, "Content-Type": "application/json", "accept": "audio/mpeg" }
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_alexandra}"

    try:
        response = requests.post(endpoint, json=body, headers=headers)
        print("RESPONSE FROM ELEVENLABS: ")
        print(response)
    except Exception as e:
        print("EXCEPTZIONE!!!")
        print(e)
        return
    
    if response.status_code == 200:
        print("response status code is 200")
        print(response)
        return response.content
    else:
        print('else')
        return
from openai import OpenAI
from decouple import config
from functions.save_messages import get_recent_messages

client = OpenAI(
    # organization=config("OPEN_AI_ORG"),
    api_key=config("OPEN_AI_API_KEY")
)


# All API requests should include your API key in an Authorization HTTP header as follows:
# Authorization: Bearer OPENAI_API_KEY

# openai.organization = config("OPEN_AI_ORG")
# openai.api_key = config("OPEN_AI_KEY")

# Open AI Whisper
def convert_audio_to_text(audio_file):
    print("comes to conver_audio_to_text")
    try:
        transcript = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file, 
        response_format="text"
        )
        return transcript
    except Exception as e:
        print(e)
        return


def generate_response(text):
    messages = get_recent_messages()
    user_message = { "role": "user", "content": text }
    messages.append(user_message)
    try:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=messages
        )
        message_text = completion.choices[0].message.content
        return message_text
    except Exception as e:
        print(e)
        return



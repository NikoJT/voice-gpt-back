import json
import random


def get_recent_messages():
    file_name = "data.json"
    learn_instruction = {
        "role": "system",
        "content": "You are a general AI assistant named Alexandra, you need to answer back in the language the user is asking the question in. Keep answers to under 30 words."
    }

    messages = []

    x = random.uniform(0, 1)
    if x < 0.5:
        learn_instruction["content"] = learn_instruction["content"] + " Your response will include dry humor."
    else:
        learn_instruction["content"] = learn_instruction["content"] + "Your response will include dark humor."

    messages.append(learn_instruction)

    try:
        with open(file_name) as user_file:
            data = json.load(user_file)
            if data:
                if len(data) < 5:
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-5:]:
                        messages.append(item)
    except Exception as e:
        print(e)
        pass

    return messages


def store_messages(message, response_message):
    file_name = "data.json"
    messages = get_recent_messages()[1:]

    user_message = { "role": "user", "content": message }
    assistant_message = { "role": "assistant", "content": response_message }
    messages.append(user_message);
    messages.append(assistant_message);

    with open(file_name, "w") as f:
        json.dump(messages, f)


def reset_messages():
    open("data.json", "w")



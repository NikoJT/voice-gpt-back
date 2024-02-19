# uvicorn main:app
# uvicorn main:app --reload

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

# Function imports
from functions.save_messages import store_messages, reset_messages
from functions.openai_requests import convert_audio_to_text, generate_response
from functions.text_to_speech import text_to_speech

app = FastAPI()

# Cors - Origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
]

# Cors - middleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/post-audio")
async def post_audio(file: UploadFile = File(...)):
    print("comes here!")
    # audio_input = open("mila_holisee.mp3", "rb")
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    audio_input = open(file.filename, "rb")


    message_decoded = convert_audio_to_text(audio_input)

    if not message_decoded:
        return HTTPException(status_code=500, detail="Audio input failed to decode")

    chat_response = generate_response(message_decoded)

    if not chat_response:
        print("not chat resposne")
        print(chat_response)
        return HTTPException(status_code=500, detail="Failed to create chat response")

    store_messages(message_decoded, chat_response)

    audio_output = text_to_speech(chat_response)

    if not audio_output:
        return HTTPException(status_code=500, detail="Failed to create audio for chat response")

    def iterfile():
        yield audio_output

    print(chat_response)
    print(message_decoded)

    return StreamingResponse(iterfile(), media_type="application/octet-stream")


@app.get("/reset")
async def reset():
    reset_messages()
    return { "message": "Conversation reset" }
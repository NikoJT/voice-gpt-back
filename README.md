# Voice GPT

Voice GPT is a FastAPI service that provides audio-to-text and text-to-speech functionalities for frontend applications.

## Features

- Convert audio files to text.
- Generate responses based on the text input.
- Convert text responses to audio files.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/voice-gpt.git
    ```

2. Navigate to the project directory:

    ```bash
    cd voice-gpt
    ```

3. Set up a virtual environment:

    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    - Unix/Linux/macOS:

        ```bash
        source venv/bin/activate
        ```

    - Windows:

        ```bash
        venv\Scripts\activate.bat
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
6. Environment variables:
    - Change .example.env to .env
    - Change the api keys to use your own api keys.
    ```
        OPEN_AI_API_KEY=example_api_key
        OPEN_AI_ORG=org-example_org_key
        ELEVEN_LABS_API_KEY=example_eleven_labs_key
    ```
    - Organization key is not mandatory, but if you want to use it instead of the api key
    usage uncomment the
    
    ### ´´´organization=config("OPEN_AI_ORG")´´´
    on functions/openai_requests.py on line 6
## Usage

1. Start the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

2. Access the API endpoints:

    - Audio to Text: POST /post-audio
    - Reset conversation: GET /reset

3. Use the provided API endpoints in your frontend application to interact with the Voice GPT service.

## API Endpoints

### POST /post-audio

This endpoint handles audio input, converts it to text, generates a response, and converts the response to audio.

**Request:**

- Method: POST
- Endpoint: `/post-audio`
- Body: FormData with audio file (multipart/form-data)

**Response:**

- If successful, returns the generated audio response.
- If there's an error, returns an appropriate HTTP status code and error message.


## Resetting Conversation

### GET /reset

This endpoint resets the conversation, clearing any stored messages.

**Request:**

- Method: GET
- Endpoint: `/reset`

**Response:**

- Returns a message confirming the conversation reset.

## Contributors

- NikoJT

## License

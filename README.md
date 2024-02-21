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

## Usage

1. Start the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

2. Access the API endpoints:

    - Audio to Text: POST /post-audio
    - Text to Speech: [Add relevant endpoint]

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

### [Add more endpoints if applicable]

## Resetting Conversation

### GET /reset

This endpoint resets the conversation, clearing any stored messages.

**Request:**

- Method: GET
- Endpoint: `/reset`

**Response:**

- Returns a message confirming the conversation reset.

## Contributors

- [Your Name or Username]

Feel free to add yourself as a contributor if you've made contributions to the project.

## License

[Add license information here, if applicable]

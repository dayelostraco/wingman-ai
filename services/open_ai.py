from openai import OpenAI


class OpenAi:
    def __init__(
        self,
        openai_api_key: str = "",
    ):
        self.api_key = openai_api_key
        self.client = OpenAI(
            api_key=openai_api_key,
        )

    def transcribe(
        self,
        filename: str,
        model: str = "whisper-1",
        **params,
    ):
        with open(filename, "rb") as audio_input:
            transcript = self.client.audio.transcriptions.create(
                model=model,
                file=audio_input,
                **params,
            )
            return transcript

    def ask(
        self,
        messages: list[dict[str, str]],
        model: str = "gpt-4-1106-preview",
        stream: bool = False,
        tools: list[dict[str, any]] = None,
    ):
        if not tools:
            completion = self.client.chat.completions.create(
                stream=stream,
                messages=messages,
                model=model,
            )
        else:
            completion = self.client.chat.completions.create(
                stream=stream,
                messages=messages,
                model=model,
                tools=tools,
                tool_choice="auto",
            )
        return completion

    def speak(self, text: str, voice: str = "nova"):
        if not voice:
            voice = "nova"
        response = self.client.audio.speech.create(
            model="tts-1",
            voice=voice,
            input=text,
        )
        return response

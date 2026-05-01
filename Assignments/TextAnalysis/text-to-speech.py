from google.cloud import texttospeech


def synthesize_text(text: str, output_file: str = "resources/output.mp3"):
    client = texttospeech.TextToSpeechClient()

    # Set the text input
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Configure the voice
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
    )

    # Configure the audio output
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the synthesis
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config,
    )

    # Save to file
    with open(output_file, "wb") as f:
        f.write(response.audio_content)
    print(f"Audio saved to {output_file}")


def synthesize_ssml(ssml, output_file: str = "resources/output_ssml.mp3"):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(ssml=ssml)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Neural2-C",  # specific voice name
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=1.0,   # 0.25 to 4.0
        pitch=0.0,           # -20.0 to 20.0 semitones
        volume_gain_db=0.0,  # -96.0 to 16.0
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open(output_file, "wb") as f:
        f.write(response.audio_content)
    print(f"Audio saved as {output_file}")


synthesize_text("I can't rate this low enough. If I could give 0 stars, I would. I watched this at the cinema when it came out but had no choice but to walk out part way through. Everything, from the action, the script, the plot, the acting, the sets, music.... is diabolical. ")

ssml = """
    <speak>
    <prosody rate="slow" volume="loud">
        I can't rate this low enough.
        <break time="500ms"/>
        If I could give 
        <emphasis level="strong">0 stars</emphasis>, 
        I would.
    </prosody>
    <break time="800ms"/>
    <prosody rate="medium">
        I watched this at the cinema when it came out but had no choice but to walk out part way through.
    </prosody>
    <break time="600ms"/>
    <prosody pitch="low" rate="slow">
        Everything, from the action, the script, the plot, the acting, the sets, music.... 
        <break time="400ms"/>
        is 
        <prosody volume="loud">
            <emphasis level="strong">diabolical</emphasis>
        </prosody>.
    </prosody>
    </speak>

"""

synthesize_ssml(ssml)


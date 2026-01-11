# Plan: Google Cloud Text-to-Speech Integration

This plan outlines the steps to add Google Cloud Text-to-Speech (TTS) as an alternative to OpenAI for generating manuscript audio.

## 1. Google Cloud Setup
- **Enable API**: Enable the "Cloud Text-to-Speech API" in the Google Cloud Console.
- **Service Account**: Create a Service Account with "Cloud Text-to-Speech API User" permissions.
- **Credentials**: Generate and download a JSON key for the Service Account.
- **Environment**: Update `.env` to include the path to this JSON key.

## 2. Dependencies
- Install the Google Cloud TTS library:
  ```bash
  pip install google-cloud-texttospeech
  ```

## 3. Script Refactoring (`render_manuscript_audio.py`) [DONE]
- **Provider Selection**: Added logic to read `TTS_PROVIDER` from `.env` (values: `openai` or `google`).
- **Abstract Rendering**: Refactored the paragraph rendering loop to use provider-specific functions.
- **Google Implementation**:
  - Initialized the `TextToSpeechClient`.
  - Configured `VoiceSelectionParams` and `AudioConfig`.
- **Error Handling**: Added specific error handling for Google Cloud API responses.

## 4. Configuration Updates [DONE]
- Updated `.env.example` in `ff-teaser` to include Google Cloud relevant variables.

## 5. Verification
- Test rendering a single paragraph with the new provider.
- Verify audio quality and VTT timestamp alignment (which depends on `get_audio_duration` using `ffprobe`, so it should be fine).

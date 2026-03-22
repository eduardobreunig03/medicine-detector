# Medicine Detector

A Python tool that transcribes audio files using OpenAI's Whisper API and automatically detects mentions of common medicines in the transcription. Results are saved to a text file.

---

## What It Does

1. Accepts a path to an audio file (mp3, wav, m4a, etc.)
2. Transcribes the audio using OpenAI's **Whisper-1** model
3. Scans the transcription for mentions of known medicines
4. Saves the detected medicines to `medicines.txt`

### Detected Medicines

The following medicines are currently recognized:

`panadol`, `nurofen`, `aspirin`, `ibuprofen`, `tylenol`, `advil`, `voltaren`, `zyrtec`

---

## Prerequisites

- Python 3.8+
- An [OpenAI API key](https://platform.openai.com/api-keys)

---

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure your API key

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_api_key_here
```

---

## How to Run

```bash
python medicine_detector.py
```

You will be prompted to enter the path to your audio file:

```
Enter the path to the audio file: /path/to/recording.mp3
```

The script will print the transcribed text and save any detected medicine mentions to `medicines.txt`.

---

## Output

- **`medicines.txt`** — lists each detected medicine on its own line, or states `No medicine mentions found.` if none were found.

---

## Project Structure

```
medecine_detector/
├── medicine_detector.py   # Main script
├── medicines.txt          # Output file (generated on run)
├── requirements.txt       # Python dependencies
├── audio_files/           # Place your audio files here
└── .env                   # API key (not committed)
```

---

## Dependencies

| Package | Purpose |
|---|---|
| `openai` | Whisper transcription API |
| `python-dotenv` | Load API key from `.env` |
| `SpeechRecognition` | Audio utilities |
| `pydub` | Audio file processing |
| `python-docx` | Document export support |

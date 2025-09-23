from pathlib import Path


DATA_DIR = Path("/workspace/data")
OUTPUTS_DIR = DATA_DIR / "outputs"


def synthesize_voiceover(script_path: str) -> str:
    """Create placeholder voiceover audio from a script.

    Returns absolute path to the audio file.
    """
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    script_text = Path(script_path).read_text()
    topic_slug = Path(script_path).stem.replace("_script", "")
    audio_path = OUTPUTS_DIR / f"{topic_slug}_voiceover.wav"
    # Placeholder: store the text for traceability
    audio_path.write_bytes(("VOICEOVER:\n" + script_text).encode("utf-8"))
    return str(audio_path)


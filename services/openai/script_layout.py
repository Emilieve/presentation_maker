import json
from pathlib import Path
from typing import Tuple

# from services.openai.client import create_openai_client  # Uncomment when using real API


DATA_DIR = Path(__file__).parent.parent.parent / "data"
OUTPUTS_DIR = DATA_DIR / "outputs"
TEMP_DIR = DATA_DIR / "temp"


def generate_script_and_layout(topic: str) -> Tuple[str, str]:
    """Generate a script and an animation layout for the given topic.

    This is a placeholder implementation that writes simple files to the
    outputs directory. Replace with a real OpenAI call as needed.
    Returns absolute paths to the created script and layout files.
    """
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)

    # Placeholder content. Replace with real prompt + OpenAI call.
    normalized = topic.replace(" ", "_").lower()
    script_text = (
        f"Video Script for: {topic}\n\n"
        "1) Hook: Why this matters.\n"
        "2) Body: Key points explained clearly.\n"
        "3) Outro: Summary and call-to-action.\n"
    )
    layout_spec = {
        "topic": topic,
        "scenes": [
            {"id": "s1", "description": "Opening animation for the hook"},
            {"id": "s2", "description": "Main content visuals"},
            {"id": "s3", "description": "Closing animation and CTA"},
        ],
    }

    script_path = OUTPUTS_DIR / f"{normalized}_script.txt"
    layout_path = OUTPUTS_DIR / f"{normalized}_layout.json"

    script_path.write_text(script_text)
    layout_path.write_text(json.dumps(layout_spec, indent=2))

    return str(script_path), str(layout_path)


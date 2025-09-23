from pathlib import Path
from typing import List


DATA_DIR = Path("/workspace/data")
OUTPUTS_DIR = DATA_DIR / "outputs"


def add_character_voiceover(animation_paths: List[str], voiceover_path: str) -> str:
    """Combine animations with a placeholder AI character and voiceover.

    Returns absolute path to the final video file.
    """
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    if not animation_paths:
        raise ValueError("No animations provided")

    topic_slug = Path(animation_paths[0]).stem.split("_scene_")[0]
    final_video = OUTPUTS_DIR / f"{topic_slug}_final.mp4"
    # Placeholder: write a marker for combined output
    final_video.write_bytes(b"placeholder-final-video")
    return str(final_video)


import json
from pathlib import Path
from typing import List


DATA_DIR = Path(__file__).parent.parent.parent / "data"
OUTPUTS_DIR = DATA_DIR / "outputs"


def generate_animations(layout_path: str) -> List[str]:
    """Create placeholder animation files for each scene in the layout.

    Returns a list of absolute file paths for generated animations.
    """
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

    layout = json.loads(Path(layout_path).read_text())
    topic_slug = layout.get("topic", "topic").replace(" ", "_").lower()

    animation_paths: List[str] = []
    for index, scene in enumerate(layout.get("scenes", []), start=1):
        anim_path = OUTPUTS_DIR / f"{topic_slug}_scene_{index}.mp4"
        # Placeholder: write a tiny marker file to represent the animation asset
        anim_path.write_bytes(b"placeholder-animation-bytes")
        animation_paths.append(str(anim_path))

    return animation_paths


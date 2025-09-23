import argparse
import json
from typing import Dict

from services.openai.script_layout import generate_script_and_layout
from services.animation.generator import generate_animations
from services.voice.tts import synthesize_voiceover
from services.character.actor import add_character_voiceover


def run(topic: str) -> Dict[str, str]:
    script_path, layout_path = generate_script_and_layout(topic)
    animations = generate_animations(layout_path)
    voiceover_path = synthesize_voiceover(script_path)
    final_video_path = add_character_voiceover(animations, voiceover_path)
    return {
        "script_path": script_path,
        "layout_path": layout_path,
        "voiceover_path": voiceover_path,
        "final_video_path": final_video_path,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run topic-to-video pipeline")
    parser.add_argument("topic", help="Topic to generate video for")
    args = parser.parse_args()
    result = run(args.topic)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()


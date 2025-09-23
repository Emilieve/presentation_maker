from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.openai.script_layout import generate_script_and_layout
from services.animation.generator import generate_animations
from services.voice.tts import synthesize_voiceover
from services.character.actor import add_character_voiceover


router = APIRouter(tags=["pipeline"])


class TopicRequest(BaseModel):
    topic: str


class PipelineResponse(BaseModel):
    topic: str
    script_path: str
    layout_path: str
    animations: list[str]
    voiceover_path: str
    final_video_path: str


@router.post("/pipeline", response_model=PipelineResponse)
async def run_pipeline(request: TopicRequest):
    try:
        script_path, layout_path = generate_script_and_layout(request.topic)
        animations = generate_animations(layout_path)
        voiceover_path = synthesize_voiceover(script_path)
        final_video_path = add_character_voiceover(animations, voiceover_path)

        return PipelineResponse(
            topic=request.topic,
            script_path=script_path,
            layout_path=layout_path,
            animations=animations,
            voiceover_path=voiceover_path,
            final_video_path=final_video_path,
        )
    except Exception as exc:  # pragma: no cover - simple error propagation
        raise HTTPException(status_code=500, detail=str(exc))


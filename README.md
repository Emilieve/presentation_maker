# Topic → Script & Layout → Animations → AI Character Voiceover

Pipeline scaffold that:

1. Accepts a topic
2. Retrieves a script and animation layout (OpenAI placeholder)
3. Generates animations (placeholder files)
4. Adds an AI character with voiceover (placeholder final video)

## Quickstart

1) Install Python deps:

```
make install
```

2) Run API:

```
make api
```

POST `http://localhost:8000/api/pipeline` with JSON:

```
{ "topic": "Black holes" }
```

3) Run CLI:

```
make cli TOPIC="Black holes"
```

Outputs are written under `data/outputs`.

## Configuration

Copy `.env.example` to `.env` and set `OPENAI_API_KEY` when using real API calls.

## Structure

- `api/` FastAPI app and routes
- `services/` domain services: `openai`, `animation`, `voice`, `character`
- `app/cli/` CLI runner
- `data/` inputs, outputs, temp, assets


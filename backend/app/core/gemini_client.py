"""
Gemini API wrapper with async generation and retry.
"""

import asyncio
import time
from typing import Any
import google.generativeai as genai
from langsmith import traceable
from loguru import logger
from app.config import settings


genai.configure(api_key=settings.GEMINI_API_KEY)


class GeminiClient:
    def __init__(self) -> None:
        self.model = genai.GenerativeModel(
            model_name=settings.GEMINI_MODEL,
            generation_config=genai.GenerationConfig(
                max_output_tokens=settings.GEMINI_MAX_TOKENS,
                temperature=settings.GEMINI_TEMPERATURE,
            ),
        )
        self._last_request_time: float = 0
        self._min_interval: float = 6.5

    async def _rate_limit(self) -> None:
        elapsed = time.monotonic() - self._last_request_time
        wait = self._min_interval - elapsed
        if wait > 0:
            await asyncio.sleep(wait)
        self._last_request_time = time.monotonic()

    @traceable(name="gemini_generate")
    async def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
        max_retries: int = 3,
    ) -> str:
        await self._rate_limit()

        contents: list[Any] = []
        if system_prompt:
            contents.append({"role": "user", "parts": [system_prompt]})
            contents.append({"role": "model", "parts": ["Understood."]})
        contents.append({"role": "user", "parts": [prompt]})

        for attempt in range(max_retries):
            try:
                response = await asyncio.to_thread(
                    self.model.generate_content, contents
                )
                return response.text
            except Exception as exc:
                wait_time = 2 ** attempt * 5
                logger.warning(
                    "Gemini attempt {attempt}/{max_retries} failed: {error}. "
                    "Retrying in {wait}s...".format(
                        attempt=attempt + 1,
                        max_retries=max_retries,
                        error=exc,
                        wait=wait_time,
                    )
                )
                if attempt < max_retries - 1:
                    await asyncio.sleep(wait_time)
                else:
                    raise

        raise RuntimeError("Gemini: all retries exhausted")


gemini_client = GeminiClient()

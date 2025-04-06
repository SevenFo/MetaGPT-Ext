#!/usr/bin/env python
"""
Mock LLM configurations for testing
"""

from metagpt.core.configs.llm_config import LLMConfig

mock_llm_config_anthropic = LLMConfig(
    api_type="anthropic", api_key="xxx", base_url="https://api.anthropic.com", model="claude-3-opus-20240229"
)

"""Custom exception hierarchy for AgentForge."""


class AgentForgeError(Exception):
    """Base error for AgentForge."""


class ConfigurationError(AgentForgeError):
    """Raised when required configuration is missing or invalid."""

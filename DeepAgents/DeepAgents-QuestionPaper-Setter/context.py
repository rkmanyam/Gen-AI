"""
This module contains context related items
"""

from dataclasses import dataclass


@dataclass
class ContextSchema:
    difficulty: str
    date: str
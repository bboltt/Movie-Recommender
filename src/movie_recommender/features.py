"""Core helper functions adapted from the recommendation notebooks.

These utilities are intentionally lightweight so they can be imported by
notebooks, scripts, and tests without requiring a running Spark session.
"""

from __future__ import annotations

import re
from collections.abc import Iterable, Sequence


def extract_year(title: str) -> int | None:
    """Extract a 4-digit year from a movie title.

    Parameters
    ----------
    title:
        A movie title that may contain a year in parentheses, e.g.
        ``"Toy Story (1995)"``.

    Returns
    -------
    int | None
        The extracted year as an integer, or ``None`` if no valid year is
        present.
    """

    match = re.search(r"\((\d{4})\)", title)
    return int(match.group(1)) if match else None


def convert_vector(vector: Iterable[float]) -> list[float]:
    """Convert an iterable numeric vector into a plain list of floats.

    This is useful when serializing vectors for storage in systems that expect
    JSON-compatible arrays.
    """

    return [float(value) for value in vector]


def reverse_convert(vector_list: Sequence[float]) -> tuple[float, ...]:
    """Convert a sequence representation back into an immutable tuple."""

    return tuple(float(value) for value in vector_list)


def get_poster_url(movie_id: int, base_url: str = "https://image.tmdb.org/t/p/w500") -> str:
    """Build a deterministic poster URL for a given movie id.

    Parameters
    ----------
    movie_id:
        Integer identifier for the movie.
    base_url:
        Base URL for poster hosting.
    """

    return f"{base_url}/{movie_id}.jpg"


def get_similar(scores: Sequence[float], top_k: int = 5) -> list[int]:
    """Return indices of the top-k highest scores in descending order.

    Parameters
    ----------
    scores:
        Sequence of similarity or relevance scores.
    top_k:
        Number of top results to return.

    Returns
    -------
    list[int]
        Index positions sorted by score (highest first), then by index for
        deterministic ordering of ties.
    """

    ranked = sorted(enumerate(scores), key=lambda item: (-item[1], item[0]))
    return [index for index, _ in ranked[:top_k]]

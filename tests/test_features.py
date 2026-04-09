"""Pytest coverage for movie_recommender feature utilities."""

from movie_recommender.features import convert_vector, extract_year, get_poster_url, get_similar, reverse_convert


def test_extract_year_present() -> None:
    """Extracts a valid release year from a standard movie title."""

    assert extract_year("Toy Story (1995)") == 1995


def test_extract_year_missing() -> None:
    """Returns None when no year token exists in the title."""

    assert extract_year("Unknown Title") is None


def test_convert_and_reverse_vector_round_trip() -> None:
    """Converts iterable vectors to list form and back to tuple form."""

    original = (1, 2.5, 3)
    as_list = convert_vector(original)
    back_to_tuple = reverse_convert(as_list)

    assert as_list == [1.0, 2.5, 3.0]
    assert back_to_tuple == (1.0, 2.5, 3.0)


def test_get_poster_url() -> None:
    """Builds the expected URL format for poster retrieval."""

    assert get_poster_url(42).endswith("/42.jpg")


def test_get_similar_returns_sorted_top_k_indices() -> None:
    """Ranks indices by descending score and deterministic tie-breaking."""

    scores = [0.3, 0.9, 0.9, 0.1]
    assert get_similar(scores, top_k=3) == [1, 2, 0]

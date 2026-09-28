from demo_service.tags import unique_tags


def test_unique_tags_drops_duplicates():
    assert sorted(unique_tags(["red", "green", "red", "blue"])) == ["blue", "green", "red"]


def test_unique_tags_of_nothing_is_empty():
    assert unique_tags([]) == []

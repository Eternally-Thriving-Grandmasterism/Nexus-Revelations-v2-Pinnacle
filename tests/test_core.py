from nexus_revelations import NexusRevelationEngine

def test_inject():
    nexus = NexusRevelationEngine()
    rev = nexus.inject_insight("Test query")
    assert rev["scarcity_elimination"] == "complete"
    assert "revelation" in rev

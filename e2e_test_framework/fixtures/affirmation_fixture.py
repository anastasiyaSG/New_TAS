import random
import pytest

AFFIRMATIONS = [
    "You are the guardian of quality—every bug you catch is a win for users!",
    "Your attention to detail makes the product shine.",
    "Every test you write is a step toward excellence.",
    "QA specialists turn chaos into confidence—keep going!",
    "Your curiosity and persistence make the team stronger.",
    "You help deliver joy to users by ensuring quality!",
    "Your work prevents problems before they reach the world."
]

@pytest.fixture()
def nice_affirmation():
    """Fixture to provide a random nice affirmation for QA specialists."""
    return random.choice(AFFIRMATIONS)

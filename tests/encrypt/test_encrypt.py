import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message("hello", "world")
    with pytest.raises(TypeError):
        encrypt_message(42, 2)

    assert encrypt_message("hello", 0) == "olleh"
    assert encrypt_message("hello", 5) == "olleh"
    assert encrypt_message("hello", -1) == "olleh"

    assert encrypt_message("hello", 1) == "h_olle"
    assert encrypt_message("hello", 3) == "leh_ol"
    assert encrypt_message("hello", 2) == "oll_eh"
    assert encrypt_message("hello", 4) == "o_lleh"

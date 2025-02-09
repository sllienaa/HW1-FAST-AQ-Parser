# write tests for transcribes

from seqparser import (
    transcribe,
    reverse_transcribe
)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the
    transcribe function here.
    """
    # check that the transcribed test sequence is correct
    transcribed = transcribe("ACTGAACCC")
    assert transcribed == "UGACUUGGG"


def test_reverse_transcribe():
    """
    Write your unit test for the
    reverse transcribe function here.
    """
    # check that the reverse transcribed test sequence is correct
    reversed_transcribed = reverse_transcribe("ACTGAACCC")
    assert reversed_transcribed == "GGGUUCAGU"

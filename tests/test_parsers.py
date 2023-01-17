# write tests for parsers

import pytest
from seqparser import FastaParser, FastqParser

def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

def get_filepath(which):
    data_dir = pathlib.Path(__file__).resolve().parent.parent / "data"
    if which == "fasta":
        return data_dir / "test.fa"
    else:
        return data_dir / "test.fq"


def open_fastq_reference():
    f = pathlib.Path(__file__).resolve().parent / "fastq-check.txt"
    with f.open() as f:
        seqs = list(map(lambda l: l.strip().split("|"), f.readlines()))
    return seqs  # will be list of lists with seq, quality that were parsed from the test files using get-seq.sh


def open_fasta_reference():
    f = pathlib.Path(__file__).resolve().parent / "fasta-check.txt"
    with f.open() as f:
        seqs = list(map(lambda l: l.strip(), f.readlines()))
    return seqs  # will be a list of seqs, quality that were parsed from the test files using get-seq.sh
        
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    # read in test data
    fasta_parsed_data = FastaParser("./data/test.fa")

    # for each sequence in the test file
    for seq in fasta_parsed_data:
        # make sure there are 2 elements per FastaParser object (ID and sequence)
        assert len(seq) == 2, "failed to have an ID and sequence per line"
        # make sure the sequence ID contains the string "seq"
        assert "seq" in seq[0], "test data's sequence IDs don't contain the string 'seq', incorrectly read"


def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    # read in test data, as a FastqParser object and parsed
    fastq_parsed_data = FastqParser("./data/test.fq")
    fastq_records = [seq for seq in fastq_parsed_data]

    # check the first record's sequence to see if it is being read in correctly
    assert fastq_records[0][1] == ("TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG",
                                   "first record's sequence is incorrect")
    # for each sequence in the test file
    for seq in fastq_parsed_data:
        # make sure each fastq nucleotide sequence is 100 base pairs
        assert len(seq[1]) == 100, "fastq nucleotide sequences are not the correct length, incorrectly parsed"

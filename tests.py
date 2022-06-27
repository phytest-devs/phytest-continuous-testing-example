from phytest import Sequence, Tree, Data

def test_sequences_in_metadata(sequence: Sequence, data: Data):
    # ensure all sequences are in the metadata
    data.assert_contains('ID', sequence.id)

def test_sequences_in_tree(sequence: Sequence, tree: Tree):
    # ensure all sequences are in the tree
    assert sequence.id in [clade.name.split('_')[0] for clade in tree.get_terminals()]

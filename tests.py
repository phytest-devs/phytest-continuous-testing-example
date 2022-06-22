from phytest import Sequence, Tree, DataFrame

def test_sequences_in_metadata(sequence: Sequence, data: DataFrame):
    # ensure all sequences are in the metadata
    assert sequence.id in data['ID'].values

def test_sequences_in_tree(sequence: Sequence, tree: Tree):
    # ensure all sequences are in the tree
    assert sequence.id in [clade.name.split('_')[0] for clade in tree.get_terminals()]
"""Testing suite for passive checker."""

import pandas as pd
from labeler.utils.passivity_check import PassiveChecker
from pathlib import Path

test_data = 'test.csv'


def test_passivity():

    directory = Path(__file__).parent
    path = f'{directory}/{test_data}'
    df = pd.read_csv(path)
    df = PassiveChecker(df).check_for_passives_df()

    assert df.iloc[0]['binary'] == 1
    assert df.iloc[1]['binary'] == 0
    assert df.iloc[2]['binary'] == 0
    assert df.iloc[3]['binary'] == 0

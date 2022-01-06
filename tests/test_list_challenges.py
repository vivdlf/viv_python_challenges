import pytest
from code_challenge.list_challenges import two_sum


@pytest.mark.xfail(reason="two_sum() hasn't been implemented yet")
@pytest.mark.parametrize(
    'input_list,target,expected', 
    [
        ([2,7,11,15], 9, [0,1]),
        ([3,2,4], 6, [1,2]),
        ([3,3], 6, [0,1]),
    ]
)
def test_two_sum(input_list, target, expected):
    # Arrange

    # Act
    actual = two_sum(input_list, target)

    # Assert
    assert actual == expected

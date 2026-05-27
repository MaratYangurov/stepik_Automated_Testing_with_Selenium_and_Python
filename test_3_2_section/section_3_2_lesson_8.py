def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"

a = test_input_text(8, 11)
a = test_input_text(11, 11)
a = test_input_text(11, 15)
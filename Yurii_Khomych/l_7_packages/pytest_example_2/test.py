import pytest

from my_test_app import test_app


@pytest.fixture(params=["nodict", "dict"])
def generate_initial_transform_parameters(request):
    test_input = {
        "name": "John Q. Public",
        "street": "123 Main St.",
        "city": "Anytown",
        "state": "FL",
        "zip": 99999,
    }
    expected_output = {
        "name": "John Q. Public",
        "street": "123 Main St.",
        "city": "Anytown",
        "state": "FL",
        "zip": 99999,
    }

    if request.param == "dict":
        test_input["relastionships"] = {
            "siblings": ["Michael R. Public", "Suzy Q. Public"],
            "parents": ["John Q. Public Sr.", "Mary S. Public"],
        }
        expected_output["siblings"] = ["Michael R. Public", "Suzy Q. Public"]
        expected_output["parents"] = ["John Q. Public Sr.", "Mary S. Public"]

    return test_input, expected_output


# @pytest.fixture()
# def generate_initial_final_transform_parameters():
#     test_input = {
#         "name": "John Q. Public",
#         "street": "123 Main St.",
#         "city": "Anytown",
#         "state": "FL",
#         "zip": 99999,
#     }
#     expected_output = {
#         "name": "John Q. Public",
#         "street": "123 Main St.",
#         "city": "Anytown",
#         "state": "FL",
#         "zip": 99999,
#         "address": f"{test_input['street']}\n{test_input['state']}, {test_input['city']}",
#         zip needed
    # }
    #
    # return test_input, expected_output


def test_initial_transform(generate_initial_transform_parameters):
    test_input = generate_initial_transform_parameters[0]
    expected_output = generate_initial_transform_parameters[1]
    assert test_app.initial_transform(test_input) == expected_output


# second example
# def test_final_transform(generate_initial_final_transform_parameters):
#     test_input = generate_initial_final_transform_parameters[0]
#     expected_output = generate_initial_final_transform_parameters[1]
#     assert test_app.final_transform(test_input) == expected_output

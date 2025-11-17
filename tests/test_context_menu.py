import pytest

from unittest.mock import Mock
from unittest.mock import patch
from src.menus.context_menu import Menu


@pytest.fixture
def menu():
    return Menu()


@pytest.mark.parametrize("input_prompt, prompt_return", [("1", "1"), ("2", "2")])
def test_prompt_nonempty(input_prompt, prompt_return):
    with patch("builtins.input") as mock_input:
        mock_input.side_effect = input_prompt
        result = Menu._prompt_nonempty(prompt="")
        assert result == prompt_return


def test_prompt_nonempty_print(menu):
    with (
        patch("builtins.input", side_effect=["", "ok"]),
        patch("builtins.print") as mock_print,
    ):
        result = menu._prompt_nonempty(prompt="anything")

    assert result == "ok"
    mock_print.assert_any_call("Please enter a none empty string")


@pytest.mark.parametrize(
    "fake_input, options, expected",
    [
        (["1"], ["1", "2"], "1"),
        (["3", "2"], ["1", "2"], "2"),
    ],
)
def test_validate_output(fake_input, options, expected):
    with (
        patch("builtins.input", side_effect=fake_input),
        patch("builtins.print") as mock_print,
    ):
        result = Menu._validate_input(prompt="", options=options)

    assert result == expected

    if len(fake_input) > 1:
        mock_print.assert_called_once_with(
            f"Invalid option, choose one in : {' '.join(options)}"
        )


@patch("builtins.print")
def test_show_options(mock_print):
    Menu.show_options()

    mock_print.assert_called_with(
        "1 - Read file"
        "\n2 - Encrypt data"
        "\n3 - Decrypt data"
        "\n4 - Write file"
        "\n5 - Append to file"
        "\n6 - Show buffer"
        "\n7 - Clear buffer"
        "\n8 - Exit"
    )


def test_menu_case_1():
    mock_manager = Mock()
    menu = Menu()
    menu.manager = mock_manager

    with patch("builtins.input", return_value="test.json"):
        menu.menu_handler(1)

    mock_manager.handle_read_file.assert_called_once_with("test.json")


def test_menu_case_2():
    mock_manager = Mock()
    menu = Menu()
    menu.manager = mock_manager

    with patch("builtins.input", side_effect=["1", "abc"]):
        menu.menu_handler(2)

    mock_manager.encrypt.assert_called_once_with(1, "abc")


def test_menu_case_3():
    mock_manager = Mock()
    menu = Menu()
    menu.manager = mock_manager

    with patch("builtins.input", return_value="anything"):
        menu.menu_handler(3)

    mock_manager.decrypt.assert_called_once_with()


def test_menu_case_4():
    mock_manager = Mock()
    menu = Menu()
    menu.manager = mock_manager

    with patch("builtins.input", return_value="test"):
        menu.menu_handler(4)

    mock_manager.handle_write_file.assert_called_once_with("test")


def test_menu_case_5():
    mock_manager = Mock()
    menu = Menu()
    menu.manager = mock_manager

    with patch("builtins.input", return_value="test"):
        menu.menu_handler(5)

    mock_manager.handle_append_to_file.assert_called_once_with("test")


def test_menu_case_6():
    mock_manager = Mock()
    menu = Menu()
    menu.manager = mock_manager

    mock_manager.buffer = Mock()
    mock_manager.buffer.data = ["abc"]

    with patch("builtins.print") as mock_print:
        menu.menu_handler(6)

    mock_print.assert_called_once_with(["abc"])


def test_menu_case_7():
    mock_manager = Mock()
    menu = Menu()
    menu.manager = mock_manager

    with patch("builtins.print") as mock_print:
        menu.menu_handler(7)

    mock_manager.buffer.clear.assert_called_once_with()
    mock_print.assert_called_once_with(
        "Buffer cleared! You can add new data to buffer."
    )

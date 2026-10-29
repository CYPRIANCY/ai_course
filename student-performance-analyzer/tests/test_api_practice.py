import requests
import unittest
from unittest.mock import Mock, patch

from api_practice import fetch_user


class TestFetchUser(unittest.TestCase):

    @patch("api_practice.requests.get")
    def test_fetch_user_success(self, mock_get: Mock) -> None:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": 1,
            "name": "Cyprian",
            "email": "cyprian@example.com",
            "address": {"city": "Abuja"},
        }

        mock_get.return_value = mock_response

        with patch("builtins.print") as mock_print:
            fetch_user(1)

        mock_get.assert_called_once_with(
            "https://jsonplaceholder.typicode.com/users/1",
            timeout=10,
        )

        mock_print.assert_any_call("Name:", "Cyprian")
        mock_print.assert_any_call("Email:", "cyprian@example.com")
        mock_print.assert_any_call("City:", "Abuja")
    

    @patch("api_practice.requests.get")
    def test_fetch_user_http_error(self, mock_get: Mock) -> None:
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = (
            requests.exceptions.HTTPError("404 Not Found")
        )
        mock_get.return_value = mock_response

        with patch("builtins.print") as mock_print:
            fetch_user(9999)

        mock_print.assert_called_once_with(
            "The API returned an HTTP error:",
            mock_response.raise_for_status.side_effect,
        )
    

    @patch("api_practice.requests.get")
    def test_fetch_user_missing_address(self, mock_get: Mock) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {
            "id": 1,
            "name": "Cyprian",
            "email": "cyprian@example.com",
        }
        mock_get.return_value = mock_response

        with patch("builtins.print") as mock_print:
            fetch_user(1)

        mock_print.assert_called_once_with(
            "Invalid API response: missing address or city."
        )




if __name__ == "__main__":
    unittest.main()
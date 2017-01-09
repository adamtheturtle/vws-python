"""
Tests for getting a target record.

https://library.vuforia.com/articles/Solution/How-To-Retrieve-a-Target-Record-Using-the-VWS-API
"""

import pytest


@pytest.mark.usefixtures('verify_mock_vuforia')
class TestGetRecord:
    """
    Tests for getting a target record.
    """

    def test_get_target(self, target_id: str) -> None:
        """
        Details of a target are returned.
        """
        pass

import unittest
from datetime import datetime, timezone

from crontab import CronTab


class TestCrontab(unittest.TestCase):
    """Test class for crontab 3rd party library"""

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

        return

    def test_get_next(self):
        # *** Prepare ***
        schedule = CronTab("*/1 * * * *")  # every 1 minute
        now = datetime(2023, 3, 21, 12, 0, 0, tzinfo=timezone.utc)

        # *** Execute ***
        delay = schedule.next(now)

        # *** Verify ***
        self.assertEqual(delay, 60)

        return

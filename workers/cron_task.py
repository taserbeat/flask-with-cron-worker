from datetime import datetime, timezone, timedelta
import typing as t
import subprocess

from workers.cron_task_process import CronTaskProcess
from workers.cron_task_option import CronTaskOption

from crontab import CronTab


class CronTask:
    def __init__(self, option: CronTaskOption) -> None:
        self.__process: t.Optional[CronTaskProcess] = None
        self.__option = option
        self.__next_start_at: t.Optional[datetime] = None

        return

    @property
    def is_running(self):
        """Whether the process called by CronWorker is running"""

        if self.__process is None:
            return False
        return not self.__process.is_exited

    def start(self, now: t.Optional[datetime] = None):
        if self.is_running:
            return

        if not isinstance(self.__next_start_at, datetime):
            return

        if not isinstance(now, datetime):
            now = datetime.now(tz=timezone.utc)

        if now < self.__next_start_at:
            return

        try:
            # FIXME: The process called by CronWorker is started twice because 'subprocess' is called from 'multiprocessing'.
            self.__process = CronTaskProcess(
                target=subprocess.run,
                args=([self.__option.command]),
                name=self.__option.task_name,
                kwargs={"shell": True, "cwd": self.__option.cwd}
            )
            self.__process.start()
        except Exception as e:
            raise e

        return

    def update_next_start(self, now: t.Optional[datetime] = None):
        if not isinstance(now, datetime):
            now = datetime.now(tz=timezone.utc)

        try:
            crontab = CronTab(self.__option.cron)
            delay_sec = crontab.next(now)
        except Exception as e:
            print(f"update next start cron error : {e}")
            self.__next_start_at = None
            return

        self.__next_start_at = now + timedelta(seconds=delay_sec)

        return

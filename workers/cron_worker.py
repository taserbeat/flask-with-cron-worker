import time
import typing as t

from workers.cron_task import CronTask
from workers.cron_task_option import CronTaskOption


class CronWorker:
    def __init__(self, options: t.Union[CronTaskOption, t.List[CronTaskOption]] = []) -> None:
        """

        Args:
            options (t.Union[CronTaskOption, t.List[CronTaskOption]]): CronTaskOption or list of CronTaskOption
        """

        if isinstance(options, CronTaskOption):
            options = [options]

        self.__tasks = [CronTask(option) for option in options]
        self.__is_active = False

        return

    def start(self):
        """Start worker thread"""

        self.__is_active = True

        print("Start cron worker")

        self._loop()

        print("Stop cron worker")

        return

    def _loop(self):
        """The main loop to be executed on thread"""

        while self.__is_active:
            self._on_update()
            time.sleep(1)
            continue

        return

    def _on_update(self):
        """Called in each loop"""

        try:
            for task in self.__tasks:
                task.start()

                continue
        except Exception as e:
            print(f"start task error : {e}")

        for task in self.__tasks:
            task.update_next_start()

            continue

        return

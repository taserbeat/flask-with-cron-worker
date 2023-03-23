import typing as t


class CronTaskOption:
    """The option having CronTask config"""

    def __init__(self, task_name: str, command: str, cron: str, cwd: t.Optional[str] = None) -> None:
        """

        Args:
            task_name (str):Task name
            command (str): Command executed by task
            cron (str): Cron schedule expressions
            cwd (t.Optional[str], optional):
                The current directory where the task will be started.
                Both absolute and relative paths are allowed.
                The start position of relative path is the location where Python was executed.
        """

        self.__task_name = task_name
        self.__command = command
        self.__cron = cron
        self.__cwd = cwd if isinstance(cwd, str) else "."

        return

    @staticmethod
    def from_dict(data: t.Dict[str, str]):
        """Create new instance from dict"""

        if "TaskName" not in data:
            raise KeyError("'TaskName' key not found.")

        if "Command" not in data:
            raise KeyError("'Command' key not found.")

        if "Cron" not in data:
            raise KeyError("'Cron' key not found.")

        return CronTaskOption(
            task_name=data["TaskName"],
            command=data["Command"],
            cron=data["Cron"],
            cwd=data.get("Cwd")
        )

    @property
    def task_name(self):
        """Task name"""
        return self.__task_name

    @task_name.setter
    def task_name(self, value: str):
        self.__task_name = value
        return

    @property
    def command(self):
        """Command executed by task"""
        return self.__command

    @command.setter
    def command(self, value: str):
        self.__command = value
        return

    @property
    def cron(self):
        """Cron schedule expressions"""
        return self.__cron

    @cron.setter
    def cron(self, value: str):
        self.__cron = value
        return

    @property
    def cwd(self):
        """The current directory where the task will be started"""
        return self.__cwd

    @cwd.setter
    def cwd(self, value: str):
        self.__cwd = value
        return

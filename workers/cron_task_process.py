from datetime import datetime, timezone
from multiprocessing import Process
import typing as t


class CronTaskProcess(Process):

    def __init__(
            self, group=None, target=None, name: t.Optional[str] = None, args: t.Iterable[t.Any] = (),
            kwargs: t.Mapping[str, t.Any] = {}, *, daemon: t.Optional[bool] = None
    ) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)

        self.__started_at: t.Optional[datetime] = None
        self.__exited_at: t.Optional[datetime] = None

        return

    def start(self) -> None:
        if not self.is_alive() and self.__started_at is None:
            self.__started_at = datetime.now(tz=timezone.utc)

        return super().start()

    def kill(self) -> None:
        if self.__exited_at is None:
            self.__exited_at = datetime.now(tz=timezone.utc)

        return super().kill()

    @property
    def started_at(self):
        """開始時刻"""
        return self.__started_at

    @property
    def exited_at(self):
        """終了時刻"""
        return self.__exited_at

    @property
    def is_exited(self):
        """終了済みであるフラグ"""
        return not self.is_alive()

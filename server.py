from flask import Flask
from concurrent.futures import ThreadPoolExecutor

from workers.cron_worker import CronWorker
from workers.cron_task_option import CronTaskOption

service = Flask(__name__)


@service.route("/", defaults={"path": "/"}, methods=["GET"])
@service.route("/<path:path>")
def index(path):
    return "this is index\n"


if __name__ == "__main__":
    option1 = CronTaskOption.from_dict(
        {
            "TaskName": "SampleTask1",
            "Command": "echo Task1; pwd;",
            "Cron": "*/1 * * * *",
            "Cwd": "./settings",
        }
    )
    option2 = CronTaskOption.from_dict(
        {
            "TaskName": "SampleTask2",
            "Command": "echo Task2; pwd;",
            "Cron": "*/2 * * * *",
            "Cwd": "./tests",
        }
    )

    cron_worker = CronWorker(options=[option1, option2])

    with ThreadPoolExecutor(max_workers=1) as executor:
        executor.submit(cron_worker.start)
        service.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)

    exit(0)

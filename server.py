from flask import Flask
from concurrent.futures import ThreadPoolExecutor

from core.settings import AppSettings
from workers.cron_worker import CronWorker
from workers.cron_task_option import CronTaskOption

service = Flask(__name__)


@service.route("/", defaults={"path": "/"}, methods=["GET"])
@service.route("/<path:path>")
def index(path):
    return "this is index\n"


if __name__ == "__main__":
    settings = AppSettings().load_setting_file().load_environment()

    options = [CronTaskOption.from_dict(data) for data in settings.option_dicts]
    cron_worker = CronWorker(options=options)

    with ThreadPoolExecutor(max_workers=1) as executor:
        executor.submit(cron_worker.start)
        service.run(host=settings.host, port=settings.port, debug=settings.debug, use_reloader=False)

    exit(0)

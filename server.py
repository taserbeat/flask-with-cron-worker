from flask import Flask

service = Flask(__name__)


@service.route("/", defaults={"path": "/"}, methods=["GET"])
@service.route("/<path:path>")
def index(path):
    return "this is index\n"


if __name__ == "__main__":
    try:
        service.run(host="0.0.0.0", port=5000, debug=True)
    except Exception as e:
        print(f"service error : {e}")
        raise e

    exit(0)

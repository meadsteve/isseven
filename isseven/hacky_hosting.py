import os

from markdown import markdown


def get_homepage_html(root: str):
    with open(root + "/README.md") as readme:
        content = "\n".join(readme.readlines())
        host_url_from_env = os.environ.get("HOST_URL")
        host_env = os.environ.get("HOST")
        port_env = os.environ.get("PORT")
        if host_url_from_env:
            host_url = host_url_from_env
        elif host_env and port_env:
            host_url = f"http://{host_env}:{port_env}"
        else:
            host_url = "http://localhost:8000"
        content = content.replace("{{HOSTED_URL}}", host_url)
        homepage_html = markdown(content, extensions=["fenced_code"])
    return homepage_html

import os

from markdown import markdown


def get_homepage_html(root: str):
    with open(root + "/README.md") as readme:
        content = "\n".join(readme.readlines())
        host_url = (
            f"https://{os.environ['HEROKU_APP_NAME']}.herokuapp.com"
            if os.environ.get("HEROKU_APP_NAME")
            else "http://localhost:8000"
        )
        content = content.replace("{{HOSTED_URL}}", host_url)
        homepage_html = markdown(content, extensions=["fenced_code"])
    return homepage_html

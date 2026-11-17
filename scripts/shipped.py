"""Rewrite the 'Recently shipped' block of README.md from public GitHub activity."""
import json
import os
import re
import sys
import urllib.request
from datetime import datetime

USER = os.environ.get("GH_USER", "light691")
SKIP = {USER, f"{USER}.github.io", "bentaGo"}
LIMIT = 5
TOKEN = os.environ.get("GITHUB_TOKEN", "")


def api(path):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "profile-shipped"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request(f"https://api.github.com{path}", headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def day(iso):
    return datetime.fromisoformat(iso.replace("Z", "+00:00")).strftime("%b %d, %Y")


def lines():
    repos = api(f"/users/{USER}/repos?type=owner&sort=pushed&per_page=30")
    out = []
    for repo in repos:
        if repo["fork"] or repo["private"] or repo["archived"] or repo["name"] in SKIP:
            continue
        name, url = repo["name"], repo["html_url"]
        commits = api(f"/repos/{USER}/{name}/commits?per_page=1")
        if not commits:
            continue
        c = commits[0]
        msg = c["commit"]["message"].splitlines()[0].replace("[", "(").replace("]", ")")
        when = day(c["commit"]["committer"]["date"])
        rel = api(f"/repos/{USER}/{name}/releases?per_page=1")
        tag = f" · [{rel[0]['tag_name']}]({rel[0]['html_url']})" if rel else ""
        out.append(f"- **[{name}]({url})**{tag} · {when}: [{msg}]({c['html_url']})")
        if len(out) == LIMIT:
            break
    return out


def main(path="README.md"):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    block = "\n".join(lines())
    new = re.sub(
        r"(<!-- shipped:start -->\n).*?(<!-- shipped:end -->)",
        lambda m: f"{m.group(1)}{block}\n{m.group(2)}",
        text,
        flags=re.S,
    )
    if new != text:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(new)
        print("updated")
    else:
        print("no change")


if __name__ == "__main__":
    main(*sys.argv[1:])

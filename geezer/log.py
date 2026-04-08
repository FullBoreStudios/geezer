from rich import print as rprint


def prnt(message, emoji="", label="", *, force=False):
    if not force and not is_debug():
        return

    prefix = ""
    if emoji and label:
        prefix = f"[{emoji}\u2002{label}] "
    elif emoji:
        prefix = f"[{emoji}] "
    elif label:
        prefix = f"[{label}] "

    style = choose_style(label or emoji)
    rprint(f"[{style}]{prefix}[/]{message}")


def warn(message, label="", *, force=False):
    prnt(message, emoji="⚠️", label=label, force=force)


def is_debug():
    import os
    return os.environ.get("DJANGO_DEBUG", "True") == "True"


def choose_style(tag):
    if any(term in tag.lower() for term in ["error", "fail"]):
        return "bold red"
    if any(term in tag.lower() for term in ["success", "done"]):
        return "bold green"
    if any(term in tag.lower() for term in ["api", "external"]):
        return "bold cyan"
    if any(term in tag.lower() for term in ["checkout", "cart"]):
        return "bold magenta"
    if any(term in tag.lower() for term in ["timing"]):
        return "dim"
    return "white"

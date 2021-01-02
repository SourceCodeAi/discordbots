from dhooks import Webhook


def message(url, msg):
    hook = Webhook(url)
    hook.send(msg)

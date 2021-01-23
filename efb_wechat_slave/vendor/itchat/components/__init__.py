from .contact import load_contact
from .hotreload import load_hotreload
from .login import load_login
from .messages import load_messages
from .register import load_register
from .session import load_session


def load_components(core):
    load_contact(core)
    load_hotreload(core)
    load_login(core)
    load_messages(core)
    load_register(core)
    load_session(core)

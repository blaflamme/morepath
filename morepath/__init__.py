# flake8: noqa
"""This is the main public API of Morepath.

Additional public APIs can be imported from the :mod:`morepath.error`
and :mod:`morepath.pdbsupport` modules. For custom directive
implementations that interact with core directives for grouping or
subclassing purposes you may need to import from
:mod:`morepath.directive`.

The other submodules are considered private. If you find yourself
needing to import from them in application or extension code, please
report an issue about it on the Morepath issue tracker.
"""

from dectate import commit, autocommit
from .app import App
from .implicit import enable_implicit, disable_implicit
from .core import (excview_tween_factory as EXCVIEW,
                   model_predicate, name_predicate, request_method_predicate,
                   body_model_predicate)
from .core import body_model_predicate as LAST_VIEW_PREDICATE
from . import directive  # register directive methods
from .generic import remember_identity, forget_identity, settings
from .view import render_json, render_html
from .request import Request, Response
from .view import redirect
from .autosetup import scan, autoscan, autosetup
from .security import Identity, IdentityPolicy, NO_IDENTITY
from .converter import Converter
from .reify import reify
from .run import run

from reg import implicit

implicit.initialize(None)
enable_implicit()

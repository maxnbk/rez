# Deferred setting value: the Deferred-wrapped callable is resolved at first
# access of the setting, after config file evaluation has completed, so it may
# use rez APIs (here: canonical_path) and read sidecar data files.
import json
import os

import rez.utils.filesystem as _fs

_repos_json = os.path.join(
    os.path.dirname(__file__), "deferred_callable_repos.json"
)

default_cachable_per_repository = Deferred(lambda: {
    _fs.canonical_path(path): value
    for path, value in json.load(open(_repos_json)).items()
})

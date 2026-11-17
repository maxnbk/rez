# Raw (non-canonical) paths as keys - rez canonicalises the keys itself,
# so there is no need (and it is an error) to call canonical_path here.
default_cachable_per_repository = {
    "/mnt/./repo/": True,
    "/mnt/other": False,
}

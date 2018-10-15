# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

"""This test does sanity checks on Spack's builtin package database."""
import re

import pytest

import spack.paths
import spack.repo
import spack.fetch_strategy


def check_repo():
    """Get all packages in the builtin repo to make sure they work."""
    for name in spack.repo.all_package_names():
        spack.repo.get(name)


@pytest.mark.maybeslow
def test_get_all_packages():
    """Get all packages once and make sure that works."""
    check_repo()


def test_get_all_mock_packages():
    """Get the mock packages once each too."""
    db = spack.repo.RepoPath(spack.paths.mock_packages_path)
    with spack.repo.swap(db):
        check_repo()


def test_all_versions_are_lowercase():
    """Spack package names must be lowercase, and use `-` instead of `_`."""
    errors = []
    for name in spack.repo.all_package_names():
        if re.search(r'[_A-Z]', name):
            errors.append(name)

    assert len(errors) == 0


def test_all_virtual_packages_have_default_providers():
    """All virtual packages must have a default provider explicitly set."""
    defaults = spack.config.get('packages', scope='defaults')
    default_providers = defaults['all']['providers']
    providers = spack.repo.path.provider_index.providers

    for provider in providers:
        assert provider in default_providers


def test_package_version_consistency():
    """Make sure all versions on builtin packages can produce a fetcher."""
    for name in spack.repo.all_package_names():
        pkg = spack.repo.get(name)
        spack.fetch_strategy.check_pkg_attributes(pkg)
        for version in pkg.versions:
            assert spack.fetch_strategy.for_package_version(pkg, version)

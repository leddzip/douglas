set -eu

#==========================================================
# Modify the version in the different files with the
# version given in parameter or the script.
#
# Currently the locations that contains the version are:
#   - pyproject.toml (project file for poetry)
#   - douglas_securty_manager/__init__.py
#   - tests/test_douglas_security_manager.py
#
# Script PARAMS:
#   $1: the new version to set in the different file that
#       contains a version reference
#
# Return/print:
#   Nothing
#
#==========================================================

new_version="$1"

#-------------------------------
# update the version inside pyproject.toml
#
# Params:
#   $1: the new version to inject
#
function update-pyproject-toml() {
  sed -i "0,/version = ".*"/{s/version = ".*"/version = \"$1\"/}" pyproject.toml
}

#-------------------------------
# update the version inside
# douglas_security_manager/__init__.py
#
# Params:
#   $1: the new version to inject
#
function update-init-py() {
  echo "__version__ = '$1'" > douglas_securty_manager/__init__.py

}

#-------------------------------
# update the version inside
# tests/test_douglas_security_manager.py
#
# Params:
#   $1: the new version to inject
#
function update-test() {
  sed -i "0,/assert __version__ == '.*'/{s/assert __version__ == '.*'/assert __version__ == '$1'/}" tests/test_douglas_security_manager.py
}


update-pyproject-toml "$new_version"
update-init-py "$new_version"
update-test "$new_version"

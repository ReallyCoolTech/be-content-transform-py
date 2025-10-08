# Copyright (C) 2025 ReallyCool Technologies, LLC
#
# This file is part of be-content-transform-py.
#
# be-content-transform-py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# be-content-transform-py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with be-content-transform-py.  If not, see <https://www.gnu.org/licenses/>.

import typer
from typer.testing import CliRunner

import contra
from contra.cli import app

from . import __version__, __version_info__

runner = CliRunner()


def test_version():
	assert contra.__version__ == __version__

def test_version_info():
	assert contra.__version_info__ == __version_info__

def test_app_no_command():
	result = runner.invoke(app)
	assert result.exit_code == 2

def test_app_version():
	result = runner.invoke(app, ["version"])
	assert result.exit_code == 0
	assert f"{__version__}" in result.output

def test_app_semver():
	result = runner.invoke(app, ["semver"])
	assert result.exit_code == 0
	assert f"{repr(__version_info__)}" in result.output

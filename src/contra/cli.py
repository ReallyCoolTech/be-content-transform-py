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

import os
from typing import Optional

import semver
import typer

from . import __version__, __version_info__

app = typer.Typer(no_args_is_help=True)


@app.command()
def version() -> str:
	print(f"{__version__}")
	raise typer.Exit()

@app.command()
def semver() -> str:
	print(f"{repr(__version_info__)}")
	raise typer.Exit()


if __name__ == "__main__":
	app()

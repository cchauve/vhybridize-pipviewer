#  Copyright (C) 2006-2007 Free Software Foundation

#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
try:
    from ez_setup import use_setuptools
    use_setuptools()
except ImportError:
    # there is no ez_setup if setup tools is installed with apt, among
    # other things
    pass

try:
    from setuptools import setup, find_packages
except ImportError:
    print "You don't have setuptools installed.  Put ez_setup.py"
    print "in the same directory as setup.py (this script) and try again."
    print "You can get it here:"
    print "  http://peak.telecommunity.com/dist/ez_setup.py"
    sys.exit(1)

from pipviewer import __version__, NAME

entry_points="""

[console_scripts]

pipviewer = pipviewer.viewer_app:main
pippacker = pipviewer.scripts.pippacker:main

"""

setup(name=NAME,
      version=__version__,
      url="http://cgl.bioinfo.uqam.ca",
      maintainer="Yannick Gingras",
      maintainer_email="ygingras@ygingras.net",
      packages=find_packages(exclude=['ez_setup']),
      package_data={'docs': ['*.html'],
                    'pipviewer': ['*.html']},
      include_package_data=True,
      scripts=[],
      zip_safe=False,
      
      install_requires=["OpenGL>=2.0",
                        # easy_install can't resolve PyQt
                        # "PyQt>=3.11", 
                        "vhybridize>=0.5.9"],

      license="GPLv3 or later",
      description="graphically display conservation on a multiple alignment",
      entry_points=entry_points,
      )

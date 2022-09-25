from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

# we get the python stubs create by stubgenj
ALL_PYI = [('*/' * depth) + '*.pyi' for depth in range(0, 10)]

setup(
    name="vassal-python",  # Required
    version="0.4.2",  # Required
    description="Python tools for manipulating VASSAL modules",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url="https://github.com/jasonestewart/vassal-python",  # Optional
    author="Jason E. Stewart",  # Optional
    author_email="jason.e.stewart@gmail.com",  # Optional
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development :: Libraries :: Java Libraries",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="VASSAL module development",  # Optional
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=["vassal-python", "VASSAL-stubs", "jars", "java-stubs"],
    package_dir={"vassal-python": "src/python",
                 "jars": "lib/java",
                 "VASSAL-stubs": "lib/python/VASSAL-stubs",
                 "java-stubs": "lib/python/java-stubs",
                 "jpype-stubs": "lib/python/jpype-stubs",
                 },
    package_data={'VASSAL-stubs': ALL_PYI,
                  'java-stubs': ALL_PYI,
                  'jpype-stubs': ALL_PYI,
                  'jars': ['Vengine.jar', 'VASSAL/tools/python/Helper.class'],
                  },
    include_package_data=True,
    # Specify which Python versions you support. In contrast to the
    # 'Programming Language' classifiers above, 'pip install' will check this
    # and refuse to install the project if the version does not match. See
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
    python_requires=">=3.7, <4",
    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/discussions/install-requires-vs-requirements/
    install_requires=["jpype1>=1.2.1,<2.*"],  # Optional
    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    extras_require={  # Optional
        "dev": ["numpy",
                "pillow",
                "opencv-python",
                "pytesseract"],
    },
    # If there are data files included in your packages that need to be
    # installed, specify them here.
    # package_data={  # Optional
    #     "sample": ["package_data.dat"],
    # },
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    # entry_points={  # Optional
    #     "console_scripts": [
    #         "sample=sample:main",
    #     ],
    # },
    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    project_urls={  # Optional
        "Bug Reports": "https://github.com/jasonestewart/vassal-python/issues",
        "Say Thanks!": "https://saythanks.io/to/jasonestewart",
        "Source": "https://github.com/jasonestewart/vassal-python/",
    },
)
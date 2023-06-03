import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

__version__ = '0.0.0'

REPO_NAME = 'text-summarizer'
AUTHOR_NAME = 'jaikushwaha7'
SRC_REPO = 'text-summarizer'
AUTHOR_EMAIL = 'jaikushwaha7@gmail.com'

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description='a small python package for NLP app Text Summarizer',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/' + AUTHOR_NAME + '/' + SRC_REPO,
    project_urls={
        "Bug Tracker": "https://github.com/" + AUTHOR_NAME + '/' + SRC_REPO + '/issues',
    },
    package_dir= {'': 'src'},
    packages=setuptools.find_packages(where='src')
)
    
import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = 'text_summarizer'
AUTHOR_USER_NAME = 'sdoshi89'
SRC_REPO = 'textSummarizer'
AUTHOR_EMAIL = 'doshisaumilm@gmail.com'

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sdoshi89/textSummarizer",
    project_urls={
        "Bug Tracker": "https://github.com/sdoshi89/textSummarizer/issues",
    },
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src')
)

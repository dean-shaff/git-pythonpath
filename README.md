## git-pythonpath

A little project for adding git repos to the python path temporarily.

### Installation

```bash
/path/to/git-pythonpath/$> python setup.py
```

### Usage

```python
from git-pythonpath import append_git_repo
repo = "https://github.com/dean-shaff/pyro4tunneling.git"
with append_git_repo(repo):
    import pyro4tunneling

```

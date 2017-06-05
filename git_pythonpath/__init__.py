"""
git-pythonpath

Include remote git repository (temporarily) in python path.
"""
import sys
import os
import shutil
import subprocess
import shlex
from contextlib import contextmanager

home_dir = os.path.expanduser("~")
INCLUDE_PATH = os.path.join(home_dir, ".git-pythonpath")


def cleanup():
    """
    Clean up repos in the INCLUDE_PATH,
    remove INCLUDE_PATH from system path
    """
    for path in os.listdir(INCLUDE_PATH):
        full_path = os.path.join(INCLUDE_PATH, path)
        shutil.rmtree(full_path)
    if INCLUDE_PATH in sys.path:
        sys.path.remove(INCLUDE_PATH)

@contextmanager
def append_git_repo(git_repo):
    """
    Append a git repo to the system path
    Args:
        -git_repo (str): The name of the remote git_repo
    """
    if not os.path.exists(INCLUDE_PATH):
        os.mkdir(INCLUDE_PATH)
    sys.path.append(INCLUDE_PATH)
    repo_name = git_repo.split("/")[-1].replace(".git","")
    if os.path.exists(os.path.join(INCLUDE_PATH, repo_name)):
        pass
    else:
        cmd = "git clone {} {}".format(git_repo, os.path.join(INCLUDE_PATH, repo_name))
        cmd_list = shlex.split(cmd)
        clone_proc = subprocess.Popen(cmd_list, shell=False,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)
        clone_proc.wait()
    yield
    cleanup()


if __name__ == '__main__':
    url1 = "https://github.com/dean-shaff/pyro4tunneling.git"
    url2 = "git@github.com:dean-shaff/pyro4tunneling.git"
    with append_git_repo(url1):
        import pyro4tunneling
    print(pyro4tunneling.TUNNELING_LOGGER)

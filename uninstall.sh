# Get the location of the egg file
INIT_FILE=`python -c "import git_pythonpath; print(git_pythonpath.__file__)"`
MODULE_VERSION=`python -c "import git_pythonpath; print(git_pythonpath.__version__)"`

if [[ $INIT_FILE == "git_pythonpath/__init__.pyc" ]]; then
	if [[ `pwd` != $HOME ]]; then
		cd $HOME # Hope it's not installed in home directory
	else
		cd .. # Less ideal is moving into some random directory
	fi
	INIT_FILE=`python -c "import git_pythonpath; print(git_pythonpath.__file__)"`
fi
# Do one final check to make sure we actually have the egg file
if [[ $INIT_FILE == *"git_pythonpath-$MODULE_VERSION-py2.7.egg"* ]]; then
	echo "Removing egg file"
	MODULE_EGG=$(dirname "$INIT_FILE")
	MODULE_EGG=$(dirname "$MODULE_EGG")
	rm $MODULE_EGG
else
	echo "Couldn't safely remove package"
	echo "Look for .egg files in output of the following command"
	echo "python setup.py install --record"
fi

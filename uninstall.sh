# Get the location of the egg file
INIT_FILE=`python -c "import git_pythonpath; print(git_pythonpath.__file__)"`
echo $INIT_FILE

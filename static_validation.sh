echo 'Running black'
black -l 120 -S --check . || exit 1
echo 'black produced no errors.'

echo 'Running isort'
isort --profile black --check-only . || exit 1
echo 'isort produced no errors.'

echo 'Running bandit'
bandit -x "./venv" -r . || exit 1

echo 'Static validation finished without errors.'
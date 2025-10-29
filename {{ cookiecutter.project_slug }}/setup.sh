uv sync
git init
git config user.name "{{ cookiecutter.author_name }}" 
git config user.email "{{ cookiecutter.email }}"
git add tests .gitignore pyproject.toml README.md setup.sh config .github
git commit -m "first commit"
git branch -M main
uv run pre-commit install

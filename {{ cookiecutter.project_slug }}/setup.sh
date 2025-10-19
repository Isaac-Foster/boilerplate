uv sync
git init
git config user.name "{{ cookiecutter.author_name }}" 
git config user.email "{{ cookiecutter.email }}"
uv run pre-commit install

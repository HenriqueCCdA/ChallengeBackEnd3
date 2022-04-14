# ChallengeBackEnd3

## Desenvoldor

```console
python -m venv .venv --upgrade-deps
source .venv/bin/activate
pip install -r requirements-dev.txt
```

Rodando os testes

```console
pytest
```

## Novas dependencias

```console
pip-compile --generate-hashes requirements.in
pip-compile --generate-hashes requirements-dev.in
```
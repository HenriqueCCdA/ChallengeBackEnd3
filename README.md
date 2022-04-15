# ChallengeBackEnd3

![](https://img.shields.io/github/last-commit/HenriqueCCdA/ChallengeBackEnd3?style=plasti&ccolor=blue)
![](https://img.shields.io/badge/Autor-Henrique%20C%20C%20de%20Andrade-blue)
[![Django CI](https://github.com/HenriqueCCdA/ChallengeBackEnd3/actions/workflows/ga.yml/badge.svg?branch=main)](https://github.com/HenriqueCCdA/ChallengeBackEnd3/actions/workflows/ga.yml)
[![codecov](https://codecov.io/gh/HenriqueCCdA/ChallengeBackEnd3/branch/main/graph/badge.svg?token=BBBZNJBJ1P)](https://codecov.io/gh/HenriqueCCdA/ChallengeBackEnd3)


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

# mini-api

![CI](https://github.com/oulhamidmed-design/mini-api/actions/workflows/ci.yml/badge.svg)

Une mini API Python (FastAPI) qui expose de petits outils : maths, texte, conversions et validations. Projet noté du module Git et GitHub.

## Installation

```bash
git clone https://github.com/oulhamidmed-design/mini-api.git
cd mini-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Lancement

### En local

```bash
uvicorn app.main:app --reload
```

L'API écoute sur http://localhost:8000. La documentation interactive est sur http://localhost:8000/docs.

### Avec Docker

```bash
docker build -t mini-api .
docker run -p 8000:8000 mini-api
```

Ou avec l'image publiée sur ghcr.io (après le tag `v1.0.0`) :

```bash
docker run -p 8000:8000 ghcr.io/oulhamidmed-design/mini-api:v1.0.0
```

## Utilisation

| Module | Route | Exemple |
|---|---|---|
| santé | `GET /sante` | `/sante` |
| math | `GET /factorielle/{n}` | `/factorielle/5` |
| math | `GET /premier/{n}` | `/premier/7` |
| math | `GET /pgcd/{a}/{b}` | `/pgcd/12/18` |
| texte | `GET /palindrome/{texte}` | `/palindrome/Radar` |
| texte | `GET /voyelles/{texte}` | `/voyelles/Bonjour` |
| texte | `GET /inverser/{texte}` | `/inverser/abc` |
| conversion | `GET /celsius/{valeur}` | `/celsius/100` |
| conversion | `GET /km-miles/{km}` | `/km-miles/10` |
| conversion | `GET /euros/{montant}/{devise}` | `/euros/100/USD` |
| validation | `GET /email/{email}` | `/email/lea@mail.fr` |
| validation | `GET /mot-de-passe/{mdp}` | `/mot-de-passe/Motdepasse1!` |
| validation | `GET /code-postal/{cp}` | `/code-postal/75001` |

Exemple :

```bash
curl http://localhost:8000/factorielle/5
# {"n":5,"resultat":120}
```

Une entrée invalide renvoie une erreur **400** avec un message :

```bash
curl -i http://localhost:8000/factorielle/-1
# HTTP/1.1 400 Bad Request
# {"detail":"n doit être positif"}
```

Notes : les taux de `/euros` sont fixes et indicatifs (USD, GBP, JPY, CHF). Un mot de passe ne doit jamais être envoyé dans une URL en vrai projet : la route `/mot-de-passe` sert uniquement d'exercice.

## Tests

```bash
pytest -v                          # lancer les tests
pytest --cov=app --cov-report=term # avec la couverture (80 % minimum)
ruff check .                       # vérifier le style
```

## Contribuer

1. Créer une issue qui décrit la tâche.
2. Partir d'un `main` à jour et créer une branche `type/numéro-description` (par exemple `feat/12-factorielle`).
3. Faire des commits atomiques au format Conventional Commits (`feat(math): ajoute factorielle`).
4. Ouvrir une pull request vers `main` avec `Closes #numéro` : la CI doit être verte.
5. Après relecture et approbation, fusionner puis supprimer la branche.

## Équipe

| Membre | Contribution |
|---|---|
| @oulhamidmed-design | Projet réalisé seul : modules math, texte, conversion et validation, CI/CD, Docker, documentation |

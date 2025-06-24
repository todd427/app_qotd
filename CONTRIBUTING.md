# Contributing to QOTD App

Thank you for your interest in contributing!

This project is a simple Django-based QOTD (Quote of the Day) app with REST API, review interface, and import tools.

---

## How to contribute:

✅ Check open Issues — especially any marked `good first issue` or `enhancement`

✅ Fork this repo → create a feature branch → submit a pull request (PR)

✅ Please follow the existing coding style (simple, Django 4.2 + DRF)

✅ Update CHANGELOG.md if your change is user-visible

✅ All contributions are welcome — issues, features, documentation, testing

---

## Development quick start:

```bash
git clone git@github.com:todd427/app_qotd.git
cd app_qotd
python -m venv envQ
source envQ/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

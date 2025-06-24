🚀 You got it — here is a nice `README.md` for your **QOTD app** — you can paste this directly:

---

````markdown
# QOTD — Quote of the Day App

A Django-based Quote of the Day app — with API, admin review, bulk import, and human-curated approval system.

Built by **Todd McCaffrey** 🚀

---

## Features

✅ REST API — `/qotd/api/random/`  
✅ Human-curated review page — `/qotd/review/`  
✅ Admin interface  
✅ Bulk import quotes from JSON  
✅ Approve / Unapprove all  
✅ Author-friendly, reusable app  
✅ Built for: *MSc Cyberpsychology Dissertation Project* 🚀

---

## Quick Start

```bash
git clone git@github.com:todd427/app_qotd.git
cd app_qotd
python -m venv envQ
source envQ/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py import_quotes my_quotes.json
python manage.py runserver
````

Then:

* View API: [http://127.0.0.1:8000/qotd/api/random/](http://127.0.0.1:8000/qotd/api/random/)
* Review page: [http://127.0.0.1:8000/qotd/review/](http://127.0.0.1:8000/qotd/review/)
* Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Importing Quotes

```bash
python manage.py import_quotes my_quotes.json
```

---

## Approving Quotes

```bash
python manage.py approve_all_quotes
python manage.py unapprove_all_quotes
```

---

## Author

**Todd McCaffrey**
[https://toddmccaffrey.com](https://toddmccaffrey.com)

---

## License

MIT License — see LICENSE file.

---

*Built with Django + DRF + human creativity — part of MSc Cyberpsychology Dissertation project.* 🚀

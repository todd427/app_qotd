
# QOTD App — Documentation

---

## Overview

This Django app provides a human-curated **Quote of the Day** (QOTD) system with:

✅ REST API  
✅ Review and approval interface  
✅ Admin tools  
✅ Bulk import  
✅ Approve / Unapprove

---

## API URLs

| URL | Description |
|-----|-------------|
| `/qotd/api/random/` | Get a random approved quote (JSON) |

Example response:

```json
{
    "text": "Every story starts with one thing: the decision to tell it.",
    "author": "Todd McCaffrey",
    "url": "https://toddmccaffrey.com",
    "source": "Personal Notes",
    "created_at": "2025-06-24T10:00:00Z"
}
```

---

## Review and Admin URLs

| URL | Description |
|-----|-------------|
| `/qotd/review/` | Review quotes (paginated) |
| `/qotd/review/edit/<quote_id>/` | Edit a quote |
| `/qotd/review/approve_all/` | Approve all quotes (POST) |
| `/qotd/review/unapprove_all/` | Unapprove all quotes (POST) |

---

## Django Admin

| URL | Description |
|-----|-------------|
| `/admin/` | Django admin panel |
| `/admin/qotd/quote/` | Manage quotes in admin |

---

## Management Commands

```bash
python manage.py import_quotes my_quotes.json
python manage.py approve_all_quotes
python manage.py unapprove_all_quotes
```

---

## Planned Features (v0.2)

- API filter by author: `/qotd/api/random/?author=name`
- API list endpoint: `/qotd/api/list/`
- API filter by tag (after tagging added)
- Landing page: `/qotd/`

---

## Author

Todd McCaffrey  
[https://github.com/todd427/app_qotd](https://github.com/todd427/app_qotd)

---

## License

MIT License — see LICENSE file.

# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to design and build a simple RESTful API using the FastAPI framework. Students will implement basic CRUD endpoints, use Pydantic models for validation, and run the API locally with Uvicorn.

## 📝 Tasks

### 🛠️ Create a simple items API

#### Description
Implement a small REST API to manage a collection of items. Each item should have an id, name, description, and price. The API will support creating, listing, retrieving, updating, and deleting items.

#### Requirements
Completed program should:

- Use FastAPI and Pydantic models for data validation.
- Provide endpoints: GET /items, POST /items, GET /items/{item_id}, PUT /items/{item_id}, DELETE /items/{item_id}.
- Use an in-memory store (Python dict) for items — persistence not required.
- Return appropriate HTTP status codes and JSON responses.
- Include clear docstrings and comments explaining the code.

### 🛠️ Add input validation and error handling

#### Description
Add validation for required fields and handle common error cases (missing item, invalid payload).

#### Requirements
Completed program should:

- Use Pydantic to validate incoming request bodies.
- Return 404 when an item is not found.
- Return 400 for invalid requests (FastAPI will handle many cases via Pydantic automatically).

### Optional: Add filtering or search

#### Description
Add a query parameter to filter items by name or price range.

#### Requirements
Completed program should:

- Support optional query params on GET /items (e.g., ?name=cat or ?min_price=5&max_price=20).
- Return matching items when filters are provided.

---

## Starter files

- `starter-code.py` — Minimal FastAPI app with example endpoints to get you started.
- `requirements.txt` — Packages required to run the starter app.

## Running the app (local)

1. Create a virtual environment and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
uvicorn starter-code:app --reload --port 8000
```

4. Open docs at: http://127.0.0.1:8000/docs

## Deliverable

Push the completed assignment folder containing `README.md` and your final `starter-code.py` (if modified). Include short notes in the README about what you changed and any known limitations.

.PHONY: dev prod test lint clean logs shell-backend neo4j-browser

dev:
	docker compose up --build

prod:
	docker compose -f docker-compose.prod.yml up -d

test:
	cd backend && poetry run pytest tests/ -v --cov=app --cov-report=term-missing

lint:
	cd backend && poetry run ruff check app/ tests/

clean:
	docker compose down -v
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null; true

logs:
	docker compose logs -f backend

shell-backend:
	docker compose exec backend bash

neo4j-browser:
	xdg-open http://localhost:7474

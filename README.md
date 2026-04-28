# AgentForge

AgentForge is a self-healing multi-agent coding assistant. It plans tasks, generates code, executes it in a sandbox, and auto-debugs failures using a LangGraph-driven loop.

## Stack
- Backend: Python 3.11, FastAPI, asyncio
- Orchestration: LangGraph, LangChain
- AI: Gemini 2.5 Flash (Google AI Studio)
- Observability: LangSmith
- Graph DB: Neo4j
- Realtime: WebSocket (FastAPI)
- Frontend: Next.js 14, TypeScript, Tailwind, shadcn/ui
- Deploy: AWS EC2, ECR, GitHub Actions

## Repo Layout
- backend: FastAPI app, agents, graph, and integrations
- frontend: Next.js dashboard
- infra: AWS scripts and configs
- .github/workflows: CI and deploy pipelines

## Local Development
1. Copy env templates and fill secrets
   - .env.example -> .env
   - backend/.env.example -> backend/.env
   - frontend/.env.example -> frontend/.env
2. Start services
   - make dev
3. Validate
   - GET http://localhost:8000/api/v1/health
   - http://localhost:7474 (Neo4j browser)
   - http://localhost:3000 (frontend)

## Tests
- Backend: make test
- Lint: make lint

## Deployment
- Configure AWS secrets in GitHub
- Push to main to trigger deploy workflow

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-b from-graphite via-ink to-graphite px-6 py-16">
      <div className="mx-auto max-w-4xl">
        <p className="text-sm uppercase tracking-[0.3em] text-mint">AgentForge</p>
        <h1 className="mt-4 text-4xl font-display tracking-tight text-white sm:text-6xl">
          Self-healing multi-agent coding assistant
        </h1>
        <p className="mt-6 text-lg text-fog">
          Planner, coder, executor, and debugger agents collaborating with live
          streaming into a terminal-style dashboard.
        </p>
        <div className="mt-10 grid gap-4 sm:grid-cols-2">
          <div className="rounded-2xl border border-white/10 bg-white/5 p-6">
            <h2 className="text-xl font-display text-white">Backend</h2>
            <p className="mt-2 text-sm text-fog">
              FastAPI, LangGraph, Neo4j, and Gemini powering autonomous code runs.
            </p>
          </div>
          <div className="rounded-2xl border border-white/10 bg-white/5 p-6">
            <h2 className="text-xl font-display text-white">Frontend</h2>
            <p className="mt-2 text-sm text-fog">
              Next.js dashboard streaming agent events over WebSocket.
            </p>
          </div>
        </div>
      </div>
    </main>
  );
}

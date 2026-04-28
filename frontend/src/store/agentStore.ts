import { create } from "zustand";

type AgentState = {
  lastEvent: string | null;
  setLastEvent: (event: string) => void;
};

export const useAgentStore = create<AgentState>((set) => ({
  lastEvent: null,
  setLastEvent: (event) => set({ lastEvent: event })
}));

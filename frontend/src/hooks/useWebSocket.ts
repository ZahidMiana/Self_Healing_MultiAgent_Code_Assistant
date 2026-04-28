import { useEffect } from "react";
import { useAgentStore } from "../store/agentStore";

export const useWebSocket = (url: string) => {
  const setLastEvent = useAgentStore((state) => state.setLastEvent);

  useEffect(() => {
    const socket = new WebSocket(url);

    socket.onmessage = (event) => {
      setLastEvent(event.data);
    };

    return () => {
      socket.close();
    };
  }, [url, setLastEvent]);
};

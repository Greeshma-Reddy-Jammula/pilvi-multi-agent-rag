import React, { useState } from "react";

type Message = {
  sender: string;
  text: string;
};

export default function ChatBox() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    const newMsg: Message = { sender: "User", text: input };
    setMessages([...messages, newMsg]);

    const res = await fetch(`http://localhost:8000/orchestrate/?task=${input}`, {
      method: "POST"
    });
    const data = await res.json();

    setMessages(prev => [
      ...prev,
      { sender: "Planner", text: data.plan },
      { sender: "Executor", text: data.result }
    ]);
    setInput("");
  };

  return (
    <div>
      <h2>AI Chat</h2>
      <div>
        {messages.map((msg, idx) => (
          <p key={idx}><b>{msg.sender}:</b> {msg.text}</p>
        ))}
      </div>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask AI..."
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

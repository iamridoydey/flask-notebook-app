import { useEffect, useState } from "react";
import NotebookInput from "./NotebookInput";
import NotebookItem from "./NotebookItem";

interface Note {
  id: number;
  note: string;
  completed: boolean;
}

const Notebooks = () => {
  const API_URL = import.meta.env.VITE_BACKEND_URI;
  console.log(API_URL);

  const [notes, setNotes] = useState<Note[]>([]);
  const [input, setInput] = useState("");

  // Fetch notes from backend once on mount
  useEffect(() => {
    fetch(`${API_URL}/notes`)
      .then((res) => res.json())
      .then((data) =>
        setNotes(
          data.map((n: any) => ({ ...n, completed: n.completed ?? false }))
        )
      );
  }, [API_URL]);

  // Add note via backend
  const addNote = () => {
    if (input.trim() === "") return;

    fetch(`${API_URL}/notes`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ note: input }),
    })
      .then((res) => res.json())
      .then((newNote) => {
        setNotes([...notes, newNote]);
        setInput("");
      });
  };

  // Delete note via backend
  const removeNote = (id: number) => {
    fetch(`${API_URL}/notes/${id}`, { method: "DELETE" }).then(() => {
      setNotes(notes.filter((note) => note.id !== id));
    });
  };

  const toggleNote = (id: number, completed: boolean) => {
    fetch(`${API_URL}/notes/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ completed: !completed }),
    })
      .then((res) => res.json())
      .then(() => {
        setNotes(
          notes.map((note) =>
            note.id === id ? { ...note, completed: !note.completed } : note
          )
        );
      });
  };

  return (
    <div className="max-w-md mx-auto mt-6">
      <NotebookInput value={input} onChange={setInput} onAdd={addNote} />
      <ul className="space-y-2">
        {notes.map((note) => (
          <NotebookItem
            key={note.id}
            note={note.note}
            completed={note.completed}
            onToggle={() => toggleNote(note.id, note.completed)}
            onRemove={() => removeNote(note.id)}
          />
        ))}
      </ul>
    </div>
  );
};

export default Notebooks;

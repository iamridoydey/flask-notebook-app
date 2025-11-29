import React from "react";

interface NotebookInputProps {
  value: string;
  onChange: (val: string) => void;
  onAdd: () => void;
}

const NotebookInput: React.FC<NotebookInputProps> = ({ value, onChange, onAdd }) => {
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault(); // prevent page reload
    onAdd();
  };

  return (
    <form onSubmit={handleSubmit} className="flex gap-2 mb-4">
      <input
        type="text"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder="Write your next task..."
        className="flex-1 border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500"
      />
      <button
        type="submit"
        className="bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-700 cursor-pointer"
      >
        Add
      </button>
    </form>
  );
};

export default NotebookInput;

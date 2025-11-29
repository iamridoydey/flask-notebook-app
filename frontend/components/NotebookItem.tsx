import React from "react";

interface NotebookItemProps {
  note: string;
  completed: boolean;
  onToggle: () => void;
  onRemove: () => void;
}

const NotebookItem: React.FC<NotebookItemProps> = ({ note, completed, onToggle, onRemove }) => {
  return (
    <li className="flex justify-between items-center bg-gray-100 px-3 py-2 rounded-lg shadow-sm">
      <div className="flex items-center gap-2">
        <input
          type="checkbox"
          checked={completed ?? false}
          onChange={onToggle}
          className="h-4 w-4 text-indigo-600 focus:ring-indigo-500 rounded cursor-pointer"
        />
        <span className={completed ? "line-through text-gray-400" : "text-gray-800"}>
          {note}
        </span>
      </div>
      <button
        onClick={onRemove}
        className="text-red-500 hover:text-red-700 text-sm font-medium cursor-pointer"
      >
        Remove
      </button>
    </li>
  );
};

export default NotebookItem;

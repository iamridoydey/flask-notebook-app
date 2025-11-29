import "./App.css";
import Header from "../components/Header";
import Notebooks from "../components/Notebooks";

function App() {
  return (
    <div className="min-h-screen animated-bg text-gray-100 flex flex-col">
      {/* Header */}
      <Header />

      {/* Main content */}
      <main className="flex-1 lg:mx-8 px-4 py-6">
        <div className="max-w-4xl mx-auto bg-gray-900/70 backdrop-blur-md shadow-xl rounded-lg p-6 border border-gray-700">
          <Notebooks />
        </div>
      </main>

      {/* Footer */}
      <footer className="border-t border-gray-700 py-4 text-center text-sm text-gray-400">
        © {new Date().getFullYear()} Flask Notebook App
      </footer>
    </div>
  );
}

export default App;

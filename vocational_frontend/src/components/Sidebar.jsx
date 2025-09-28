import React from "react"

export default function Sidebar({ setView, view }) {
  const links = [
    { id: "users", label: "👥 Usuarios" },
    { id: "instituciones", label: "🏫 Instituciones" },
    { id: "tests", label: "📝 Tests vocacionales" },
    { id: "notificaciones", label: "🔔 Notificaciones" },
    { id: "videollamadas", label: "🎥 Videollamadas" },
    { id: "profile", label: "🙍‍♂️ Perfil" },
    { id: "settings", label: "⚙️ Configuración" },
  ]

  return (
    <aside className="w-64 bg-gray-900 text-white h-screen flex flex-col">
      {/* Logo + nombre */}
      <div className="flex items-center gap-3 px-4 py-5 border-b border-gray-700">
        <img 
          src="https://cdn-icons-png.flaticon.com/512/535/535239.png" 
          alt="Brújula"
          className="w-8 h-8"
        />
        <span className="text-lg font-bold">Tu Ruta</span>
      </div>

      {/* Links */}
      <nav className="flex flex-col gap-1 mt-4 px-2">
        {links.map(link => (
          <button
            key={link.id}
            onClick={() => setView(link.id)}
            className={`text-left px-3 py-2 rounded transition ${
              view === link.id 
                ? "bg-blue-600 font-semibold" 
                : "hover:bg-gray-700"
            }`}
          >
            {link.label}
          </button>
        ))}
      </nav>
    </aside>
  )
}

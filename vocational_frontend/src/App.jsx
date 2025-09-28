import React, { useState } from "react"
import Landing from "./components/landing"
import Login from "./components/Login"
import Navbar from "./components/Navbar"
import Sidebar from "./components/Sidebar"
import Users from "./components/Users"
import InstitucionesPage from "./components/Instituciones/InstitucionesPage"


export default function App() {
  const [step, setStep] = useState("landing") // landing | login | app
  const [token, setToken] = useState(null)
  const [refresh, setRefresh] = useState(null)
  const [me, setMe] = useState(null)
  const [view, setView] = useState("users")

  if (step === "landing") return <Landing onStart={() => setStep("login")} />

  if (step === "login") {
    return (
      <Login onLogin={(t, r, u) => {
        setToken(t); setRefresh(r); setMe(u)
        setStep("app")
      }} />
    )
  }

  if (step === "app") {
    return (
      <div className="flex">
        <Sidebar setView={setView} view={view} />
        <div className="flex-1 min-h-screen bg-gray-50">
          <Navbar me={me} onLogout={() => { 
            setToken(null); setRefresh(null); setMe(null); setStep("login") 
          }} />
          <main className="p-4">
            {view === "users" && <Users token={token} me={me} />}
            {view === "instituciones" && <InstitucionesPage />}
            {view === "tests" && <div className="p-6 bg-white shadow rounded">📝 Módulo de Tests vocacionales en construcción...</div>}
            {view === "notificaciones" && <div className="p-6 bg-white shadow rounded">🔔 Módulo de Notificaciones en construcción...</div>}
            {view === "videollamadas" && <div className="p-6 bg-white shadow rounded">🎥 Módulo de Videollamadas en construcción...</div>}
            {view === "profile" && <div className="p-6 bg-white shadow rounded">🙍‍♂️ Perfil en construcción...</div>}
            {view === "settings" && <div className="p-6 bg-white shadow rounded">⚙️ Configuración en construcción...</div>}
          </main>
        </div>
      </div>
    )
  }
}


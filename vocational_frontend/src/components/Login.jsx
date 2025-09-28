import React, { useState } from 'react'

const API_BASE = import.meta.env.VITE_AUTH_API || "http://localhost:8000"

export default function Login({ onLogin }) {
  const [email, setEmail] = useState('admin@example.com')
  const [password, setPassword] = useState('admin')
  const [error, setError] = useState(null)

  const submit = async (e) => {
    e.preventDefault()
    setError(null)
    try {
      const res = await fetch(`${API_BASE}/api/auth/login/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
      })
      if (!res.ok) throw new Error('Login inválido')
      const data = await res.json()
      onLogin(data.tokens.access, data.tokens.refresh, data.user)
    } catch (err) {
      setError(err.message)
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-500 via-indigo-500 to-purple-600">
      <div className="bg-white rounded-2xl shadow-lg p-8 w-full max-w-md">
        
        {/* Logo con brújula */}
        <div className="flex flex-col items-center mb-6">
          <img 
            src="https://cdn-icons-png.flaticon.com/512/535/535239.png" 
            alt="Brújula logo"
            className="w-16 h-16 mb-2"
          />
          <h1 className="text-2xl font-bold text-gray-800">Tu Ruta Educativa</h1>
          <p className="text-sm text-gray-500">Encuentra tu camino 🚀</p>
        </div>

        <form onSubmit={submit} className="flex flex-col gap-4">
          <input
            value={email}
            onChange={e => setEmail(e.target.value)}
            placeholder="Email"
            className="border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <input
            value={password}
            onChange={e => setPassword(e.target.value)}
            type="password"
            placeholder="Contraseña"
            className="border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />

          <button className="bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 transition transform hover:scale-105">
            Entrar
          </button>

          {error && <div className="text-red-500 text-sm">{error}</div>}
        </form>
      </div>
    </div>
  )
}

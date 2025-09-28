import React, { useEffect, useState } from "react"

const API_BASE = import.meta.env.VITE_AUTH_API || "http://localhost:8000"

export default function Users({ token, me }) {
  const [users, setUsers] = useState([])
  const [q, setQ] = useState("")
  const [form, setForm] = useState({
    email: "",
    password: "",
    nombre: "",
    apellido: "",
    rol: "estudiante"
  })

  const isAdmin = me?.rol === "admin"

  // cargar usuarios
  const load = async () => {
    const res = await fetch(`${API_BASE}/api/users/?q=${encodeURIComponent(q)}`, {
      headers: { Authorization: `Bearer ${token}` }
    })
    if (res.ok) {
      const data = await res.json()
      setUsers(data.results || data)
    }
  }

  useEffect(() => { load() }, [q])

  // crear usuario
  const save = async (e) => {
    e.preventDefault()
    const res = await fetch(`${API_BASE}/api/users/`, {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
      body: JSON.stringify(form)
    })
    if (res.ok) {
      setForm({ email: "", password: "", nombre: "", apellido: "", rol: "estudiante" })
      load()
    }
  }

  // eliminar usuario
  const del = async (id) => {
    const res = await fetch(`${API_BASE}/api/users/${id}/`, {
      method: "DELETE",
      headers: { Authorization: `Bearer ${token}` }
    })
    if (res.ok) load()
  }

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Usuarios</h2>
      <input
        placeholder="Buscar..."
        value={q}
        onChange={e => setQ(e.target.value)}
        className="border rounded px-3 py-2 mb-4 w-full"
      />
      {isAdmin && (
        <form onSubmit={save} className="grid gap-3 grid-cols-2 md:grid-cols-3 mb-6">
          <input placeholder="Email" value={form.email} onChange={e => setForm({ ...form, email: e.target.value })} className="border rounded px-3 py-2" />
          <input placeholder="Password" type="password" value={form.password} onChange={e => setForm({ ...form, password: e.target.value })} className="border rounded px-3 py-2" />
          <input placeholder="Nombre" value={form.nombre} onChange={e => setForm({ ...form, nombre: e.target.value })} className="border rounded px-3 py-2" />
          <input placeholder="Apellido" value={form.apellido} onChange={e => setForm({ ...form, apellido: e.target.value })} className="border rounded px-3 py-2" />
          <select value={form.rol} onChange={e => setForm({ ...form, rol: e.target.value })} className="border rounded px-3 py-2">
            <option value="estudiante">Estudiante</option>
            <option value="orientador">Orientador</option>
            <option value="admin">Admin</option>
          </select>
          <button className="bg-green-600 text-white py-2 rounded hover:bg-green-700 transition">Crear</button>
        </form>
      )}
      <table className="w-full border border-gray-300 rounded-lg overflow-hidden shadow">
        <thead className="bg-gray-100 text-gray-700">
          <tr>
            <th className="px-4 py-2 text-left">Email</th>
            <th className="px-4 py-2 text-left">Nombre</th>
            <th className="px-4 py-2 text-left">Rol</th>
            <th className="px-4 py-2 text-left">Activo</th>
            <th className="px-4 py-2 text-left">Acciones</th>
          </tr>
        </thead>
        <tbody>
          {users.map(u => (
            <tr key={u.id} className="border-t hover:bg-gray-50">
              <td className="px-4 py-2">{u.email}</td>
              <td className="px-4 py-2">{u.nombre} {u.apellido}</td>
              <td className="px-4 py-2">{u.rol}</td>
              <td className="px-4 py-2">{u.activo ? "Sí" : "No"}</td>
              <td className="px-4 py-2">
                {isAdmin && (
                  <button onClick={() => del(u.id)} className="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600 transition">
                    Eliminar
                  </button>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

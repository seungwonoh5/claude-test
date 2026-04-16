import { useState, useEffect } from 'react'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

function App() {
  const [users, setUsers] = useState(null)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetch(`${API_URL}/api/users`)
      .then((res) => res.json())
      .then((data) => setUsers(data.users))
      .catch(() => setError('Failed to fetch from API'))
  }, [])

  return (
    <div style={{ fontFamily: 'sans-serif', textAlign: 'center', marginTop: '4rem' }}>
      {error && <p>{error}</p>}
      {!users && !error && <p>Loading...</p>}
      {users && users.map((user) => (
        <p key={user.id}>{user.first_name} {user.last_name}</p>
      ))}
    </div>
  )
}

export default App

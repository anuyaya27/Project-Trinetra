import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Home from './components/Home'
import Case from './components/Case'
import Clue from './components/Clue'
import Astrology from './components/Astrology'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/case" element={<Case />} />
        <Route path="/clue" element={<Clue />} />
        <Route path="/astrology" element={<Astrology />} />
      </Routes>
    </Router>
  )
}

export default App
import React from 'react';
<<<<<<< HEAD

// import animate on scroll
import axios from 'axios';
import Aos from 'aos';
import 'aos/dist/aos.css';

// import components
import Hero from './components/index';

const App = () => {
  const [data, setData] = useState([]);
  const [source, setSource] = useState('');

  useEffect(() => {
    Aos.init({
      duration: 1800,
      offset: 0,
    });
  }, []);

  useEffect(() => {
    if (source) {
      axios.get(`http://localhost:8000/raw_data/source/${source}`)
        .then(response => setData(response.data))
        .catch(error => console.error('Error fetching data:', error));
    }
  }, [source]);

  return (
    <div className='overflow-hidden'>
      <Hero />
      <div>
        <h1>Data Warehouse</h1>
        <input
          type="text"
          value={source}
          onChange={e => setSource(e.target.value)}
          placeholder="Enter source"
        />
        <div>
          {data.map(item => (
            <div key={item.id} data-aos="fade-up">
              <h3>{item.source}</h3>
              <p>{item.data}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
=======
import { BrowserRouter as Router, Routes, Link, Route } from 'react-router-dom';
import {
  AudioDataList,
  LanguageList,
  SourceList,
  RawTextDataList,
  CleanTextDataList,
} from './components';

const App = () => {
  return (
    <Router>
      <div style={{ display: 'flex' }}>
        <div style={{ width: '200px', padding: '20px', background: '#f0f0f0' }}>
          <h2>Menu</h2>
          <ul style={{ listStyleType: 'none', padding: 0 }}>
            <li>
              <Link to="/languages">Languages</Link>
            </li>
            <li>
              <Link to="/sources">Sources</Link>
            </li>
            <li>
              <Link to="/raw-text-data">Raw Text Data</Link>
            </li>
            <li>
              <Link to="/cleaned-text-data">Cleaned Text Data</Link>
            </li>
            <li>
              <Link to="/audio-data">Audio Data</Link>
            </li>
          </ul>
        </div>
        <div style={{ margin: '20px', flex: 1 }}>
          <Routes>
            <Route path="/audio-data" element={<AudioDataList />} />
            <Route path="/languages" element={<LanguageList />} />
            <Route path="/sources" element={<SourceList />} />
            <Route path="/raw-text-data" element={<RawTextDataList />} />
            <Route path="/cleaned-text-data" element={<CleanTextDataList />} />
            <Route
              path="/"
              element={
                <div>
                  <h2>Welcome</h2>
                  <p>Select a menu item to view the data.</p>
                </div>
              }
            />
          </Routes>
        </div>
      </div>
    </Router>
  );
};
>>>>>>> d05e14d5c63d58cf41e10c4cb90f662a28a5326b

export default App;

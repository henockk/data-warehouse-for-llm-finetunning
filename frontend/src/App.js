import React from 'react';
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

export default App;

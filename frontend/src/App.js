import React from 'react';

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

export default App;

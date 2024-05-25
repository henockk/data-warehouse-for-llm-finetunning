import React, { useState, useEffect } from 'react';
import axios from 'axios';

const SourceList = () => {
  const [sources, setSources] = useState([]);
  const [search, setSearch] = useState('');
  const [sort, setSort] = useState('id');
  const [order, setOrder] = useState('asc');

  useEffect(() => {
    fetchSources();
  }, [search, sort, order]);

  const fetchSources = async () => {
    try {
      const response = await axios.get(`http://localhost:5000/sources`, {
        params: {
          search,
          sort,
          order,
        },
      });
      setSources(response.data);
    } catch (error) {
      console.error('Error fetching sources:', error);
    }
  };

  return (
    <div>
      <h2>Sources</h2>
      <input
        type="text"
        placeholder="Search"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />
      <table>
        <thead>
          <tr>
            <th onClick={() => setSort('id')}>ID</th>
            <th onClick={() => setSort('source_name')}>Source Name</th>
            <th onClick={() => setSort('source_type')}>Source Type</th>
          </tr>
        </thead>
        <tbody>
          {sources.map((src) => (
            <tr key={src.id}>
              <td>{src.id}</td>
              <td>{src.source_name}</td>
              <td>{src.source_type}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default SourceList;

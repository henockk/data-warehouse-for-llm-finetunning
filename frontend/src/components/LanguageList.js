import React, { useState, useEffect } from 'react';
import axios from 'axios';

const LanguageList = () => {
  const [languages, setLanguages] = useState([]);
  const [search, setSearch] = useState('');
  const [sort, setSort] = useState('id');
  const [order, setOrder] = useState('asc');

  useEffect(() => {
    fetchLanguages();
  }, [search, sort, order]);

  const fetchLanguages = async () => {
    try {
      const response = await axios.get(`http://localhost:5000/languages`, {
        params: {
          search,
          sort,
          order,
        },
      });
      setLanguages(response.data);
    } catch (error) {
      console.error('Error fetching languages:', error);
    }
  };

  return (
    <div>
      <h2>Languages</h2>
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
            <th onClick={() => setSort('language_name')}>Language Name</th>
          </tr>
        </thead>
        <tbody>
          {languages.map((lang) => (
            <tr key={lang.id}>
              <td>{lang.id}</td>
              <td>{lang.language_name}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default LanguageList;

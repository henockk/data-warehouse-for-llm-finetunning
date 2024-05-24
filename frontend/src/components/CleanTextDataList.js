import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CleanTextDataList = () => {
  const [cleanedTextData, setCleanedTextData] = useState([]);
  const [search, setSearch] = useState('');
  const [sort, setSort] = useState('id');
  const [order, setOrder] = useState('asc');

  useEffect(() => {
    fetchCleanedTextData();
  }, [search, sort, order]);

  const fetchCleanedTextData = async () => {
    try {
      const response = await axios.get(
        'http://localhost:5000/cleaned_text_data',
        {
          params: { search, sort, order },
        },
      );
      setCleanedTextData(response.data);
    } catch (error) {
      console.error('Error fetching cleaned text data:', error);
    }
  };

  const handleSort = (column) => {
    const newOrder = sort === column && order === 'asc' ? 'desc' : 'asc';
    setSort(column);
    setOrder(newOrder);
  };

  return (
    <div>
      <h2>Cleaned Text Data</h2>
      <input
        type="text"
        placeholder="Search"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />
      <table>
        <thead>
          <tr>
            <th onClick={() => handleSort('id')}>ID</th>
            <th onClick={() => handleSort('content')}>Content</th>
            <th onClick={() => handleSort('cleaned_at')}>Cleaned At</th>
          </tr>
        </thead>
        <tbody>
          {cleanedTextData.map((data) => (
            <tr key={data.id}>
              <td>{data.id}</td>
              <td>{data.content}</td>
              <td>{data.cleaned_at}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CleanTextDataList;

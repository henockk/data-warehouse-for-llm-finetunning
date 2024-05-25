import React, { useState, useEffect } from 'react';
import axios from 'axios';

const RawTextDataList = () => {
  const [rawTextData, setRawTextData] = useState([]);
  const [search, setSearch] = useState('');
  const [sort, setSort] = useState('id');
  const [order, setOrder] = useState('asc');

  useEffect(() => {
    fetchRawTextData();
  }, [search, sort, order]);

  const fetchRawTextData = async () => {
    try {
      const response = await axios.get(`http://localhost:5000/raw_text_data`, {
        params: {
          search,
          sort,
          order,
        },
      });
      setRawTextData(response.data);
    } catch (error) {
      console.error('Error fetching raw text data:', error);
    }
  };

  return (
    <div>
      <h2>Raw Text Data</h2>
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
            <th onClick={() => setSort('content')}>Content</th>
            <th onClick={() => setSort('date_collected')}>Date Collected</th>
          </tr>
        </thead>
        <tbody>
          {rawTextData.map((data) => (
            <tr key={data.id}>
              <td>{data.id}</td>
              <td>{data.content}</td>
              <td>{data.date_collected}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default RawTextDataList;

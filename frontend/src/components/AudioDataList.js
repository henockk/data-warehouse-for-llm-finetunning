import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AudioDataList = () => {
  const [audioData, setAudioData] = useState([]);
  const [search, setSearch] = useState('');
  const [sort, setSort] = useState('id');
  const [order, setOrder] = useState('asc');

  useEffect(() => {
    fetchAudioData();
  }, [search, sort, order]);

  const fetchAudioData = async () => {
    try {
      const response = await axios.get(`http://localhost:5000/audio_data`, {
        params: {
          search,
          sort,
          order,
        },
      });
      setAudioData(response.data);
    } catch (error) {
      console.error('Error fetching audio data:', error);
    }
  };

  const handleSort = (column) => {
    const newOrder = sort === column && order === 'asc' ? 'desc' : 'asc';
    setSort(column);
    setOrder(newOrder);
  };

  return (
    <div>
      <h2>Audio Data</h2>
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
            <th onClick={() => handleSort('audio_path')}>Audio Path</th>
            <th onClick={() => handleSort('transcript')}>Transcript</th>
            <th onClick={() => handleSort('date_collected')}>Date Collected</th>
          </tr>
        </thead>
        <tbody>
          {audioData.map((data) => (
            <tr key={data.id}>
              <td>{data.id}</td>
              <td>{data.audio_path}</td>
              <td>{data.transcript}</td>
              <td>{data.date_collected}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default AudioDataList;

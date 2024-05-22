import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000';

export const fetchLanguages = () => axios.get(`${API_BASE_URL}/languages`);
export const fetchSources = () => axios.get(`${API_BASE_URL}/sources`);
export const fetchRawTextData = () => axios.get(`${API_BASE_URL}/raw_text_data`);
export const fetchCleanedTextData = () => axios.get(`${API_BASE_URL}/cleaned_text_data`);
export const fetchAudioData = () => axios.get(`${API_BASE_URL}/audio_data`);
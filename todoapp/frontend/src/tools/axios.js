import axios from 'axios';

const clientAxio = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/v1.0/',
});

export default clientAxio;
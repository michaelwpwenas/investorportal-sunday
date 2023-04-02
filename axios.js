import axios from 'axios';

const API_URL = 'http://localhost:5000/api'; // replace with your API URL

class DataService {
  getAll(tableName) {
    return axios.get(`${API_URL}/${tableName}`);
  }

  get(tableName, id) {
    return axios.get(`${API_URL}/${tableName}/${id}`);
  }

  create(tableName, data) {
    return axios.post(`${API_URL}/${tableName}`, data);
  }

  update(tableName, id, data) {
    return axios.put(`${API_URL}/${tableName}/${id}`, data);
  }

  delete(tableName, id) {
    return axios.delete(`${API_URL}/${tableName}/${id}`);
  }
}

export default new DataService();
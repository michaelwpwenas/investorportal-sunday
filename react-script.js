import React, { useState, useEffect } from 'react';
import DataService from './DataService';

function MyComponent() {
  const [data, setData] = useState([]);

  useEffect(() => {
    DataService.getAll('my_table').then(response => {
      setData(response.data);
    });
  }, []);

  return (
    <div>
      {data.map(item => (
        <p key={item.id}>{item.name}</p>
      ))}
    </div>
  );
}

export default MyComponent;
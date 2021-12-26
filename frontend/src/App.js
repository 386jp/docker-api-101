import React, { useState, useEffect } from 'react';

import Container from 'react-bootstrap/Container';
import Card from 'react-bootstrap/Card';

function App() {

  const [postData, setPostData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const res = await fetch(
        process.env.REACT_APP_API_HOST_NAME + 'posts/',
      );
      const json = await res.json();
      // console.log(json);
      setPostData(json);
    };
    fetchData();
  }, []);

  return (
    <Container className="p-3">
    <Container className="p-5 mb-4 bg-light rounded-3">
      <h1 className="header">Docker API 101</h1>
      <p className="lead">Docker + FastAPI + SQLModel + ReactJS Modern API Example</p>
      {postData.map((post, i) => (
        <Card style={{ width: '18rem' }} className="mb-4 rounded-3" key={i}>
          <Card.Body>
            <Card.Title>{post.title ? post.title : ''}</Card.Title>
            <Card.Text>{post.content ? post.content : ''}</Card.Text>
          </Card.Body>
        </Card>
      ))}
    </Container>
  </Container>
  );
}

export default App;

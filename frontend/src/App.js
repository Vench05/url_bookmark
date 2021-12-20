import './App.css';
import { Card, Container, ListGroup, ListGroupItem } from 'react-bootstrap'
import axios from 'axios'
import { useEffect, useState } from 'react';

function App() {
  const [bookmarks, setBookmarks] = useState([])

  // useEffect(async () => {
  //   await axios.get('http://localhost:8000/bookmarks')
  //     .then(res => setBookmarks(res.data))
  // }, [])

  return (
    <Container>
      {bookmarks.map(data => {
        <Card style={{ margin: 100, width: '18rem', marginLeft: 'auto', marginRight: 'auto' }}>
          <Card.Img variant="top" src={data.screenshot} />
          <Card.Body>
            <Card.Title>{data.title}</Card.Title>
            <Card.Text>
              {data.some_info}
            </Card.Text>
          </Card.Body>
          <ListGroup className="list-group-flush">
            <ListGroupItem>Cras justo odio</ListGroupItem>
            <ListGroupItem>Dapibus ac facilisis in</ListGroupItem>
            <ListGroupItem>Vestibulum at eros</ListGroupItem>
          </ListGroup>
          <Card.Body>
            <Card.Link href={data.url}>Link</Card.Link>
          </Card.Body>
        </Card>
      })}
    </Container>
  );
}

export default App;

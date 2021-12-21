import './App.css';
import { Card, Container, InputGroup, FormControl, Button } from 'react-bootstrap'
import axios from 'axios'
import { useEffect, useState } from 'react';

function App() {
  const [bookmarks, setBookmarks] = useState([])

  useEffect(async () => {
    async function fetchData() {
      await axios.get('http://localhost:8000/bookmarks')
        .then(res => setBookmarks(res.data))
        .catch(res => console.log(res))
    }
    fetchData();
  }, [])

  return (
    <Container style={{ marginTop: 100 }} >
      <InputGroup size="sm" className="mb-3">
        <Button> <InputGroup.Text id="inputGroup-sizing-sm">Add Url</InputGroup.Text> </Button>
        <FormControl aria-label="Add" aria-describedby="inputGroup-sizing-sm" />
      </InputGroup>

      {bookmarks.map(data =>
        <Card key={data.id} style={{ width: '18rem' }}>
          <Card.Img variant="top" src={require(`./image/${data.title}.png`)} />
          <Card.Body>
            <Card.Title> {data.title} </Card.Title>
            <Card.Text> {data.some_info} </Card.Text>
            <Card.Link href={data.url}>{data.url}</Card.Link>
          </Card.Body>
        </Card>
      )}
    </Container>
  );
}

export default App;

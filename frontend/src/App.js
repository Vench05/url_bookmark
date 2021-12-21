import './App.css';
import { CloseButton, Container, InputGroup, FormControl, Button, Accordion, Figure, Row, Col } from 'react-bootstrap'
import axios from 'axios'
import { useEffect, useState } from 'react';

function App() {
  const [bookmarks, setBookmarks] = useState([])
  const [newUrl, setNewUrl] = useState('')
  const [isLoading, setLoading] = useState(false);

  useEffect(async () => {
    setLoading(false)
    async function fetchData() {
      await axios.get('http://localhost:8000/bookmarks')
        .then(res => setBookmarks(res.data))
        .catch(res => console.log(res))
    }
    fetchData();
  }, [])

  async function add_url() {
    setLoading(true)
    await axios.post('http://localhost:8000/bookmarks/', { 'url': newUrl })
      .then(res => {
        setBookmarks(prevState => [...prevState, res.data])
        setLoading(false)
        setNewUrl('')
      })
  }

  async function deleteUrl(id) {
    await axios.delete(`http://localhost:8000/bookmarks/${id}/delete`)
      .then(res => setBookmarks(bookmarks.filter(data => data.id !== id)))
  }

  return (
    <Container style={{ marginTop: 100 }} >
      <InputGroup size="sm" className="mb-3">
        <Button onClick={add_url}> <InputGroup.Text id="inputGroup-sizing-sm">{isLoading ? 'Loading…' : 'Add Url'}</InputGroup.Text> </Button>
        <FormControl value={newUrl} onChange={e => setNewUrl(e.target.value)} aria-label="Add" aria-describedby="inputGroup-sizing-sm" />
      </InputGroup>
      <Accordion>
        {bookmarks.map(data =>
          <Accordion.Item eventKey={data.id} key={data.id}>
            <Accordion.Header>
              <CloseButton onClick={deleteUrl} />
              {data.title}
            </Accordion.Header>
            <Accordion.Body>
              <Row>
                <Col>
                  <Figure>
                    <Figure.Image
                      width={500}
                      height={180}
                      alt="171x180"
                      src={require(`./image/${data.title}.png`)}
                    />
                    <Figure.Caption>
                      Screenshot
                    </Figure.Caption>
                  </Figure>
                </Col>
                <Col>
                  {data.some_info ? data.some_info : 'Didn\'t get any info'}
                </Col>
              </Row>
              <Row>
                <div className="d-grid gap-2">
                  <Button variant="primary" size="sm" onClick={(e) => {
                    e.preventDefault();
                    window.location.href = data.url
                  }}>
                    {data.url}
                  </Button>
                </div>
              </Row>
            </Accordion.Body>
          </Accordion.Item>
        )}
      </Accordion>
    </Container>
  );
}

export default App;

import './App.css';
import Card from './components/Card';

function App() {
  return (
    <div className="App">
      <Card 
        imgSrc="https://picsum.photos/300/200"
        imgAlt="Card Img"
        title="Card Title"
        description="Sample card description."
        btnText="myButton"
        link="/"
      />
    </div>
  );
}

export default App;

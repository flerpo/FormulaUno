import React, { Component } from 'react';

class App extends Component {
  state = {
    tracks: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/'); // fetching the data from api, before the page loaded
      const tracks = await res.json();
      this.setState({
        tracks
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {console.log(this.state.tracks)}
        {this.state.tracks.map(item => (
          <div key={item.trackId}>
            <h1>{item.name}</h1>
            <span>{item.current_record}</span>
            <span>{item.length}</span>
          </div>
        ))}
      </div>
    );
  }
}

export default App;

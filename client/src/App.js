import React, { Component } from 'react'
import Header from './header'
import FormType from './formSelect'
import './formSelect.css'
import p1 from './p1.png'
import p2 from './p2.png'
import p3 from './p3.png'
import { Steps, Step } from "react-step-builder";
class App extends Component{
  constructor(props) {
    super(props);
    this.pics = [p1 , p2 , p3]
  }
  render() {
    return (
      <div id='wrapper'>
      <Header />
      <FormType src={ this.pics }/>
      </div>
    )
  }
}


export default App;

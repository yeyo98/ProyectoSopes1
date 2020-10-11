import React from 'react';
import logo from '../logo.svg';
import './styles/App.css';
import NavBar from './NavBar'
import { BrowserRouter, Route, Switch } from 'react-router-dom'
import Estadistica from './Estadistica';
//import Cards from './Cards';
import ContenidoA from './Contenido';
import ContenidoB from './ContenidoB';

class App extends React.Component{
  render(){
    
    return (
      <div className="App">
        <NavBar/>
        <BrowserRouter>
            <Switch>
                <Route exact path = '/contendidoA' component={ContenidoA} />
                <Route exact path = '/contendidoB' component={ContenidoB} />
                <Route exact path = '/estadistica' component={Estadistica} />
                <Route component={Date} />
            </Switch>
        </BrowserRouter>

        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            <code>Bienvenido!!</code> :D
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
          </a>
        </header>
      </div>
    );
  }
}
/*
                
                <Route exact path = '/contendidoB' component={Performance} />
<header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header> */
export default App;

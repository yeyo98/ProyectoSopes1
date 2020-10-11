import React from 'react';

class NavBar extends React.Component{

    render(){
        return(
            <nav className="navbar navbar-dark bg-dark">
                <div>
                <a className="navbar-brand" href="/contendidoA">Contenido A</a>
                <a className="navbar-brand" href="/contendidoB">Contenido B</a>
                <a className="navbar-brand" href="/estadistica">Estadisticas</a></div>
            </nav>
        )
    }
}

export default NavBar;
import React from 'react';

import Grafica from './Grafica'

class Estadistica extends React.Component{

    servidorA = 'http://35.236.53.86/serverFeature'
    servidorB = 'http://34.94.243.77/serverFeature'
    render(){
        return(
            <div>
                <Grafica
                    bordercolor1='rgba(75,192,192,1)'
                    background1='rgba(75,192,192,0.2)'
                    bordercolor2='#742774'
                    background2='#c04bc0'
                    name='A'
                    ruta={this.servidorA}
                />
                <Grafica
                    bordercolor1='#0aa517'
                    background1='#b9febf'
                    bordercolor2='#ae0d0d'
                    background2='#9b0101'
                    name='B'
                    ruta={this.servidorB}
                />
            </div>
        )
    }
}

export default Estadistica
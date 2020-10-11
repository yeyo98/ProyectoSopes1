import React from 'react';
import Cards from './Cards'

class ContenidoB extends React.Component{

    constructor(props){
        super(props)
        this.state = {
            lista:  []
        }
    }

    async componentDidMount(){
        await this.ObtenerDatos()
     }
 
     async componentDidUpdate(){
         await setTimeout( async()=>{
             await this.ObtenerDatos()
         },5000)
     }
 
 
     getLista(){
         return this.state.lista
     }

     async ObtenerDatos(){
        const api = await fetch('http://34.94.243.77/recuperarCitas')
        const valores = await api.json()
        let lista = this.getLista()
        lista = valores.arr
        //console.log(lista)

        this.setState({
            lista
        })
     }

     render(){
        this.ObtenerDatos()
         return(
         <div>
             { this.state.lista.map((dato)=>{
                 return(
                 <Cards
                    nombre={dato.autor}
                    nota={dato.nota}
                 />)
             })
             }
         </div>
         )
     }
}

export default ContenidoB
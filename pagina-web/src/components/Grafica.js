import React from 'react';
import { Line }  from 'react-chartjs-2';

class Grafica extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            data: {
                labels: ['0.5', '0.10', '0.15', '0.20', '0.25', '0.30', '0.35', '0.40', '0.45','0.50','0.60'],
                datasets: [
                    {
                        label: `Servidor ${props.name} RAM`,
                        fill:true,
                        lineTension:0.5,
                        pointRadius:3,
                        pointHitRadius:0,
                        borderColor: props.bordercolor1,
                        backgroundColor: props.background1,
                        data: [0],
                    },
                    {
                        label: `Servidor ${props.name} CPU`,
                        fill:true,
                        lineTension:0.5,
                        pointRadius:3,
                        pointHitRadius:0,
                        borderColor: props.bordercolor2,
                        background: props.background2,
                        data: [0],
                    },
                ]
            }
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


    getData(){
        return this.state.data
    }

    async ObtenerDatos(){
        const api = await fetch(this.props.ruta)
        const valores = await api.json()

        //console.log(valores)
        if(valores.estado === 400)
            return;
        
        let data = this.getData()
        
        if(data.datasets[0].data.length === data.labels.length){
            data.datasets[0].data.splice(0,1)
        }
        
        if(data.datasets[1].data.length === data.labels.length){
            data.datasets[1].data.splice(0,1)
        }
        
        data.datasets[0].data.push(valores.ram)
        
        data.datasets[1].data.push(valores.cpu)

        this.setState({
            data
        })
    }

    render(){
        return(
            <Line data={this.getData()}
             redraw
             width={800} height={250}/>
        )
    }
}

export default Grafica
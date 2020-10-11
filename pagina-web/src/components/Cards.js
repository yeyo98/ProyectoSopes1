import React from 'react';
import circlesImg from '../images/circles.png'
import './styles/Cards.css'

class Cards extends React.Component{

    render(){
        return(
            <div className="card mx-auto Fitness-Card"
            style={{
                backgroundImage: `url(${circlesImg}), linear-gradient(to right, '#A74CF2', '#617BFB') `
            }}
            >
                <div className="card-body">
                    <div className="row center">
                        <div className="col-6 Fitness-Card-Info">
                            <h1>{this.props.nombre}</h1>
                            <p>{this.props.nota}</p>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default Cards;
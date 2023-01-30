import React from 'react';
import Alphabet from './ASL Alphabet Chart.jpg';
import Number from './ASL Number Chart.jpg';
import Book from './Book.jpg';
import Meet from './Meet.jpg';
import Name from './Name.jpg';
import Nice from './Nice.jpg';
import Read from './Read.jpg';
import What from './What.jpg';
import You from './You.jpg';


function Learn() {
    return (
        <div>
            <div className="learn"><h1>Learn American Sign Language with Us</h1></div>

            <div className="learn"><img src={Alphabet} height={850} width={1160}></img></div>
            <div className="learn"><img src={Number} height={601} width={852}></img></div>

            <div className="learn"><img src={Book} height={720} width={1280}></img><h3>Book</h3></div>
            <div className="learn"><img src={Meet} height={720} width={1280}></img><h3>Meet</h3></div>
            <div className="learn"><img src={Name} height={720} width={1280}></img><h3>Name</h3></div>
            <div className="learn"><img src={Nice} height={720} width={1280}></img><h3>Nice</h3></div>
            <div className="learn"><img src={Read} height={720} width={1280}></img><h3>Read</h3></div>
            <div className="learn"><img src={What} height={720} width={1280}></img><h3>What ?</h3></div>
            <div className="learn"><img src={You} height={720} width={1280}></img><h3>You / Your</h3></div>
        </div>

    );
}

export default Learn;
import React from 'react';
import {useState, useEffect} from 'react';
function Welcome() {

    return (
        <div>
            <div className="welcome"><h1>Welcome</h1></div>
            <div className="welcome"><p>My name is Wong Jack Yih, TP055436</p></div>
            <div className="welcome">
                <p>This is my final year project called "Sign Speakers", its aim is to translate American Sign Language in real time.
                    In this study, we compared 2 different implementation methods and model types to assess its perdiction performance.
                </p>
            </div>
            <div className="welcome">
                <p> Based on the assesment and model evaluation done in the report, an LSTM Model is chosen. The demo model loaded for this model would be our LSTM Volcabulary model.
                    Which recognizes 2 handed American Sign Language words. The options are shown on screen with bar charts to indicate its prediction confidence.
                </p>
            </div>
        </div>

    );
}

export default Welcome;
import React from 'react'
import language from './language.jpg'

class Language extends React.Component{
    constructor(props) {
        super(props)
    }
    render() {
        return (
            <div className="language">
                <image src={language} />
                <label>
                    Language
                     <input name="language" type="text" placeholder="enter language name and rate yourself" />
                </label>
                <label>
                    Rate
                     <input type="range" name="langRate" min="1" max="5"/>
                    </label>
            </div>
        )
    }
}


export default Language
import React from 'react'
import skillPic from './skill.png'

class Skills extends React.Component{
    constructor(props) {
        super(props)
    }
    render() {
        <div className="skill">
            <img src={skillPic} />
            <label>
                Skills
                <input name="skill" type="text" />
            </label>
            <label>
                <input name="skillRate" type="range" min="1" max="5" />
                </label>
        </div>
    }
}

export default Skills
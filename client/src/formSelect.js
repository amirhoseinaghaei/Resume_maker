import React from 'react'

function FormType(props) {
    console.log(props.src[0])
    return (
        <div class="picWrapper">
        <label>
                <input className="selection" id="form1" type="checkbox" value="false" />
                <img className="pics" src={props.src[0]} />
            </label>
            <label>
                <input className="selection" id="form2" type="checkbox" value="false" />
                <img className="pics" src={props.src[1]} />
            </label>
            <label>
                <input className="selection" id="form3" type="checkbox" value="false" />
                <img className="pics" src={props.src[2]} />
            </label>
            
        </div>
    )
}

export default FormType
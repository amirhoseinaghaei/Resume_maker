import React from 'react'

class Personal extends React.Component{
    constructor(props) {
        super(props)
    }
    render() {
        return (
            <div className="personal">
                <label>
                First Name*
                <input name="firstName" type="text" required />
                </label>
                <label>
                Last Name*
                <input name="lastName" type="text" required />
                </label>
                <label>
                Field*
                <input name="field" type="text" required />
                </label>
                <label>
                Phone*
                <input name="phone" type="tel" required pattern="09[0-9]{9}" placeholder="09000000000" />
                </label>
                <label>
                Email*
                <input name="email" type="email" required placeholder="johndoe@something.com" />
                </label>
                <label>
                Github*
                <input name="github" type="url" required />
                </label>
                <label>
                    Repo
                <input name="repo" type="url" />
                <button> ADD </button>
                </label>
                <label className="adress">
                Country
                <input name="country" type="text" required />
                </label>
                <label className="adress">
                City
                <input name="city" type="text" />
                </label>
                <label  className="adress">
                Street
                <input name="street" type="text" />
                </label>
                <label>
                    Summary about yourself
                    <textarea name="sum" placeholder="..." ></textarea>
                </label>
            </div>
        )
    }
}

export default Personal
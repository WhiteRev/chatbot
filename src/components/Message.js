import React from 'react';
import { formatRelative} from 'date-fns';

let x = 2;
const y = x++;
console.log(y)
const Message = ({
    createdAt = null,
    text = '',
    displayName = '',
    photoURL = '',
}) => {
    return(
    <div className="sl_message">
        {photoURL ? (
            <img src={photoURL} alt="Avatar" className='sh_userimg' width={45} height={45}/>
        ) : null}
        {displayName ? <p className='sl_messagecht'>{displayName}</p> : null}
        {createdAt ?.seconds ? (
            <span className='sl_hide'>
                {formatRelative(new Date(createdAt.seconds = 1000), new Date()
                )}
            </span>) : null}
        <p className='sl_messagecht'>{text}</p>
    </div>
    );
};
export default Message;
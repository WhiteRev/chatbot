import React, { useEffect, useState } from 'react';
import firebase from 'firebase/compat/app';
import Message from './Message';

import { db } from '../App';
// Components

const Channel = ({ user = null, }) => {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');

  const { uid, displayName, photoURL } = user;

  useEffect(() => {
    if (db){
      const unsubcribe = db
        .collection('messages')
        .orderBy('createdAt')
        .limit(100)
        .onSnapshot(querySnapshot => {
          const data = querySnapshot.docs.map(doc => ({
            ... doc.data(),
            id: doc.id,
          }));
          setMessages(data);
        })
          return unsubcribe;
    } 


  }, [db]);
  

  const handleOnChange = e => {
    setNewMessage(e.target.value);
  };

  const handleOnSubmit = e => {
    
    e.preventDefault();
    if (db) {
      db.collection('messages').add({
        text: newMessage,
        createdAt: firebase.firestore.FieldValue.serverTimestamp(),
        uid,
        displayName,
        photoURL

      })

    }
    document.getElementById("myForm").reset(); 

  };
  return (
    <div>
        <ul className='discussion'>
        {messages.map(message => (

          
            <li className='bubble sender first' key={message.id}>
              <Message { ...message} />
            </li>
          )) }
      </ul>  
      <form id='myForm' onSubmit={handleOnSubmit}>
        <input
        className="btnsubmit"
          type="text"
          value={newMessage}
          onChange={handleOnChange}
          placeholder="Type your message here ..."z
        />
        <button type="submit" disabled={!newMessage}>
          Send

        </button>
        <button type="sl_talk" disabled={!newMessage}>
          TALK

        </button>
      </form>
    </div>
  );
};

export default Channel;

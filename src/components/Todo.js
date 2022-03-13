import React, { useEffect, useState } from 'react';
import firebase from 'firebase/compat/app';
import Message from './Message';

import { db } from '../App';
// Components

const Todo = ({ user = null, }) => {
  const [todos, settodos] = useState([]);
  const [newtodo, setNewtodo] = useState('');

  const { uid, displayName, photoURL } = user;

  useEffect(() => {
    if (db){
      const unsubcribe = db
        .collection('todo')
        .orderBy('createdAt')
        .limit(100)
        .onSnapshot(querySnapshot => {
          const data = querySnapshot.docs.map(doc => ({
            ... doc.data(),
            id: doc.id,
          }));
          settodos(data);
        })
          return unsubcribe;
    } 


  }, [db]);
  

  const handleOnChange = e => {
    setNewtodo(e.target.value);
  };

  const handleOnSubmit = e => {
    
    e.preventDefault();
    if (db) {
      db.collection('todos').add({
        text: newtodo,
        createdAt: firebase.firestore.FieldValue.serverTimestamp(),
        uid,
        displayName,
        photoURL

      })

    }
    document.getElementById("myForm").reset(); 

  };
  return (
    <div className="sl-alignright">
        <ul className='discussion alignright'>
        {todos.map(todo => (

          
            <li className='bubble sender first' key={todo.id}>
              <Message { ...todo} />
            </li>
          )) }
      </ul>    

    </div>
  );
};

export default Todo;

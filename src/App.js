import React, { useEffect, useState } from "react";
import logo from './logo.svg';
// Components
import Channel from './components/Channel';
import Todo from './components/Todo';
import sl_web from './App/sl_web';
import Button from './components/Button';
import './App.css';
import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import 'firebase/compat/firestore';
import { fireEvent } from "@testing-library/react";

firebase.initializeApp({
  apiKey: "AIzaSyC9yV4SK-FvyMWTJ4vvHT2N6i5j2ucawuc",

  authDomain: "react-firechat-22f33.firebaseapp.com",

  projectId: "react-firechat-22f33",

  storageBucket: "react-firechat-22f33.appspot.com",

  messagingSenderId: "513806193235",

  appId: "1:513806193235:web:5c4d23786a9b3e07882ca6",

  measurementId: "G-E99T672XHY"

}
);





export const auth = firebase.auth();
export const db = firebase.firestore(); 
export const googleAuthProvider = new firebase.auth.GoogleAuthProvider();



function App() {

  const [user, setUser] = useState(() => auth.currentUser) ;
  const [initializing, setInitializing] = useState(true)  ;
  
  useEffect(() => {
    const unsubcribe = auth.onAuthStateChanged(user => {
      if (user) {
        setUser(user);
      } else {
        setUser(null);
      }
      if (initializing) {
        setInitializing(false);
      }
    });
    return unsubcribe;
  }, []);
  
  const signInWithGoogle = async () => {
    // Retrieve Google provider object
    const provider = new firebase.auth.GoogleAuthProvider();
    // Set language to the default browser preference
    auth.useDeviceLanguage();
    // Start sign in process
    try {
      await auth.signInWithPopup(provider);
    } catch (error) {
      console.log(error.message);
    }
  };
  

  const signOut = async () => {
    try{
      await firebase.auth().signOut();

    } catch (error) {
      console.log(error.message);
       
    }
  };

  if (initializing) return "Loading ...";

  return (
    <div className="App">
    <div className="chat_app">
      {user ? (
      <> 
      <div className="sl_mat">
      <div className="sl_chat">
          <div className="OffButton" >
            <Button onClick={signOut}>Sign Out</Button>
          </div>
          <Channel user={user} db={db} />

      </div>
      <div className="App_todo">
      <Todo user={user} db={db} />
       </div>
    </div>
      </>
      ):  (
      <div className="sl_sign_box">

        <div className="sl_sign">
        <Button onClick={signInWithGoogle}>Sign in With Google</Button>
        </div>
      </div>
      )}
    </div>

  </div>
  );
}

export default App;

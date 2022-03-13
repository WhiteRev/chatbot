
import React from 'react';
import '../../App.css';
import Cards from '../Cards';
import Footer from '../Footer';

function Services() {
  return (
    <>
      <div>
      <video src='/videos/video-1.mp4' autoPlay loop muted />
      <h1 className='services'>SERVICES</h1>
      </div>
      <Cards />
      <Footer />
    </>
  );
}

export default Services;

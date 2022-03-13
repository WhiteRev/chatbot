
import React from 'react';
import '../../App.css';
import Cards from '../Cards';
import Footer from '../Footer';

function Products() {
  return (
    <>
      <div>
      <video src='/videos/video-1.mp4' autoPlay loop muted />
      <h1 className='products'>Coucouc </h1>
      <div><h1 className='bla'>Product</h1></div>
      </div>
      <Cards />
      <Footer />
    </>
  );
}

export default Products;

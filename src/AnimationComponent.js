import React from 'react';
import Lottie from 'react-lottie';
import animationData from './animation.json'; // make sure this path is correct

const AnimationComponent = () => {
  const defaultOptions = {
    loop: true,
    autoplay: true,
    animationData: animationData,
    rendererSettings: {
      preserveAspectRatio: 'xMidYMid slice'
    }
  };

  return (
    <div className="animation-container">
      <Lottie options={defaultOptions} height={410} width={600} speed={0.3} />
    </div>
  );
};

export default AnimationComponent;
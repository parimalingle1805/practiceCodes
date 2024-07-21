import React from 'react';
import './Card.css';

const Card = ({
  imgSrc,
  imgAlt,
  title,
  description,
  btnText,
  link
}) => {
  return (
    <div className='card'>
      {imgSrc && <img src={imgSrc} alt={imgAlt} />}
      {title && <h1>{title}</h1>}
      {description && <p>{description}</p>}
      {link && btnText && <div className='button-div'>
        <a href={link} className='button'>{btnText}</a>
      </div>}
    </div>
  )
};

export default Card;
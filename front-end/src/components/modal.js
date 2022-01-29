import React, { useEffect, useState } from "react";

const Modal = ({ src, alt, caption, onClose }) => {
  return (
    <div className="modal">
      <span className="close" onClick={onClose}>
        &times;
      </span>
      <img className="modal-content" src={src} alt={alt} />
    </div>
  )
}

export const ModalBox = (src) => {
  const [isOpen, setIsOpen] = useState(false)
  const showModal = () => setIsOpen(true)

  return (
    <div className="App">
      <img
        className="image"
        onClick={showModal}
        src= {src.url}
        alt=""
      />
      {isOpen && (
        <Modal
          src={src.url}
          alt=""
          caption=""
          onClose={() => setIsOpen(false)}
        />
      )}
    </div>
  )
}
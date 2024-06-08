'use client'
import React from 'react'

interface ButtonProps {
  onClick: () => void;
  color: string;
  text: string;
}

const Button: React.FC<ButtonProps> = ({ onClick, color, text }) => {
  const colorClasses: { [key: string]: string } = {
    blue: 'bg-blue-500 hover:bg-blue-700',
    red: 'bg-red-500 hover:bg-red-700',
    green: 'bg-green-500 hover:bg-green-700'
  };

  const colorClass = colorClasses[color] || colorClasses['blue'];

  return (
    <button className={`bg-${colorClass} hover: ${colorClass} text-white font-bold py-2 px-4 rounded-xl mt-7`} onClick={onClick}>
      {text}
    </button>
  )
}

export default Button

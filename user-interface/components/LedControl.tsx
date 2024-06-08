'use client'
import Button from "./Button"
import axios from 'axios';

const LedControl = () => {
  const ledOn = async () => {
    console.log("Lights ON");
    try {
      const response = await axios("http://192.168.0.104:8000/led?state=on");
      console.log(response.data);
    } catch (error) {
      console.log("Error turning on: ", error);
    }
  }

  const ledOff = async () => {
    console.log("Lights OFF");
    try {
      const response = await axios("http://192.168.0.104:8000/led?state=off");
      console.log(response.data);
    } catch (error) {
      console.log("Error turning off: ", error);
    }
  }

  return (
    <div className="flex justify-center items-center min-h-screen">
      <div className = "border border-red-600 rounded-md w-fit p-5">
        <h1 className="text-red-600"><em><b>LIGHTS CONTROL</b></em></h1>
        <div className="space-x-6">
        <Button onClick={ledOn} text = "ON" color = "green"/>
        <Button onClick={ledOff} text = "OFF" color = "red"/>
        </div>
      </div>
    </div>
  )
}

export default LedControl

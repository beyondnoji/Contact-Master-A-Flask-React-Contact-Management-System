import { useState, useEffect } from 'react'
import ContactForm from './ContactForm'
import './App.css'
import ContactList from './ContactList'

function App() {
const [contacts, setContacts] = useState([])
const [isModalOpen, setIsModalOpen] = useState(false)
const [currentContact, setCurrentContact] = useState({})
useEffect(() => {
  fetchContacts()
  // calls fetchContacts as soon as site renders
}, []); 

const fetchContacts = async () => { 
  const response = await fetch("http://127.0.0.1:5000/contacts")
  // sending a get request to contacts route
  // once it gives a response: 
  const data = await response.json() 
  setContacts(data.contacts) 
  // sets it in the state 
};
const closeModal = () => {
  setIsModalOpen(false)
  setCurrentContact({})
}

const openCreateModal = () => {
  if (!isModalOpen) setIsModalOpen(true)
}

const openEditModal = (contact) => {
  if (isModalOpen) return
  setCurrentContact(contact)
  setIsModalOpen(true)
}

const onUpdate = () => {
  closeModal()
  fetchContacts()
}

  return (
    <>
      <ContactList contacts={contacts} updateContact={openEditModal} updateCallback={onUpdate} />
      <button onClick={openCreateModal}>Create New Contact</button>
      {isModalOpen && <div className="modal">
        <div className="modal-content">
          <span className="close" onClick={closeModal}>&times;</span>
          <ContactForm existingContact={currentContact} updateCallback={onUpdate} />
        </div>
      </div>
      }
    </>
  );
}

export default App;

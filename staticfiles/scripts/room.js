document.addEventListener('DOMContentLoaded', (event) => {
    const chatMessagesContainer = document.getElementById('chat-messages-container');
    chatMessagesContainer.scrollTop = chatMessagesContainer.scrollHeight;
});
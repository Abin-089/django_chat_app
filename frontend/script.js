document.addEventListener('DOMContentLoaded', () => {
    /*******************************************
     * PART A: Zoom-based resizing
     *******************************************/
    function adjustZoom() {
      const width = window.innerWidth;
      let zoomFactor = 1; // default 100%
  
      if (width >= 992 && width <= 1600) {
        zoomFactor = 0.9;
      } else if (width >= 700 && width <= 767) {
        zoomFactor = 0.8;
      } else if (width >= 600 && width < 700) {
        zoomFactor = 0.75;
      } else if (width <= 600) {
        zoomFactor = 0.5;
      }
  
      // Apply zoom for browsers that support it
      document.body.style.zoom = zoomFactor;
    }
  
    // Call at page load
    adjustZoom();
    // Call on window resize
    window.addEventListener('resize', adjustZoom);
  
    /*******************************************
     * PART B: Collapsible Left Menu (example)
     *******************************************/
    const toggleMenuBtn = document.getElementById('toggleMenuBtn');
    const leftMenu = document.getElementById('leftMenu');
    const mainContent = document.getElementById('mainContent');
  
    toggleMenuBtn.addEventListener('click', () => {
      const isOpen = leftMenu.classList.contains('open');
      if (!isOpen) {
        leftMenu.classList.add('open');
        mainContent.style.marginLeft = '240px';
      } else {
        leftMenu.classList.remove('open');
        mainContent.style.marginLeft = '0';
      }
    });
  
    /*******************************************
     * PART C: Simulated Send Message (example)
     *******************************************/
    const messagesContainer = document.getElementById('messagesContainer');
    const messageInput = document.getElementById('messageInput');
    const sendBtn = document.getElementById('sendBtn');
  
    sendBtn.addEventListener('click', () => {
      const msg = messageInput.value.trim();
      if (msg) {
        const newMsg = document.createElement('div');
        newMsg.classList.add('message', 'sent');
        newMsg.innerHTML = `<strong>You:</strong> ${msg}`;
        messagesContainer.appendChild(newMsg);
        messageInput.value = '';
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
      }
    });
  
    messageInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendBtn.click();
      }
    });
  });
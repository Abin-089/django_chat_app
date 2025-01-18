# Django Chat Application

This project is a simple chat application built with Django, featuring the ability to display all registered users in a collapsible left menu, initiate private chats, and retrieve old messages. It also uses WebSocket functionality for real-time communication.

## Features

1. **User Authentication:**
   - Users can log in, sign up, and log out.

2. **Rooms Page:**
   - Displays all available chat rooms.
   - Allows users to join specific chat rooms.

3. **Collapsible User List:**
   - A collapsible menu on the left side displays all registered users (excluding the logged-in user).
   - Users can select any user from the menu to initiate a private chat.

4. **Private Chat:**
   - Logged-in users can engage in private one-on-one chats.
   - Old messages between the two users are retrieved and displayed.

5. **Real-Time Messaging:**
   - Messages sent in the chat are updated in real-time using WebSockets.

6. **Responsive Design:**
   - The application is styled with Tailwind CSS, ensuring a responsive and modern user interface.

---

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application:**
   Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## File Structure

- **`base.html`:**
  - Contains the main layout with a collapsible user list.
- **`rooms.html`:**
  - Displays all chat rooms available for joining.
- **`private_chat.html`:**
  - Handles the interface for private one-on-one chats, displaying old messages and a form to send new ones.
- **WebSocket Implementation:**
  - WebSocket connections are used for real-time messaging.

---

## Key Files and Features

### Templates

1. **`base.html`:**
   - Includes the navigation bar, collapsible user list, and main content area.

2. **`private_chat.html`:**
   - Displays the private chat interface.
   - Retrieves and displays old messages.

3. **`rooms.html`:**
   - Lists all chat rooms and allows users to join them.

### Models

1. **`Message`:**
   - Fields: `sender`, `receiver`, `content`, `timestamp`.
   - Stores chat messages between users.

### Views

1. **`private_chat`:**
   - Retrieves old messages between two users.

2. **`rooms`:**
   - Displays available chat rooms.

## How to Use

1. **Log In or Sign Up:**
   - Use the navigation bar to log in or sign up.

2. **View Users:**
   - Click the "Toggle Users" button to view all registered users in the collapsible menu.

3. **Initiate Private Chat:**
   - Click on a username to start a private chat.

4. **Send and Receive Messages:**
   - Use the input field in the private chat interface to send messages.
   - Messages are updated in real-time.

5. **View Old Messages:**
   - Previous messages between users are displayed in the chat interface.

---

## Dependencies

- **Django**: Backend framework.
- **Channels**: For WebSocket support.

---

## Future Improvements

- Add group chat functionality.
- Include typing indicators.
- Implement read receipts.
- Improve the UI with more modern designs.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.



# Hotels Booking Assistant

This project implements an AI-powered hotel booking assistant using the LiveKit Agents framework. The assistant helps guests book rooms by collecting their name, address, and preferred room type, and processes bookings through a simple booking system.

## Features
- **Guest Interaction**: Collects guest details (name, address, room type) and processes booking requests.
- **Booking Management**: Checks for existing bookings, verifies room availability, and creates new bookings.
- **Voice and Video Support**: Integrates with LiveKit for real-time interaction, including noise cancellation.
- **Mock Data**: Includes sample bookings for testing purposes.
- **Environment Configuration**: Uses a `.env` file for securely managing API keys.

## Prerequisites
- Python 3.8+
- LiveKit Agents framework
- Google Gemini API key (for the RealtimeModel)
- Dependencies listed in `requirements.txt`
- A `.env` file with the following variable:
  ```
  GEMINI_API_KEY=your_gemini_api_key_here
  ```

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/pavan091220002/Hotel-voice-bot
   cd Hotel-voice-bot
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the project root and add your Gemini API key:
   ```plaintext
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## Project Structure
- `agent.py`: Main entry point for the LiveKit agent, defines the `HotelAssistant` class, and handles session setup and booking requests.
- `booking.py`: Contains the `Booking` dataclass and `BookingSystem` class for managing bookings and room availability.
- `prompts.py`: Defines the assistant's instructions and welcome message.
- `requirements.txt`: Lists Python dependencies.
- `.env`: Stores environment variables (e.g., API keys).

## Usage
1. **Run the Agent**:
   Start the LiveKit agent with the following command:
   ```bash
   python agent.py dev
   ```

2. **Test in LiveKit Agent Playground**:
   - Ensure the LiveKit server is running and configured.
   - Open the LiveKit Agent Playground in your browser.
   - Connect to the agent session to interact with the assistant.
   - The assistant will greet you with a welcome message and prompt for your name, address, and room type (single, double, or suite).
   - Follow the prompts to make a booking. The assistant will confirm the booking or inform you if the room is unavailable or if you have an existing booking.

## Testing with Mock Data
The `BookingSystem` class includes mock bookings for testing:
- "scary", "Nellore", "single"
- "arjun", "tirupati", "double"
- "deepak", "Nellore", "suite"

You can test the assistant by attempting to book with these names to trigger the "existing booking" response or use new names to create bookings.

## Room Availability
- Single rooms: 10 available
- Double rooms: 5 available
- Suite rooms: 2 available

The system checks availability before creating a booking and updates the booking counter accordingly.


## Troubleshooting
- **API Key Issues**: Verify that the `GEMINI_API_KEY` is correctly set in the `.env` file.
- **Dependency Errors**: Ensure all dependencies in `requirements.txt` are installed.
- **LiveKit Connection Issues**: Check that the LiveKit server is running and accessible.
- **Booking Errors**: If bookings fail, verify room availability or check for existing bookings with the same guest name.

from dotenv import load_dotenv
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import noise_cancellation, google
from prompts import AGENT_INSTRUCTIONS, WELCOME_MESSAGE
from booking import BookingSystem, Booking
import os

load_dotenv()

class HotelAssistant(Agent):
    
    def __init__(self) -> None:
        super().__init__(
            instructions=AGENT_INSTRUCTIONS,
            llm=google.beta.realtime.RealtimeModel(
                voice="Aoede",
                temperature=0.8,
                api_key=os.getenv("GEMINI_API_KEY")
            )
        )
        self.booking_system = BookingSystem()

    async def process_booking_request(self, guest_name: str, address: str, room_type: str):
        """Process a booking request with name, address, and room type."""
        try:
            existing_booking = self.booking_system.has_existing_booking(guest_name)
            if existing_booking:
                return (f"Sorry, {guest_name}, you already have a booking. "
                        f"Booking ID: {existing_booking.booking_id}, Room Type: {existing_booking.room_type}, "
                        f"Address: {existing_booking.address}. Would you like to contact a staff member for assistance?")
            
            booking = self.booking_system.create_booking(
                guest_name=guest_name,
                address=address,
                room_type=room_type.lower()
            )
            if booking:
                return (f"Booking confirmed for {guest_name}! Booking ID: {booking.booking_id}, "
                        f"Room Type: {booking.room_type}, Address: {booking.address}. "
                        f"Thank you for choosing Stellar Haven Hotels!")
            else:
                return f"Sorry, no {room_type} rooms are available. Would you like to try another room type?"
        except Exception as e:
            return f"Error processing booking: {str(e)}. Please try again or contact our staff."

async def entrypoint(ctx: agents.JobContext):
    try:
        session = AgentSession()

        await session.start(
            room=ctx.room,
            agent=HotelAssistant(),
            room_input_options=RoomInputOptions(
                video_enabled=True,
                noise_cancellation=noise_cancellation.BVC(),
            ),
        )

        await ctx.connect()

        await session.generate_reply(
            instructions=WELCOME_MESSAGE,
        )
    except Exception as e:
        print(f"Error in entrypoint: {str(e)}")
        raise

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
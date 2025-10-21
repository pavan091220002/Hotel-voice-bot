from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Booking:
    guest_name: str
    address: str
    room_type: str
    booking_id: int

class BookingSystem:
    def __init__(self):
        self.bookings: List[Booking] = []
        self.booking_counter = 1
        self.rooms = {
            "single": 10,
            "double": 5,  
            "suite": 2   
        }
        self._add_mock_data()

    def _add_mock_data(self):
        """Add mock bookings for testing."""
        mock_bookings = [
            Booking("scary", "Nellore", "single", self.booking_counter),
            Booking("arjun", "tirupati", "double", self.booking_counter + 1),
            Booking("deepak", "Nellore", "suite", self.booking_counter + 2),
        ]
        self.bookings.extend(mock_bookings)
        self.booking_counter += len(mock_bookings)

    def has_existing_booking(self, guest_name: str):
        """Check if the guest already has a booking."""
        for booking in self.bookings:
            if booking.guest_name.lower() == guest_name.lower():
                return booking
        return None

    def check_availability(self, room_type: str):
        """Check if a room of the specified type is available."""
        if room_type not in self.rooms:
            return False
        booked_count = sum(1 for booking in self.bookings if booking.room_type == room_type)
        return booked_count < self.rooms[room_type]

    def create_booking(self, guest_name: str, address: str, room_type: str):
        """Create a new booking if a room is available."""
        if not self.check_availability(room_type):
            return None
        booking = Booking(
            guest_name=guest_name,
            address=address,
            room_type=room_type,
            booking_id=self.booking_counter
        )
        self.bookings.append(booking)
        self.booking_counter += 1
        return booking
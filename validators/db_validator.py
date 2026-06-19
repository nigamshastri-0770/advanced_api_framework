def validate_booking_exists(db, booking_id):

    result = db.execute(
        f"SELECT * FROM bookings WHERE id={booking_id}"
    )

    assert len(result) > 0, "Booking not found in DB"
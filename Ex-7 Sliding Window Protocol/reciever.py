import os
import random
import time

def receive_frames():
    sender_buffer = "Sender_Buffer.txt"
    receiver_buffer = "Receiver_Buffer.txt"
    expected_frame = 0

    while True:
        # Check if the sender has written to the buffer
        if os.path.exists(sender_buffer):
            with open(sender_buffer, "r") as f:
                frames = f.readlines()

            for frame in frames:
                frame_number = int(frame.split()[1][:-1])  # Extract the frame number
                data = frame.split(":")[1].strip()

                print(f"Received Frame {frame_number}: {data}")

                # Simulate an error randomly
                if random.random() < 0.2:
                    print(f"Simulating error for Frame {frame_number}")
                    ack_message = f"NACK {frame_number}"
                elif frame_number == expected_frame:
                    print(f"Frame {frame_number} is as expected.")
                    ack_message = f"ACK {frame_number}"
                    expected_frame += 1
                else:
                    print(f"Frame {frame_number} is not as expected. Expected Frame {expected_frame}.")
                    ack_message = f"NACK {expected_frame}"

                # Write the ACK/NACK to the receiver buffer
                with open(receiver_buffer, "w") as f:
                    f.write(ack_message)

                # Simulate processing time
                time.sleep(1)

            # Clear sender buffer for next iteration
            os.remove(sender_buffer)
        else:
            # Wait before checking again
            time.sleep(0.5)

# Start receiving frames
receive_frames()

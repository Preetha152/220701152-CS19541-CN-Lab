import time
import os

def send_frames(window_size, message):
    sender_buffer = "Sender_Buffer.txt"
    receiver_buffer = "Receiver_Buffer.txt"

    frames = [[i, message[i]] for i in range(len(message))]
    current_frame = 0

    while current_frame < len(frames):
        print(f"Sending frames {current_frame} to {min(current_frame + window_size, len(frames)) - 1}")
        
        # Write frames to sender buffer
        with open(sender_buffer, "w") as f:
            for i in range(current_frame, min(current_frame + window_size, len(frames))):
                f.write(f"Frame {frames[i][0]}: {frames[i][1]}\n")

        # Simulate sending frames
        time.sleep(1)

        # Wait for acknowledgment
        while not os.path.exists(receiver_buffer):
            time.sleep(0.5)
        
        with open(receiver_buffer, "r") as f:
            ack_data = f.read().strip()

        # Process the acknowledgment
        if ack_data.startswith("ACK"):
            ack_number = int(ack_data.split()[1])
            print(f"Received ACK {ack_number}")
            if ack_number >= current_frame:
                current_frame = ack_number + 1
        elif ack_data.startswith("NACK"):
            nack_number = int(ack_data.split()[1])
            print(f"Received NACK {nack_number}")
            current_frame = nack_number

        # Clear receiver buffer for next iteration
        os.remove(receiver_buffer)

    print("All frames sent and acknowledged!")

# Input from the user
window_size = int(input("Enter window size: "))
message = input("Enter the text message to send: ")

# Send the frames
send_frames(window_size, message)

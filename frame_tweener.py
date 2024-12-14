import cv2
import numpy as np

def generate_tween_frames(frame1, frame2, alpha):
	"""
	Generate tween frames by blending two frames using the specified alpha value.
	"""
	return cv2.addWeighted(frame1, 1 - alpha, frame2, alpha, 0)

def draw_text_on_frame(frame, text, position, color, font_scale=0.5, thickness=1):
	"""
	Draw solid text on a frame at a given position.
	"""

	temp_frame = frame.copy()
	return cv2.putText(temp_frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness, cv2.LINE_AA)

# Load the spritesheet
image_path = 'Input.png'
spritesheet = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

# Input frame grid dimensions
vframes = int(input("Vertical Frames: "))
hframes = int(input("Horizontal Frames: "))

# Extract frames
height, width, channels = spritesheet.shape

frame_width = width // hframes
frame_height = height // vframes

# Container for all frames
frames_by_row = []

# Collect all frames row by row
for v in range(vframes):
	row_frames = []
	for h in range(hframes):
		frame = spritesheet[
			v * frame_height:(v + 1) * frame_height,  # Vertical slice
			h * frame_width:(h + 1) * frame_width    # Horizontal slice
		]
		row_frames.append(frame)
	frames_by_row.append(row_frames)

# Tween settings
tween_count = 3  # Number of tween frames between key frames

# Process each row to generate tweens
final_rows = []

for row_frames in frames_by_row:
	tween_frames = []

	# Generate tween frames between consecutive frames
	for i in range(len(row_frames) - 1):
		for t in range(1, tween_count + 1):
			alpha = t / (tween_count + 1)
			tween_frames.append(generate_tween_frames(row_frames[i], row_frames[i + 1], alpha))

	# Combine original and tween frames into a new row
	final_row = []
	for i in range(len(row_frames) - 1):
		final_row.append(row_frames[i])
		final_row.extend(tween_frames[i * tween_count:(i + 1) * tween_count])
	final_row.append(row_frames[-1])

	final_rows.append(final_row)

# Combine rows into a final spritesheet
final_width = len(final_rows[0]) * frame_width
final_height = len(final_rows) * frame_height
final_spritesheet = np.zeros((final_height, final_width, channels), dtype=np.uint8)

# Populate the new spritesheet row by row
for row_idx, row in enumerate(final_rows):
	for col_idx, frame in enumerate(row):
		y_start = row_idx * frame_height
		y_end = y_start + frame_height
		x_start = col_idx * frame_width
		x_end = x_start + frame_width

		final_spritesheet[y_start:y_end, x_start:x_end] = frame

# Save the tween spritesheet
output_path = 'tween_spritesheet.png'
cv2.imwrite(output_path, final_spritesheet)
print(f"Tween spritesheet saved to '{output_path}'")


# --- Generate Quantized Spritesheet with Text Overlay ---
quant_spritesheet = np.zeros((final_height, final_width, channels), dtype=np.uint8)  # Transparent background
total_frame_count = 0  # Global frame counter

for row_idx, row in enumerate(final_rows):
	for col_idx, frame in enumerate(row):
		# Frame position in spritesheet
		y_start = row_idx * frame_height
		y_end = y_start + frame_height
		x_start = col_idx * frame_width
		x_end = x_start + frame_width

		# Copy the frame from the final spritesheet
		frame_copy = np.zeros((frame_height, frame_width, 4), dtype=np.uint8)  # Transparent frame

		# Add text (Red: Total Count, Blue: VFrame, Green: HFrame) with full alpha (255)
		frame_copy = draw_text_on_frame(frame_copy, f"T: {total_frame_count}", (5, 15), (255, 0, 0,255))  # Red text
		frame_copy = draw_text_on_frame(frame_copy, f"V: {row_idx+1}", (5, 30), (0, 255, 0,255))  # Green text
		frame_copy = draw_text_on_frame(frame_copy, f"H: {col_idx+1}", (5, 45), (0, 0, 255,255))  # Blue text

		# Replace the frame with the text-overlay frame into quant_spritesheet
		quant_spritesheet[y_start:y_end, x_start:x_end] = frame_copy

		total_frame_count += 1

# Save the quantized spritesheet
quant_output_path = 'quant_tween_spritesheet.png'
cv2.imwrite(quant_output_path, quant_spritesheet)
print(f"Quantized tween spritesheet saved to '{quant_output_path}'")
